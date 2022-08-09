from django.contrib import admin
from management.models import Birth_report, Department,Doctor, Donors, Medicine, Nurse, Other_Staff,Patient,Room,Alloted_Beds,Appointment,Leave_message

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
admin.site.register(Birth_report)
admin.site.register(Appointment)
admin.site.register(Leave_message)

