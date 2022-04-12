from django.urls import path
from management import views
urlpatterns = [ 
    path('', views.welcome_page,name="login_page"),
    path('doctors/',views.doctors_page, name="doctors_page"),
    path('patients/',views.patient_page, name="patients_page"),
    path('financies/',views.financial_activities, name="financies_page"),
    path('medicines/',views.medicines, name="medicine_page"),
    path('donors/',views.donors_page, name="donors_page"),
    path('beds/',views.beds_page, name="beds_page"),
    path('reports/',views.reports_page, name="reports_page"),
    path('profile_page/',views.profile_page, name="profile_page"),


]