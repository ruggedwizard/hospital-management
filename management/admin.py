from django.contrib import admin
from management.models import Department,Doctor,Patient,Room,Alloted_Beds

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Alloted_Beds)
