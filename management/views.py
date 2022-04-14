from django.shortcuts import render
from management.models import Department, Doctor, Patient
# Create your views here.
def welcome_page(request):
    return render(request,'management/Pages/login_page.html')

def departments_page(request):
    departments = Department.objects.all()
    context ={
        'departments':departments
    }
    return render(request,'management/Pages/departments_page.html',context)

def doctors_page(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'management/Pages/doctors_page.html',context)

def patient_page(request):
    patients = Patient.objects.all()
    context = {
        'patients':patients
    }
    return render(request,'management/Pages/patient_page.html',context)

def financial_activities(request):
    return render(request,'management/Pages/financial_activities_page.html')

def medicines(request):
    return render(request,'management/Pages/medicine_page.html')

def donors_page(request):
    return render(request,'management/Pages/donor_page.html')

def beds_page(request):
    return render(request,'management/Pages/beds_page.html')

def reports_page(request):
    return render(request,'management/Pages/reports_page.html')

def profile_page(request):
    return render(request,'management/Pages/profile_page.html')