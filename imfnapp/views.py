from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
import json
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')

def loginforms(request):
    return render(request,'login.html')

def adminform(request):
    return render(request,'admin.html') 

def hospital_index(request):
    return render(request,'hospitalindex.html')

def doctor_index(request):
    return render(request,'doctorindex.html')

def patient_index(request):
    return render(request,'patientindex.html')

def ambulance_index(request):
    return render(request,'ambulanceindex.html')

def doctor_index(request):
    return render(request,'doctorindex.html')    
    # return render(request,'doctorindex.html') 

def pharmacy_index(request):
    return render(request,'pharmacyindex.html')    

def Register_hospital(request): 
        if request.method == 'POST':
            form=hospitalform(request.POST)
            login=loginform(request.POST)
            if form.is_valid() and login.is_valid():
                login_data=login.save(commit=False)
                print(login_data)
                login_data.user_type='hospital'
                login_data.save()
                hosp=form.save(commit=False)
                hosp.Login_id=login_data
                hosp.save()
            return redirect('/')
        else:        
            form=hospitalform() 
            login=loginform()
        return render(request,"hospital.html",{'form':form,'login':login})

def Register_ambulance(request):

    if request.method == 'POST':
        form=ambulanceform(request.POST,request.FILES)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            login_data.user_type='ambulance'
            login_data.save()
            amb=form.save(commit=False)
            hospital = form.cleaned_data['hospital_id']
            amb.hospital_id=hospital
            amb.Login_id = login_data
            amb.save()
            return redirect('/')
    else:
        form=ambulanceform()
        login=loginform()
    return render(request,"ambulance.html",{'form':form,'login':login}) 

def register_doctor(request):
    if request.method == 'POST':
        form = doctorform(request.POST, request.FILES)
        login = loginform(request.POST)

        if form.is_valid() and login.is_valid():
            login_data = login.save(commit=False)
            login_data.user_type = 'doctor'
            login_data.save()
            doc = form.save(commit=False)
            hospital = form.cleaned_data['hospital_name']
            # doc.hospital_name = hospital
            doc.login_id = login_data
            doc.hospital_login_id = hospital
            doc.save()
            return redirect('/')

    else:
        form = doctorform() 
        login = loginform() 

    return render(request, 'doctors.html', {'form': form, 'login': login})

def hospital_login(request):
    if request.method == 'POST':
        form = logincheckform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            
            try:
                user = login.objects.get(Email=username)
                if user.Password == password:
                    if user.user_type == 'hospital':
                        request.session['hospital_id'] = user.id
                        return redirect('hospital_home')
                    elif user.user_type == 'ambulance':
                        request.session['ambulance_id'] = user.id
                        return redirect('ambulance_home')
                    elif user.user_type == 'patient':
                        request.session['patient_id'] = user.id
                        return redirect('patient_home')
                    elif user.user_type == 'doctor':
                        request.session['doctor_id'] = user.id
                        return redirect('doctor_home')
                    elif user.user_type == 'pharmacy':
                        request.session['pharm_id'] = user.id
                        return redirect('pharmacy_home')
                else:
                    messages.error(request, 'Invalid password')
            except login.DoesNotExist:  # Correcting the exception handling
                messages.error(request, 'User does not exist')

    else:
        form = logincheckform()
    return render(request, "login.html", {'form': form})

def datatable(request):
    hospitals=hospital.objects.all()
    return render(request,"hosdatatable.html",{'hospitals':hospitals})

def datatables(request):
    ambulances=ambulance.objects.all()
    return render(request,"ambdatatable.html",{'ambulances':ambulances})

def doctordatatable(request):
    doctors=doctor.objects.all()
    return render(request,'datatable.html',{'doctors':doctors}) 

def patientdatatable(request):
    patients=patient.objects.all()
    return render(request,'patientdatatable.html',{'patients':patients}) 


 

