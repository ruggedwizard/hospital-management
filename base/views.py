from django.shortcuts import render
from management.models import Doctor,Appointment,Leave_message
from .forms import MakeAppointment
from .emails import send_email


# Create your views here.
def landing_page(request):
    forms = MakeAppointment()
    """ SAVE APPOINTMENT DATA TO DATABASE AND SEND EMAIL TO THE USER UPON COMPLETION"""
    if request.method == 'POST':
        fullname=request.POST['fullname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        reason_for_appointment = request.POST['reason-for-appointment']
        date_of_appointment = request.POST['date-of-appointment']
        _appointment = Appointment.objects.create(Fullname=fullname,Contact_email=email,Contact_phone=phone_number,Reason_for_Appointment=reason_for_appointment)
        """SENDING USER EMAIL USING SMTPLIB PYTHON"""
        
        """USING FORMS MODEL BUT INPUT CUSTOMIZATION FAILED"""
        # forms= MakeAppointment(request.POST)
        # if forms.is_valid():
        #     _data =forms.save()
        #     send_email(_data.Contact_email)

        # else:
        #     forms = MakeAppointment() 
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
    if request.method == 'POST':
        email = request.POST['email']
        message_for_doctor = request.POST['message']
        print(request.POST)
        Leave_message.objects.create(email=email,message_for_doctor=message_for_doctor)
    return render(request,'base/Pages/contact_page.html')

def blog_page(request):
    return render(request,'base/Pages/blog_page.html')