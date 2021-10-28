from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from hospital.models import Doctor, Appointment
from hospital.forms import DoctorForm, AppointmentForm
from .decorators import unauthenticated_user, admin_only, allowed_users, patient_only
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from django.conf import settings
from django.core.mail import send_mail


def sign_up_view(request):
    form = UserCreateForm(request.POST)
    if form.is_valid():
        user = form.save()
        current_site = get_current_site(request)
        mail_subject = "An Account was Created"
        message = render_to_string('account/send_mail.html', {
            'user': user,
            'domain': current_site.domain,

        })
        send_mail = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[send_mail])
        email.send()
        return redirect('log-in')

        messages.success(request, "Successfully Created Account")
    context = {
        'form': form,
    }
    return render(request, 'account/signup.html', context)


def log_in_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            context = {
                'form': form,
                'error': "Invalid Email or Password!!",
            }
            return render(request, 'account/login.html', context)

    context = {

    }
    return render(request, 'account/login.html', context)


def log_out_view(request):
    logout(request)
    return redirect('log-in')




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