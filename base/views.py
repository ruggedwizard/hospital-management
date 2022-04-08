from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'base/Pages/login_page.html')