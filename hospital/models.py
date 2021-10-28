from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


departments=[
        ('Cardiologist','Cardiologist'),
        ('Dermatologists','Dermatologists'),
        ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
        ('Allergists/Immunologists','Allergists/Immunologists'),
        ('Anesthesiologists','Anesthesiologists'),
        ('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
    ]



class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_address = models.CharField(max_length=100)
    doctor_phone = models.IntegerField(unique=True)
    doctor_mail = models.EmailField(unique=True)
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    doctor_fee = models.IntegerField(null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    weekly_available = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.doctor_name + ' + ' + self.department

    def get_absolute_url(self):
        return reverse('doctor-list')



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, default="+880", unique=True)
    symptoms = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    symptoms_details = models.TextField(null=True)
    age = models.IntegerField()
    appointment_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    time = models.CharField(max_length=20, null=True)
    is_appointment = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name.username


class Admitted(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    admited_date = models.DateField()
    room_no = models.IntegerField()
    room_service = models.IntegerField()
    symptoms = models.CharField(max_length=100, choices=departments, default='Cardiologist')
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.patient_name


class PatientDischarge(models.Model):
    assign_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    admitted = models.ForeignKey(Admitted, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=False)
    medicine_cost = models.IntegerField(null=True)
    other_charge = models.IntegerField()

    def __str__(self):
        return self.admitted.patient_name if all([self.admitted, self.admitted.patient_name]) else 0

    def days_count(self):
        return self.release_date - self.admitted.admited_date if all([self.admitted, self.admitted.admited_date]) else 0

    def room_bill(self):
        return self.days_count() * self.admitted.room_service if all([self.admitted, self.admitted.room_service])  else 0

    def total_bill(self):
        return self.room_bill().days + self.medicine_cost + self.other_charge + self.assign_doctor.doctor_fee

        
