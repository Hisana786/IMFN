from django.db import models


class hospital(models.Model):
    Hospital_Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=100)
    District = models.CharField(max_length=30)
    City = models.CharField(max_length=40)
    Contact_No = models.CharField(max_length=15)
    Login_id = models.ForeignKey("login", on_delete=models.CASCADE, null=True, blank=True)


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
    Login_id = models.ForeignKey("login", on_delete=models.CASCADE, null=True, blank=True)


class doctor(models.Model):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    doctor_name = models.CharField(max_length=25)
    photo = models.FileField(upload_to='uploads')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Male")
    DOB = models.DateField(max_length=25)
    specialisation = models.CharField(max_length=40)
    year_of_experience = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    hospital_name = models.CharField(max_length=40)
    Login_id = models.ForeignKey("login", on_delete=models.CASCADE, default=True)
