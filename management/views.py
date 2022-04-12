from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request,'management/Pages/login_page.html')

def doctors_page(request):
    return render(request,'management/Pages/doctors_page.html')

def patient_page(request):
    return render(request,'management/Pages/patient_page.html')