from django.contrib import admin
from management.models import Department,Doctor, Donors, Medicine, Nurse, Other_Staff,Patient,Room,Alloted_Beds

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Alloted_Beds)
admin.site.register(Medicine)
admin.site.register(Other_Staff )
admin.site.register(Nurse )
admin.site.register(Donors)
