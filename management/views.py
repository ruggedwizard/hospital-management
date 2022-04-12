from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request,'management/Pages/login_page.html')

def doctors_page(request):
    return render(request,'management/Pages/doctors_page.html')

def patient_page(request):
    return render(request,'management/Pages/patient_page.html')

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