from django.urls import path
from hospital.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('doctor/list', doctor_list, name='doctor-list'),
    path('doctor/create', doctor_create, name='doctor-create'),
    path('doctor/edit/<int:pk>', DoctorEdit.as_view(), name='doctor-edit'),
    path('doctor/delete/<int:pk>', delete_doctor, name='doctor-delete'),

    # // appointment
    path('appointment/list', appointment_list, name='appointment-list'),
    path('appointment/create', appointment_create, name='appointment-create'),
   

    # // admited patient
    path('admitted/list', admitted_list, name='patient-admit'),
    path('admitted/create', admit_create_view, name='patient-admit-create'),

    # // discharge patient
    path('discharge/list', discharge_patient, name='discharge-patient-list'),
    path('discharge/<int:pk>', discharge_view, name='discharge-view'),
    path('discharge/patient/detail/<int:pk>', discharge_patient_detail, name='discharge-patient-detail'),

    path('pdf_download/<int:pk>', download_pdf_view, name="pdf_download"),

    # // patient appointment
    path('confirm/<int:id>', confirm_view, name='confirm'),


    
]