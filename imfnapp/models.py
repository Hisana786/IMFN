from django.db import models
import uuid

class hospital(models.Model):
    Hospital_Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=100)
    District = models.CharField(max_length=30)
    City = models.CharField(max_length=40)
    Contact_No = models.CharField(max_length=15)
    Login_id = models.ForeignKey("login", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.Hospital_Name
  


class login(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10)


class ambulance(models.Model):
    Ambulance_Category = models.CharField(max_length=35)
    Ambulance_Type = models.CharField(max_length=50)
    Vehicle_NO = models.CharField(max_length=15)
    Contact_No = models.CharField(max_length=15)
    Driver_Name = models.CharField(max_length=30)
    Login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    hospital_id = models.ForeignKey("hospital", on_delete=models.CASCADE, null=True, blank=True)


class patient(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default="Male")
    DOB = models.DateField()
    contact_no = models.CharField(max_length=25)
    Login_id = models.OneToOneField("login", on_delete=models.CASCADE, null=True, blank=True,related_name='patient')
    MRnumber=models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.MRnumber:  # Only generate if not already assigned
            self.MRnumber = self.generate_unique_mrnumber()
        super().save(*args, **kwargs)

    def generate_unique_mrnumber(self):
        """Generate a unique MR number"""
        while True:
            new_mrnumber = f"MR-{uuid.uuid4().hex[:5].upper()}"  # Example: MR-AB12CD34E5
            if not patient.objects.filter(MRnumber=new_mrnumber).exists():
                return new_mrnumber

    def __str__(self):
        return f"{self.name} - {self.MRnumber}"
    


class doctor(models.Model):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    
    doctor_name = models.CharField(max_length=25)
    photo = models.FileField(upload_to='uploads')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Male")
    DOB = models.DateField(null=False) 
    specialisation = models.CharField(max_length=40)
    year_of_experience = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    consultation_fee = models.IntegerField(default=0) 
    # OneToOneField for hospital
    hospital_login_id = models.ForeignKey('hospital', on_delete=models.CASCADE, related_name='doctor_login',null=True,blank=True)

    # ForeignKey for login_id
    login_id = models.ForeignKey("login", on_delete=models.CASCADE, related_name="Doctor_login", default=True)

class appointment(models.Model):
    Date=models.DateField(max_length=25)
    Time=models.TimeField(max_length=25)
    doctor_login_id = models.ForeignKey("login", on_delete=models.CASCADE, related_name="doctors", default=True)
    patient_login_id = models.ForeignKey("login", on_delete=models.CASCADE, related_name="patient_login", default=True)
    Current_Date = models.DateField(auto_now_add=True)
    Payment_Status = models.IntegerField(default=0)
    Cancel_status = models.IntegerField(default=0)
    Url = models.URLField(max_length=200,null=True,blank=True)

class payment(models.Model):
    Amount = models.IntegerField(default=0)
    Current_Date = models.DateField(auto_now_add=True)
    Card_owner = models.CharField(max_length=25)
    Card_no = models.CharField(max_length=16)
    Exp_month = models.IntegerField()
    Exp_year = models.IntegerField()
    CVV = models.CharField(max_length=4)

class Location(models.Model):
    latitude = models.CharField(max_length=9)
    longitude = models.CharField(max_length=9)
    amb_login_id = models.ForeignKey("ambulance", on_delete=models.CASCADE, related_name="ambulancs", default=True)
    pat_id = models.ForeignKey("patient", on_delete=models.CASCADE, related_name="patients", default=True)
    hosp_id =  models.ForeignKey("hospital", on_delete=models.CASCADE, related_name="hosps", default=True)
    current_date = models.DateField(auto_now_add=True)

class pharmacy(models.Model):
    Pharmacy_id= models.CharField(max_length=10)
    contact_no = models.CharField(max_length=15)
    Login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    hos_id = models.ForeignKey("hospital", on_delete=models.CASCADE, related_name="hos", default=True)
    def __str__(self):
        return self.Pharmacy_id

class medicines(models.Model):
    medicine_category = models.CharField(max_length=35)
    company_name = models.CharField(max_length=45)
    medicine_name = models.CharField(max_length=45)
    medicine_details = models.CharField(max_length=80)
    amount = models.IntegerField(default=0) 
    Pharmacy_id = models.ForeignKey(pharmacy, on_delete=models.CASCADE, null=True, blank=True) 

class transferpatient(models.Model):
    from_hospital=models.ForeignKey(hospital,on_delete=models.CASCADE,related_name="hospi",default=True)
    to_hospital=models.ForeignKey(hospital,on_delete=models.CASCADE,related_name="hospit",default=True)
    pat_id=models.ForeignKey(patient,on_delete=models.CASCADE,related_name="pat",default=True)
    current_date=models.DateField(auto_now_add=True)      
    





    



