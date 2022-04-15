from django.db import models

# Create your models here.
class Department(models.Model):
    Department_name = models.CharField(max_length=250, unique=True, blank=True, null=True)
    Department_details = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.Department_name + " Department"

class Room(models.Model):
    Room_location = models.CharField(max_length=250, null=True,blank=True)
    Room_ID = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Room_availability = models.BooleanField(default=True)

    def __str__(self):
        return "Located at :" + self.Room_location 

GENDER = (
        ('UNDECIDED','UNDECIDED'),
        ('MALE','MALE'),
        ('FEMALE','FEMALE')
    )

class Doctor(models.Model):
    Doctor_firstname = models.CharField(max_length=250, null=True,blank=True)
    Doctor_lastname = models.CharField(max_length=250, null=True,blank=True)
    Doctor_gender = models.CharField(max_length=25, choices=GENDER, default="UNDECIDED")
    Doctor_department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="doctor_department")
    Doctor_specialization = models.CharField(max_length=250, null=True, blank=True)
    Doctor_phone_number = models.CharField(max_length=250, null=True, blank=True)
    Doctor_email_address = models.EmailField(default="firstname.lastname@hospitalmanagement.com", null=True, blank=True)
    Doctor_location = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return "Dr. "+ self.Doctor_firstname+ " " + self.Doctor_lastname
    


class Patient(models.Model):
    Patient_id = models.CharField(unique=True, max_length=200, default="Please Update",null=True,blank=True)
    Patient_lastname = models.CharField(max_length=250,null=True, blank=True)
    Patient_firstname = models.CharField(max_length=250,null=True, blank=True)
    Patient_email_address = models.EmailField(max_length=250, null=True, blank=True, default="Null_provided@email.com")
    Patient_phone_number = models.CharField(max_length=120, null=True, blank=True)
    Patient_address = models.CharField(max_length=350,null=True,blank=True)
    Patient_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="patient_doctor")
    Patient_blood_group = models.CharField(max_length=200, default="Please Update")
    Patient_blood_genotype = models.CharField(max_length=200, default="Please Update")
    Patient_age = models.IntegerField(null=True,blank=True)
    Patient_gender = models.CharField(max_length=25, choices=GENDER,default="UNDECIDED")
    Patient_room = models.ForeignKey(Room, on_delete=models.CharField, null=True, blank=True)

    def __str__(self):
        return self.Patient_lastname +" " + self.Patient_firstname + " Details"

class Bill(models.Model):
    PAYMENT_STATUS = (
        ("PENDING","PENDING"),
        ("COMPLETED","COMPLETED"),
    )

    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank= True)
    amount_paid = models.FloatField(max_length=2000)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS, default="PENDING")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name.Patient_lastname + "PAYMENT STATUS IS " + self.payment_status

class Appointment(models.Model):
    Fullname = models.CharField(max_length=250)
    Contact_email = models.EmailField(max_length=500, default="notprovided@example.com", null=True, blank=True)
    Contact_phone = models.CharField(max_length=250)
    Appointment_date = models.DateTimeField()
    Reason_for_Appointment = models.TextField(max_length=2500)
    Appointment_completed = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ["Appointment_date"]

    def __str__(self):
        return self.Fullname + " Appointment"
    

class Alloted_Beds(models.Model):
    Bed_id = models.ForeignKey(Room,on_delete=models.CASCADE,null=True, blank=True) 
    Alloted_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Alloted_time = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    # Discharge_time = models.DateField(null=False, blank=True)

    def __str__(self):
        return self.Bed_id.Room_ID + " is Alloted to " + self.Alloted_patient.Patient_lastname + " " + self.Alloted_patient.Patient_firstname