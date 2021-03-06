from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from management.models import Doctor, Nurse



class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class CreateDoctorPofile(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['Profile_image','Doctor_firstname','Doctor_lastname','Doctor_gender','Doctor_department','Doctor_specialization','Doctor_phone_number','Doctor_email_address','Doctor_location']
    
class CreateNurseProfile(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['Profile_image','Nurse_lastname','Nurse_firstname','Nurse_email_address','Nurse_phone_number','Nurse_location']