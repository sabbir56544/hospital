from django.contrib import admin
from .models import Doctor, Appointment, PatientDischarge, Admitted

admin.site.register(Doctor)

admin.site.register(Appointment)
admin.site.register(PatientDischarge)
admin.site.register(Admitted)
