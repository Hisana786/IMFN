from django.urls import path
from .import views

urlpatterns= [
    path('logins/',views.loginforms,name='logins'),
    path('admins/',views.adminform,name='admins'),
    path('users/',views.userform,name='users'),
    path('ambulance_home/',views.ambulance_index,name='ambulance_home'),
    path('doctor_home/',views.doctor_index,name='doctor_home'),
    path('hospital_home/',views.hospital_index,name='hospital_home'),
    path('patient_home/',views.patient_index,name='patient_home'),
    path('doctor_home/',views.doctor_index,name='doctor_home'),
    path('Register_hospital/',views.Register_hospital,name='Register_hospital'),
    path('Register_ambulance/',views.Register_ambulance,name='Register_ambulance'),
    path('hospital_login/',views.hospital_login,name='hospital_login'),
    path('datatable/',views.datatable,name='datatable'),
    path('datatables/',views.datatables,name='datatables'),
    path('hospitalprofile/',views.hospitalprofile,name='hospitalprofile'),
    path('',views.index,name='index'),
    path('ambulanceprofile/',views.ambulanceprofile,name='ambulanceprofile'),
    path('hospital_ambulance_view/',views.hospital_ambulance_view,name='hospital_ambulance_view'),
    path('register_patient/',views.register_patient,name='register_patient'),
    path('profile/',views.profile,name='profile'),
    path('register_doctor/',views.register_doctor,name='register_doctor'),
    path('doctordatatable/',views.doctordatatable,name='datatable'),
    path('patientdatatable/',views.patientdatatable,name='patientdatatable'),
    path('doctorprofile/',views.doctorprofile,name='doctorprofile'),
    path('patient_home/',views.patient_index,name='patient_home'),
    path('hospital_doctor_view/',views.hospital_doctor_view,name='hospital_doctor_view'),
    path('doctorprofile/',views.doctorprofile,name='doctorprofile'),
    path('doctor_home/',views.doctor_index,name='doctor_home'),
    path('patient_home/',views.patient_index,name='patient_home'),
    path('hospital_doctor_view/',views.hospital_doctor_view,name='hospital_doctor_view'),
    path('hospitalsearch/',views.search_hospital,name='hospitalsearch'),
    path('patient_home/',views.patient_index,name='patient_home'),
    path('doctor_home/',views.doctor_index,name='doctor_home')

]


