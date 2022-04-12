from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request,'management/Pages/dashboard_page.html')