from dataclasses import fields
from management.models import Appointment
from django import forms

class MakeAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Fullname','Contact_email','Contact_phone','Appointment_date']