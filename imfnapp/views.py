from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import login,hospital,ambulance, patient,doctor
from .forms import hospitalform,loginform,ambulanceform,logincheckform,hospitaleditform,ambulanceeditform,logineditform, patientform, profileform,doctorform,doctorprofileform

def index(request):
    return render(request,'index.html')

def loginforms(request):
    return render(request,'login.html')

def adminform(request):
    return render(request,'admin.html') 

def hospital_index(request):
    return render(request,'hospitalindex.html')

def ambulance_index(request):
    return render(request,'ambulanceindex.html')

def userform(request):
    return render(request,'user.html')   

def Register_hospital(request): 
    if request.method == 'POST':
        form=hospitalform(request.POST)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            login_data.user_type='hospital'
            login_data.save()
            hosp=form.save(commit=False)
            hosp.Login_id=login_data
            hosp.save()
            return redirect('hospital_home')
    else:        
        form=hospitalform() 
        login=loginform()
    return render(request,"hospital.html",{'form':form,'login':login})

def Register_ambulance(request):
    if request.method == 'POST':
        form=ambulanceform(request.POST)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            login_data.user_type='ambulance'
            login_data.save()
            amb=form.save(commit=False)
            amb.Login_id=login_data
            amb.save()
            return redirect('ambulance_home')
    else:
        form=ambulanceform()
        login=loginform()
    return render(request,"ambulance.html",{'form':form,'login':login}) 

def register_doctor(request):
    if request.method=='POST':
        form=doctorform(request.POST or None,request.FILES)
        login=loginform(request.POST)
        if form.is_valid() and login.is_valid():
            login_data=login.save(commit=False)
            login_data.user_type='doctor'
            login_data.save()
            doc=form.save(commit=False)
            doc.login_id=login_data
            doc.save()
            return redirect('users')
    else:        
        form=doctorform()
        login=loginform()
         
    return render(request,'doctors.html',{'form':form,'login':login})


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
                        return redirect('users')
                    elif user.user_type == 'doctor':
                        request.session['doctor_id'] = user.id
                        return redirect('users')
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
 

def hospitalprofile(request):
    hospital_id = request.session.get('hostipal_id')
    hospital_login_data = get_object_or_404(login,id=hospital_id)
    hospital_data = get_object_or_404(hospital,Login_id=hospital_login_data)

    if request.method == 'POST':
        form = hospitaleditform(request.POST,instance=hospital_data)
        loginss = logineditform(request.POST,instance=hospital_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('Register_hospital')
    else:        
        form = hospitaleditform(instance = hospital_data) 
        loginss = logineditform(instance = hospital_login_data)
    return render(request,"hospitalprofile.html",{'form':form,'loginss':loginss})

def ambulanceprofile(request):
    ambulance_id = request.session.get('ambulance_id')
    ambulance_login_data = get_object_or_404(login,id=ambulance_id)
    ambulance_data = get_object_or_404(hospital,Login_id=ambulance_login_data)

    if request.method == 'POST':
        form = ambulanceeditform(request.POST,instance=ambulance_data)
        loginss = logineditform(request.POST,instance=ambulance_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('Register_ambulance')
    else:        
        form = ambulanceeditform(instance = ambulance_data) 
        loginss = logineditform(instance = ambulance_login_data)
    return render(request,"ambulanceprofile.html",{'form':form,'loginss':loginss})    

def hospital_ambulance_view(request):
    ambulancess=ambulance.objects.all()
    return render(request,"ambulances.html",{'ambulancess':ambulancess})


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
            return redirect('register_patient')
    else:        
        form=patientform()
        login=loginform() 
    return render(request,"patient.html",{'form':form,'login':login})

def profile(request):
    patient_id = request.session.get('patient_id')
    patient_login_data = get_object_or_404(login,id=patient_id)
    patient_data = get_object_or_404(patient,Login_id=patient_login_data)

    if request.method == 'POST':
        form = profileform(request.POST,instance=patient_data)
        loginss = logineditform(request.POST,instance=patient_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('users')
    else: 
        form = profileform(instance = patient_data) 
        loginss = logineditform(instance = patient_login_data)
    return render(request,"profile.html",{'form':form,'loginss':loginss})

def doctorprofile(request):
    doctor_id = request.session.get('doctor_id')
    doctor_login_data = get_object_or_404(login,id=doctor_id)
    doctor_data = get_object_or_404(doctor,login_id=doctor_login_data)

    if request.method == 'POST':
        print('hi')
        form = doctorprofileform(request.POST,instance=doctor_data)
        loginss = loginform(request.POST,instance=doctor_login_data)
        if form.is_valid() and loginss.is_valid():
            form.save()
            loginss.save()
            return redirect('users')
    else:        
        form = doctorprofileform(instance = doctor_data) 
        loginss = loginform(instance = doctor_login_data)
<<<<<<< HEAD
    return render(request,"doctorprofile.html",{'form':form,'loginss':loginss})  

def hospital_doctor_view(request):
    doctorss= doctor.objects.all()
    return render(request,"doctorsdetails.html",{'doctorss':doctorss})


=======
    return render(request,"doctorprofile.html",{'form':form,'loginss':loginss})    
def search_hospital(request):
    query=request.GET.get('q','')
    hospitals=hospital.objects.all()
    if query:
        hospitals=hospital.filter(Hospital_Name__icontains=query)
>>>>>>> 50f5c167457a801b6170cbe7ab876cf9267287a0

    return render(request,'hospitalsearch.html',{'hospitals':hospitals,'query':query})
