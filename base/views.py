from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,'base/index.html')

def login_page(request):

    return render(request,'base/Pages/login_page.html')

def signup_page(request):

    return render(request,'base/Pages/signup_page.html')