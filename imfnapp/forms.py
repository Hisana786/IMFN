from django import forms
from .models import hospital,login,ambulance,patient,doctor,appointment,payment,Location,pharmacy,medicines
from datetime import date

class hospitalform(forms.ModelForm):
    Contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model=hospital
        fields=['Hospital_Name','Address','District','City','Contact_No']
        widget=forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})

class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields=['Email','Password']

class ambulanceform(forms.ModelForm):
    hospital_id= forms.ModelChoiceField(queryset=hospital.objects.all(), empty_label='select')
    Contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model=ambulance
        fields=['Ambulance_Category','Ambulance_Type','Vehicle_NO','Contact_No','Driver_Name']
        widget=forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})


class doctorform(forms.ModelForm):
    contact_no=forms.CharField(max_length=10,min_length=10)
    hospital_name = forms.ModelChoiceField(queryset=hospital.objects.all(), empty_label='select hospital')
    class Meta:
        model = doctor
        fields = ['doctor_name', 'photo', 'gender', 'DOB', 'specialisation', 'year_of_experience', 'contact_no','hospital_name']
        widgets = {
            'password': forms.PasswordInput(),
            'gender': forms.RadioSelect(),
            'DOB': forms.TextInput(attrs={'type': 'date'}),
            'contact_no':forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})
        }
      

class logincheckform(forms.Form):
    Email=forms.CharField(max_length=100, required=True)
    Password=forms.CharField(widget=forms.PasswordInput, required=True)


class hospitaleditform(forms.ModelForm):
    Contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model = hospital
        fields = ['Hospital_Name','Address','District','City','Contact_No']
        widget=forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})

class ambulanceeditform(forms.ModelForm):
    Contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model = ambulance
        fields = ['Ambulance_Category','Ambulance_Type','Vehicle_NO','Contact_No','Driver_Name']
        widget=forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})

class logineditform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email']

class patientform (forms.ModelForm):
     #password=forms.CharField(widget=forms.PasswordInput)
     contact_no=forms.CharField(max_length=10,min_length=10)
     class  Meta:
        model=patient
        fields=['name','address','gender','DOB','contact_no']
        widgets ={
          'password': forms.PasswordInput(),
          'gender': forms.RadioSelect(),
          'DOB': forms.TextInput(attrs={'type':'date'}),
          'contact_no':forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})
         }
class profileform(forms.ModelForm):
     #password=forms.CharField(widget=forms.PasswordInput)
     contact_No=forms.CharField(max_length=10,min_length=10)
     class  Meta:
        model=patient
        fields=['name','address','gender','DOB','contact_no']
        widgets = {
            'DOB':forms.DateInput(attrs={'id':'dateob'}),
            'contact_no':forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})
        }

class logineditform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email']

class doctorprofileform(forms.ModelForm):
    contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model=doctor
        fields=['doctor_name','photo','gender','DOB','specialisation','year_of_experience','contact_no']
        widgets={
            'password' : forms.PasswordInput(),
            'gender' : forms.RadioSelect(),
            'DOB' : forms.TextInput(attrs={'type':'date'}),
            'contact_no':forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})
        }              

class logincheckforms(forms.Form):
    Email=forms.CharField(max_length=100, required=True)
    Password=forms.CharField(widget=forms.PasswordInput, required=True)

class appointmentform(forms.ModelForm):
    class Meta:
        model=appointment
        fields=['Date','Time']
        widgets={
            'Date':forms.TextInput(attrs={'type':'date','min': date.today().strftime('%Y-%m-%d'), 'id':'appoint'}),
            'Time':forms.TextInput(attrs={'type':'time'}),
            'Prescription':forms.Textarea(attrs={'rows': 4, 'cols':50, 'placeholder': 'Enter Prescription...'})

        }    

class paymentform(forms.ModelForm):
    class Meta:
        model=payment
        fields=['Card_owner','Card_no','Exp_month','Exp_year','CVV']   


class consultationform(forms.ModelForm):
    class Meta:
        model=doctor
        fields=['consultation_fee']


class Locationform(forms.ModelForm):
    class meta:
        model=Location
        fields=['']

class pharmacyform(forms.ModelForm):
    Contact_No=forms.CharField(max_length=10,min_length=10)
    class Meta:
        model=pharmacy
        fields=['Pharmacy_id','contact_no']
        widget=forms.TextInput(attrs={'placeholder':'Enter 10-digit phone number'})  

class medicinesform(forms.ModelForm):
    class Meta:
        model=medicines
        fields=['medicine_category','company_name','medicine_name','medicine_details','amount','Pharmacy_id']  

class Prescriptionform(forms.ModelForm):
    class Meta:
        model=appointment
        fields=['Prescription']
        widget={
            'Prescription':forms.Textarea(attrs={'rows': 4, 'cols':50, 'placeholder': 'Enter Prescription...'})
            }


    



