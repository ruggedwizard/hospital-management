from django.urls import path
from base import views
urlpatterns = [
    path('login-page/',views.login_page, name="login_page"),
    path('meet-our-doctors/',views.doctor_page, name="doctor_page"),
    path('departments/',views.department_page, name="department_page"),
    path('health-tips/',views.blog_page, name="blog_page"),
    path('about/',views.about_page, name="about_page"),
    path('contact_us/',views.contact_us_page, name="conatct_us_page"),
    path('',views.landing_page,name="home_page"),
]