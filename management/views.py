from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return HttpResponse('<h1>Systems Welcome page</h1>')