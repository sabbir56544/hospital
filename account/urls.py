from django.urls import path
from .views import *

urlpatterns = [
    path('signup', sign_up_view, name='sign-up'),
    path('login', log_in_view, name='log-in'),
    path('patient/appointment/view', patient_appointment_view, name='patient-appointment-view'),

]