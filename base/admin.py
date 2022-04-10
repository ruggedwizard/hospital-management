from django.contrib import admin
from base.models import Doctor,Patient,Bill,Room,Department,Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Bill)
admin.site.register(Appointment)