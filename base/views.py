from django.shortcuts import render
from management.models import Doctor,Appointment
from base.forms import MakeAppointment


# Create your views here.
def landing_page(request):
    forms = MakeAppointment()
    if request.method == 'POST':
        fullname=request.POST['fullname']
        email=request.POST['contact_email']
        date_of_appointment = request.POST['date_of_appointment']
        reason_for_appointment = request.POST['reason_for_appointment']
        contact_phone = request.POST['phone_number']
        appointment = Appointment.objects.create(Fullname=fullname,Contact_email=email,Contact_phone=contact_phone,Reason_for_Appointment=reason_for_appointment,Appointment_date=date_of_appointment)
        appointment.save()
    context = {
        'forms':forms
    }
    return render(request,'base/Pages/landing_page.html',context)

def login_page(request):

    return render(request,'base/Pages/login_page.html')

def signup_page(request):

    return render(request,'base/Pages/signup_page.html')

def doctor_page(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'base/Pages/doctors_page.html',context)

def department_page(request):
    return render(request,'base/Pages/department_page.html')

def about_page(request):
    return render(request,'base/Pages/about_page.html')

def contact_us_page(request):
    return render(request,'base/Pages/contact_page.html')

def blog_page(request):
    return render(request,'base/Pages/blog_page.html')