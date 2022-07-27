from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from base.models import Patient
from management.models import Alloted_Beds, Birth_report, Doctor, Donors, Medicine, Nurse


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

class AddMedicine(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class AddPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields= '__all__'

class AddDonor(forms.ModelForm):
    class Meta:
        model = Donors
        fields = '__all__'

class AddBirthReport(forms.ModelForm):
    class Meta:
        model = Birth_report
        fields = '__all__'

class AllotBed(forms.ModelForm):
    class Meta:
        model = Alloted_Beds
        fields = '__all__'