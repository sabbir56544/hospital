from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from hospital.models import Doctor, Appointment, PatientDischarge, Admitted
from hospital.forms import DoctorForm, AppointmentForm, AdmittedForm, DischargForm
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, CreateView, View
from django.urls import reverse_lazy,reverse
from account.decorators import admin_only, unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from datetime import datetime
from account.models import Profile

from django.conf import settings
from django.core.mail import send_mail

# // pdf download
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home_view(request):
    doctor = Doctor.objects.all()
    appointment = Appointment.objects.filter(is_appointment=False).order_by('created_at')[0:4]
    admitted = Admitted.objects.all()
    total_doctors = doctor.count()
    total_appointments = appointment.count()
    total_addmiteds = admitted.count()

    doctors = Doctor.objects.all().order_by('-doctor_fee')[:4]

    now = datetime.now() # current date and time
    hour = now.strftime("%H")# current hour
    hour = int(hour)

    appointment = Appointment.objects.filter(is_delete=False)
    appointment_list = Appointment.objects.filter(is_delete=False).order_by('-created_at')[0:5]
    patient = Profile.objects.all()
    appointment_done = Appointment.objects.filter(is_appointment=True, is_delete=False).count()
    appointment_pending = Appointment.objects.filter(is_appointment=False, is_delete=False).count()
  

    context = {
        'total_doctor': total_doctors,
        'total_appointment': total_appointments,
        'total_addmitted': total_addmiteds,
        'doctors': doctors,
        'hour': hour,
        'appointment_done': appointment_done,
        'appointment_pending': appointment_pending,
        'appointment_list': appointment_list,
        'patient': patient,
        'appointments': appointment,
    }  
    return render(request, 'index.html', context)

@login_required

def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
    }  
    return render(request, 'hospital/doctor_list.html', context)

@login_required
@admin_only
def doctor_create(request):
    form = DoctorForm()
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'product was successfully added')
            return redirect('doctor-list')
    context = {
        'form': form,
        'error': "Form is invalid",
    }
    return render(request, 'hospital/doctor_form.html', context)

@method_decorator(admin_only, name='dispatch')
class DoctorEdit(LoginRequiredMixin, UpdateView):
    model = Doctor
    template_name = 'hospital/doctor_form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('doctor-list')    

@login_required
@admin_only
def delete_doctor(request, pk):
    obj = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        messages.warning(request, 'This Doctor was delete successfully')
        obj.delete()
        return HttpResponseRedirect(reverse('doctor-list'))

    return render(request, 'hospital/doctor_delete.html')


# // room booked    
@login_required
@admin_only
def appointment_list(request):
    appointment = Appointment.objects.all()
    context = {
        'appointments': appointment,
    }

    return render(request, 'hospital/appointment_list.html', context)

@login_required

def appointment_create(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment was successfully added')
            return redirect('appointment-list')
    context = {
        'form': form,
        'error': "Form is invalid",
    }
    return render(request, 'hospital/patient_form.html', context)





# // Admitted Patient
@login_required
@admin_only
def admitted_list(request):
    admitted = Admitted.objects.all()
    context = {
        'admitted': admitted,
    }

    return render(request, 'hospital/admitted_list.html', context)

@login_required
@admin_only
def admit_create_view(request):
    form = AdmittedForm()
    if request.method == 'POST':
        form = AdmittedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Admitted Successfully ...')
            return redirect('patient-admit')

    context = {
        'form': form,
    }        

    return render(request, 'hospital/admitted_form.html', context)


# // discharge patient

@login_required
@admin_only
def discharge_patient(request):
    dis_patient = PatientDischarge.objects.all()

    context = {
        'dis_patient': dis_patient,
    }

    return render(request, 'hospital/discharge_patient_list.html', context)


@login_required
@admin_only
def discharge_patient_detail(request, pk):
    discharge_patient = PatientDischarge.objects.get(pk=pk)
    context = {
        'discharge_patient': discharge_patient,
    }

    return render(request, 'hospital/discharge_patient_detail.html', context)
    


@login_required
@admin_only
def discharge_view(request, pk):
    form = DischargForm()
    if request.method == 'POST':
        form = DischargForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Successfull')
            return redirect('discharge-patient')
    context = {
        'form': form,
    }        

    return render(request, 'hospital/discharge.html', context)


# // download pdf

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def download_pdf_view(request,pk):
    dischargeDetails = PatientDischarge.objects.all().filter(admitted=pk).order_by('-id')[:1]

    dict = {
        'assign_doctor': dischargeDetails[0].assign_doctor.doctor_name,
        'admitted': dischargeDetails[0].admitted.patient_name,
        'phone': dischargeDetails[0].admitted.phone,
        'address': dischargeDetails[0].admitted.address,
        'symptoms': dischargeDetails[0].admitted.symptoms,
        'release_date': dischargeDetails[0].release_date,
        'medicine_cost': dischargeDetails[0].medicine_cost,
        'other_charge': dischargeDetails[0].other_charge,
        'days_count': dischargeDetails[0].days_count,
        'room_bill':dischargeDetails[0].room_bill,
        'total_bill': dischargeDetails[0].total_bill,

    }
    print('dischargeDetails', dischargeDetails)
    return render_to_pdf('hospital/pdf_template.html',dict)

    # dischargeDetails = PatientDischarge.objects.all().filter(admitted=pk).order_by('-admitted_id')

    # context = {
    #     'discharge': dischargeDetails,
    # }

    # pdf = render_to_pdf('hospital/pdf_template.html', context)
    # if pdf:
    #     response = HttpResponse(pdf, content_type="application/pdf")
    #     content = "inline; filename=hospital/pdf_template.html"
    #     response['Content-Disposition'] = content
    #     return response

    # return HttpResponse("not found")   


# // patient appointment view
def patient_appointment_view(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_form = form.save(commit=False)

            appointment_form.patient_name = request.user
            appointment_form.save()
            subject = "Welcome to Unique Hospital"
            message = f"Hi {request.user.username}, Thanks for your appointment for {appointment_form.doctor.doctor_name}. We will confirm your order as soon as possible. Please check your mail after sometimes"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email, ]
            send_mail(subject, message, email_from, recipient_list)  
            return redirect('/')
        else:
            form = AppointmentForm()

    context = {
        'form': form,
    }            

    return render(request, 'hospital/patient_form.html', context)


def confirm_view(request, id):
    appointment_obj = Appointment.objects.get(id=id)
    form = AppointmentForm(instance=appointment_obj)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment_obj)
        if form.is_valid():
            form.save()
            if appointment_obj.is_appointment == True:
                subject = "Welcome to Unique Hospital"
                message = f"Hi {request.user.username}, Thanks for your appointment for {form.doctor.doctor_name}. We will confirm your order as soon as possible."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.user.email, ]
                send_mail(subject, message, email_from, recipient_list)  
            return redirect('/')
    context = {
        'appointment_obj': appointment_obj,
        'form': form,
    }

    return render(request, 'hospital/confirm_appointment.html', context)