def hospitalprofile(request):
    hospital_id = request.session.get('hospital_id')
    print(hospital_id)
    hospital_login_data = get_object_or_404(login,id=hospital_id)
    print("data")
    hospital_data = get_object_or_404(hospital,Login_id=hospital_login_data)
    if request.method == 'POST':
        form = hospitaleditform(request.POST,instance=hospital_data)
        loginss = logineditform(request.POST,instance=hospital_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('hospital_home')
    else:        
        form = hospitaleditform(instance = hospital_data) 
        loginss = logineditform(instance = hospital_login_data)
    return render(request,"hospitalprofile.html",{'form':form,'loginss':loginss})

def ambulanceprofile(request):
    ambulance_id = request.session.get('ambulance_id')

    print(ambulance_id)


    ambulance_login_data = get_object_or_404(login,id=ambulance_id)
    ambulance_data = get_object_or_404(ambulance,Login_id=ambulance_login_data)
 
    if request.method == 'POST':
        form = ambulanceeditform(request.POST,instance=ambulance_data)
        loginss = logineditform(request.POST,instance=ambulance_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('ambulance_home')
    else:        
        form = ambulanceeditform(instance = ambulance_data) 
        loginss = logineditform(instance = ambulance_login_data)
    return render(request,"ambulanceprofile.html",{'form':form,'loginss':loginss})    

def hospital_ambulance_view(request):
    hospitals_id=request.session.get('hospital_id')
    hospitalss = get_object_or_404(hospital,Login_id=hospitals_id)
    ambulances=ambulance.objects.filter(hospital_id=hospitalss)
    return render(request,"ambulances.html",{'ambulances':ambulances})


def register_patient(request):
    if request.method=='POST':
        form=patientform(request.POST)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            login_data.user_type='patient'
            login_data.save()
            pat=form.save(commit=False)
            pat.Login_id=login_data
            pat.save()
            return redirect('/')
    else:        
        form=patientform()
        login=loginform() 
    return render(request,"patient.html",{'form':form,'login':login})

def profile(request):
    patient_id = request.session.get('patient_id')
    print(patient_id)
    patient_login_data = get_object_or_404(login,id=patient_id)
    patient_data = get_object_or_404(patient,Login_id=patient_login_data)

    if request.method == 'POST':
        form = profileform(request.POST,instance=patient_data)
        loginss = logineditform(request.POST,instance=patient_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('patient_home')
    else: 
        form = profileform(instance = patient_data) 
        loginss = logineditform(instance = patient_login_data)
    return render(request,"profile.html",{'form':form,'loginss':loginss})

def doctorprofile(request):
    doctor_id = request.session.get('doctor_id')
    print(doctor_id)
    doctor_login_data = get_object_or_404(login,id=doctor_id)
    doctor_data = get_object_or_404(doctor,login_id=doctor_login_data)

    if request.method == 'POST':
        form = doctorprofileform(request.POST,instance=doctor_data)
        loginss = loginform(request.POST,instance=doctor_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('doctor_home')
    else:        
        form = doctorprofileform(instance = doctor_data) 
        loginss = loginform(instance = doctor_login_data)
        return render(request,"doctorprofile.html",{'form':form,'loginss':loginss})    


def search_hospital(request):
    query=request.GET.get('search')
    print(query)
    hospitals=hospital.objects.all()
    if query:
        hospitals=hospital.objects.filter(Q(Hospital_Name__icontains=query) | Q(District__icontains=query) | Q(City__icontains=query))
    return render(request,'hospitalsearch.html',{'hospitals':hospitals,'query':query})

def hospital_doctor_view(request):
    hospital_id=request.session.get('hospital_id')
    hospitals = get_object_or_404(hospital,Login_id=hospital_id)
    doctorss=doctor.objects.filter(hospital_login_id=hospitals)
    return render(request,'doctorsdetails.html',{'doctorss':doctorss})   

def payments(request,amount,appid):
    if request.method=='POST':
        form=paymentform(request.POST)
        print(form)
        if form.is_valid():
            a=form.save(commit=False)
            a.Amount=amount
            a.save()
            b=appointment.objects.get(id=appid)
            b.Payment_Status=1
            b.save()
            return redirect('patient_home') 
    else:
        form=paymentform()                              
    return render(request,'payment.html',{'form':form})    
 
def doctor_search(request,id):
    doctorrs=doctor.objects.filter(hospital_login_id=id)
    return render(request,'doctorsearch.html',{'doctorrs':doctorrs})  

def appointments(request,id):
    patient_id = request.session.get('patient_id')
    # print(patient_id)
    patient_login_data = get_object_or_404(login,id=patient_id)
    doctorlogin = get_object_or_404(login,id=id)
    doctortbl=get_object_or_404(doctor,login_id=id)
    patient_data = get_object_or_404(patient,Login_id=patient_login_data)
    if request.method=='POST':
        form=appointmentform(request.POST)
        if form.is_valid():
            app=form.save(commit=False)
            app.patient_login_id=patient_login_data
            app.doctor_login_id=doctorlogin
            app.save()
            
            return redirect('payment',doctortbl.consultation_fee,app.id)
    else:        
        form=appointmentform() 
    return render(request,'appointment.html',{'form':form})

def consultation(request,id):
    doctor_data = get_object_or_404(doctor,id=id)
    if request.method=='POST':
        form=consultationform(request.POST)
        if form.is_valid():
            cons=form.save(commit=False)
            cons.consultation_fee = form.cleaned_data['consultation_fee']
            cons.id = doctor_data.id
            cons.save(update_fields=['consultation_fee'])
            
        return redirect('hospital_doctor_view')
    else:
        form=consultationform()
    return render(request,'consultation.html',{'form':form})

def view_appointment(request):
    doctor_id=request.session.get('doctor_id')
    doctor_appoin = get_object_or_404(login,id=doctor_id)
    appointments=appointment.objects.filter(Payment_Status=1,doctor_login_id=doctor_appoin).select_related('patient_login_id__patient')
    return render(request,'viewappoints.html',{'appointments':appointments})

def edit_appointments(request,id):
    apps=get_object_or_404(appointment,id=id)
    if request.method=='POST':
        form=appointmentform(request.POST,instance=apps)
        if form.is_valid():
            form.save()
            return redirect('patient_home')
    else:
        form=appointmentform(instance=apps)
    return render(request,'editappointment.html',{'form':form})

def cancel_appointment(request,id):
    b=get_object_or_404(appointment,id=id)
    b.Cancel_status=1
    b.save()
    messages.success(request,"Appointment canceled successfully.")
    return redirect('patient_home')


def views_appointments(request):
    patient_id=request.session.get('patient_id')
    patient_appoin = get_object_or_404(login,id=patient_id)
    appointments=appointment.objects.filter(Payment_Status=1,patient_login_id=patient_appoin).select_related('patient_login_id__patient')
    return render(request,'viewappoin.html',{'appointments':appointments})

def delete_appointment(request,id):
    c=get_object_or_404(appointment,id=id)
    c.delete()
    return redirect('patient_home')

def video_conference(request, id):
    video = get_object_or_404(appointment, id=id)
    user_type = None
    doctor_id=request.session.get('doctor_id')
    dr = get_object_or_404(login, id=doctor_id)

    user_type = dr.user_type

    return render(request, 'videoconference.html', {'video': video, 'user_type': user_type})


def save_appointment_url(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        if url:
            appointments = get_object_or_404(appointment,id=id)
            appointments.Url = url
            appointments.save()

            return JsonResponse({'success': True, 'message': 'URL saved successfully'})

        return JsonResponse({'success': False, 'message': 'No URL provided'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

def patient_search(request):
    query=request.GET.get('search')
    print(query)
    patientss=patient.objects.all()
    if query:
        patientss=patient.objects.filter(Q(MRnumber__icontains=query)) 
    return render(request,'patientsearch.html',{'patientss':patientss,'query':query}) 

def amb_search(request,id):
    hospitals_id=request.session.get('hospital_id')
    hospitalss = get_object_or_404(hospital,Login_id=hospitals_id)
    Patient=get_object_or_404(patient,id=id)
    # pat=patient.objects.filter(MRnumber=Patient)
    ambs=ambulance.objects.filter(hospital_id=hospitalss)
    return render(request,'ambsearch.html',{'ambs':ambs,'pat':Patient}) 


def save_location(request):
    hospitals_id=request.session.get('hospital_id')
    hospitalss = get_object_or_404(hospital,Login_id=hospitals_id)
    if request.method == 'POST':
        data = json.loads(request.body)

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        patid= data.get('patid')
        ambid= data.get('ambid')
        hosid= data.get('hosid')
        p=get_object_or_404(patient,id=patid)
        amb=get_object_or_404(ambulance,id=ambid)
        
        if not all([latitude, longitude,patid,ambid]):
            return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

        # Create and save the Location instance
        location = Location(
            latitude=latitude,
            longitude=longitude,
            pat_id=p,
            amb_login_id=amb,
            hosp_id=hospitalss

        )
        location.save()

        return JsonResponse({"status": "success"})
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

def Register_pharmacy(request):
    hospital_id=request.session.get('hospital_id') 
    hosp=get_object_or_404(hospital,Login_id=hospital_id)
    if request.method == 'POST':
        form=pharmacyform(request.POST)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            print(login_data)
            login_data.user_type='pharmacy'
            login_data.save()
            pharm=form.save(commit=False)
            pharm.hos_id=hosp
            pharm.Login_id=login_data
            pharm.save()
            return redirect('hospital_home')    
    else:        
        form=pharmacyform() 
        login=loginform()
    return render(request,"pharmacy.html",{'form':form,'login':login})

def view_location(request):
    ambulance_id=request.session.get('ambulance_id')
    ambs=get_object_or_404(ambulance,Login_id=ambulance_id)
    locations=Location.objects.filter(amb_login_id=ambs)
    return render(request,'viewlocation.html',{'locations':locations})

def hospital_view_location(request):
    hospital_id=request.session.get('hospital_id')
    hosps=get_object_or_404(hospital,Login_id=hospital_id)
    locations=Location.objects.filter(hosp_id=hosps)
    return render(request,'viewlocations.html',{'locations':locations})

def pharmacyprofile(request):
    pharm_id = request.session.get('pharm_id')
    print(pharm_id)
    pharmacy_login_data = get_object_or_404(login,id=pharm_id)
    print("data")
    pharmacy_data = get_object_or_404(pharmacy,Login_id=pharmacy_login_data)
    if request.method == 'POST':
        form = pharmacyform(request.POST,instance=pharmacy_data)
        loginss = loginform(request.POST,instance=pharmacy_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('pharmacy_home')
    else:        
        form = pharmacyform(instance = pharmacy_data) 
        loginss = loginform(instance = pharmacy_login_data)
    return render(request,"pharmacyprofile.html",{'form':form,'loginss':loginss})

def Register_medicine(request): 
    if request.method == 'POST':
        form=medicinesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy_home')    
    else:        
        form=medicinesform() 
    return render(request,"medicine.html",{'form':form})


def patient_transfer(request):
    hospital_id=request.session.get('hospital_id')
    hospss=get_object_or_404(hospital,Login_id=hospital_id)
    query=request.GET.get('search')
    print(query)
    pats=patient.objects.all()
    if query:
        pats=patient.objects.filter(Q(MRnumber__icontains=query)) 
    return render(request,'patienttransfer.html',{'pats':pats,'query':query})   

def view_hospital(request,id):
    hospital_id=request.session.get('hospital_id')
    patients=get_object_or_404(patient,id=id)
    query=request.GET.get('search')
    print(query)
    hospitals=hospital.objects.filter(~Q(Login_id = hospital_id))
    if query:
        hospitals=hospital.objects.filter(Q(Hospital_Name__icontains=query) | Q(District__icontains=query) | Q(City__icontains=query))
    return render(request,'viewhospital.html',{'hospitals':hospitals,'query':query,'patients':patients})

def view_medicine(request):
    medicine_id=request.session.get('pharm_id')
    med=get_object_or_404(pharmacy,Login_id=medicine_id)
    query=request.GET.get('search')
    print(query)
    meds=medicines.objects.filter(Pharmacy_id=med)
    if query:
        meds=medicines.objects.filter(Q(medicine_name__icontains=query) | Q(medicine_category__icontains=query)) 
    return render(request,'viewmedicine.html',{'meds':meds,'query':query})

def change_medicine(request,id):
    meds=get_object_or_404(medicines,id=id)
    if request.method=='POST':
        form=medicinesform(request.POST,instance=meds)
        if form.is_valid():
            form.save()
            return redirect('pharmacy_home')
    else:
        form=medicinesform(instance=meds)
    return render(request,'editmedicine.html',{'form':form})

def remove_medicine(request,id):
    c=get_object_or_404(medicines,id=id)
    c.delete()
    return redirect('pharmacy_home')

def confirm_transfer(request,id,ids):
    hospital_ids=request.session.get('hospital_id')
    old_hospital_id=get_object_or_404(hospital,Login_id=hospital_ids)
    patient_id=get_object_or_404(patient,id=id)
    hospital_id=get_object_or_404(hospital,id=ids)
    transferpatient.objects.create(from_hospital=old_hospital_id,pat_id=patient_id,to_hospital=hospital_id)
    return redirect('hospital_home')

def doctor_view_medicine(request):
    doctor_id=request.session.get('doctor_id')
    docs=get_object_or_404(doctor,login_id=doctor_id)
    hos=doctor.hospital_login_id
    # pharms=pharmacy.objects.filter(hos_id=hos)
    query=request.GET.get('search')
    print(query)
    meds=medicines.objects.filter(Pharmacy_id__hos_id=docs.hospital_login_id)  
    if query:
        meds=medicines.objects.filter(Q(medicine_name__icontains=query) | Q(medicine_category__icontains=query))  
    return render(request,'doctviewmed.html',{'meds':meds,'query':query})

def view_transfer(request):
    hospital_id=request.session.get('hospital_id')
    hoss=get_object_or_404(hospital,Login_id=hospital_id)
    trans=transferpatient.objects.filter(from_hospital=hoss)
    return render(request,'viewtransfer.html',{'trans':trans})

def transfer_view(request):
    hospital_id=request.session.get('hospital_id')
    hoss=get_object_or_404(hospital,Login_id=hospital_id)
    trans=transferpatient.objects.filter(to_hospital=hoss)
    return render(request,'viewtransfer.html',{'trans':trans})

def add_prescription(request,id):
    appoints=get_object_or_404(appointment,id=id)
    if request.method=="POST":
        form=Prescriptionform(request.POST,instance=appoints)
        if form.is_valid():
            pres=form.cleaned_data['Prescription']
            appoints.Prescription=pres
            appoints.save()
            return redirect('view_appointment')

    else:
        form=Prescriptionform(instance=appoints)
    return render(request,'addprescription.html',{'form':form,'appoints':appoints})

























    





  


    




  





