from django.urls import path
from management import views
urlpatterns = [ 
    path('', views.welcome_page,name="login_page"),
    path('doctors/',views.doctors_page, name="doctors_page"),
    path('patients/',views.patient_page, name="patients_page"),

]