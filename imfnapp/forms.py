from django import forms
from .models import hospital,login,ambulance,patient,doctor,appointment,payment,Location,pharmacy

class hospitalform(forms.ModelForm):

    class Meta:
        model=hospital
        fields=['Hospital_Name','Address','District','City','Contact_No']

class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields=['Email','Password']

class ambulanceform(forms.ModelForm):
    hospital_id= forms.ModelChoiceField(queryset=hospital.objects.all(), empty_label='select')
    class Meta:
        model=ambulance
        fields=['Ambulance_Category','Ambulance_Type','Vehicle_NO','Contact_No','Driver_Name']

class doctorform(forms.ModelForm):
    hospital_name = forms.ModelChoiceField(queryset=hospital.objects.all(), empty_label='select hospital')
    class Meta:
        model = doctor
        fields = ['doctor_name', 'photo', 'gender', 'DOB', 'specialisation', 'year_of_experience', 'contact_no','hospital_name']
        widgets = {
            'password': forms.PasswordInput(),
            'gender': forms.RadioSelect(),
            'DOB': forms.TextInput(attrs={'type': 'date'})
        }
      

class logincheckform(forms.Form):
    Email=forms.CharField(max_length=100, required=True)
    Password=forms.CharField(widget=forms.PasswordInput, required=True)


class hospitaleditform(forms.ModelForm):
    class Meta:
        model = hospital
        fields = ['Hospital_Name','Address','District','City','Contact_No']

class ambulanceeditform(forms.ModelForm):
    class Meta:
        model = ambulance
        fields = ['Ambulance_Category','Ambulance_Type','Vehicle_NO','Contact_No','Driver_Name']

class logineditform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email']

class patientform (forms.ModelForm):
     #password=forms.CharField(widget=forms.PasswordInput)

     class  Meta:
        model=patient
        fields=['name','address','gender','DOB','contact_no']
        widgets ={
          'password': forms.PasswordInput(),
          'gender': forms.RadioSelect(),
          'DOB': forms.TextInput(attrs={'type':'date'})
         }
class profileform(forms.ModelForm):
     #password=forms.CharField(widget=forms.PasswordInput)

     class  Meta:
        model=patient
        fields=['name','address','gender','DOB','contact_no']
        widget = {
            'DOB':forms.DateInput(attrs={'id':'dateob'})
        }

class logineditform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email']

class doctorprofileform(forms.ModelForm):
    
    class Meta:
        model=doctor
        fields=['doctor_name','photo','gender','DOB','specialisation','year_of_experience','contact_no']
        widgets={
            'password' : forms.PasswordInput(),
            'gender' : forms.RadioSelect(),
            'DOB' : forms.TextInput(attrs={'type':'date'})
        }              

class logincheckforms(forms.Form):
    Email=forms.CharField(max_length=100, required=True)
    Password=forms.CharField(widget=forms.PasswordInput, required=True)

class appointmentform(forms.ModelForm):
    class Meta:
        model=appointment
        fields=['Date','Time']
        widgets={
            'Date':forms.TextInput(attrs={'type':'date'}),
            'Time':forms.TextInput(attrs={'type':'time'})

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

    class Meta:
        model=pharmacy
        fields=['Pharmacy_id','contact_no']        

    



