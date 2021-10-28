from django import forms
from .models import Doctor, Appointment, Admitted, PatientDischarge
import datetime
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('doctor_name', 'doctor_address', 'doctor_phone', 'doctor_mail', 'department', 'doctor_fee')

        widgets = {
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_address': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'doctor_fee': forms.TextInput(attrs={'class': 'form-control'}),
        }


# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ('doctor', 'name', 'address', 'phone', 'symptoms', 'age', 'appointment_date', 'time')

#         widgets = {
#             'doctor': forms.Select(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'symptoms': forms.TextInput(attrs={'class': 'form-control'}),
#             'age': forms.TextInput(attrs={'class': 'form-control'}),
#             'appointment_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'mm-dd-yy'}),
#             'time': forms.TextInput(attrs={'class': 'form-control'}),

            
#         }        


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'address', 'phone', 'symptoms', 'symptoms_details', 'age', 'appointment_date', 'time')

        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            # 'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'symptoms': forms.Select(attrs={'class': 'form-control'}),
            'symptoms_details': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }


class AdmittedForm(forms.ModelForm):
    class Meta:
        model = Admitted
        fields = ('patient_name', 'symptoms', 'doctor', 'room_no', 'room_service', 'admited_date' )

        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'symptoms': forms.Select(attrs={'class': 'form-control'}),
            'room_no': forms.TextInput(attrs={'class': 'form-control'}),
            'room_service': forms.TextInput(attrs={'class': 'form-control'}),
            'admited_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            

        }


class DischargForm(forms.ModelForm):
    class Meta:
        model = PatientDischarge
        fields = ('assign_doctor', 'admitted', 'release_date', 'medicine_cost', 'other_charge')

        widgets = {
            'assign_doctor': forms.Select(attrs={'class': 'form-control'}),
            'admitted': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.TextInput(attrs={'class': 'form-control'}),
            'medicine_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'other_charge': forms.TextInput(attrs={'class': 'form-control'}),

        }