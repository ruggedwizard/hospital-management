from django.urls import path
from base import views
urlpatterns = [
    path('login-page/',views.login_page, name="login_page"),
    path('',views.landing_page,name="home_page"),
]