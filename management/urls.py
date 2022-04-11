from django.urls import path
from management import views
urlpatterns = [ 
    path('', views.welcome_page,name="management_welcome_page"),
]