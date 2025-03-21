from django.urls import path
import imfnapp.userform
from .import views

urlpatterns= [
    path('logins/',views.loginforms,name='logins'),
    path('admins/',views.adminform,name='admins'),
    path('users/',imfnapp.userform.userform,name='users'),
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
    path('doctor_home/',views.doctor_index,name='doctor_home'),
    path('payment/<int:amount>/<int:appid>/',views.payments,name='payment'),
    path('doctor_search/<int:id>/',views.doctor_search,name='doctor_search'),
    path('appointment/<int:id>/',views.appointments,name='appointment'),
    path('consultation/<int:id>/',views.consultation,name='consultation'),
    path('view_appointment/',views.view_appointment,name='view_appointment'),
    path('edit_appointment/<int:id>/',views.edit_appointments,name='edit_appointment'),
    path('cancel_appointment/<int:id>/',views.cancel_appointment,name='cancel_appointment'),
    path('views_appointments/',views.views_appointments,name='views_appointments'),
    path('delete_appointment/<int:id>/',views.delete_appointment,name='delete_appointment'),
    path('video_conference/<int:id>/',views.video_conference,name='video_conference'),
    path('save_appointment_url/<int:id>/',views.save_appointment_url,name='save_appointment_url'),
    path('patient_search/',views.patient_search,name='patient_search'),
    path('amb_search/<int:id>/',views.amb_search,name='amb_search'),
    path('location/',views.save_location,name='location'),
    path('Register_pharmacy/',views.Register_pharmacy,name='Register_pharmacy'),
    path('view_location/',views.view_location,name='view_location'),
    path('hospital_view_location/',views.hospital_view_location,name='hospital_view_location'),
    path('pharmacy_home/',views.pharmacy_index,name='pharmacy_home'),
    path('pharmacyprofile/',views.pharmacyprofile,name='pharmacyprofile')
]

