from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,'base/Pages/landing_page.html')

def login_page(request):

    return render(request,'base/Pages/login_page.html')

def signup_page(request):

    return render(request,'base/Pages/signup_page.html')

def doctor_page(request):
    return render(request,'base/Pages/doctors_page.html')

def department_page(request):
    return render(request,'base/Pages/department_page.html')

def about_page(request):
    return render(request,'base/Pages/about_page.html')

def contact_us_page(request):
    return render(request,'base/Pages/contact_page.html')

def blog_page(request):
    return render(request,'base/Pages/blog_page.html')