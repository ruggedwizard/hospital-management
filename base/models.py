from django.db import models

# Create your models here.
class Departments(models.Model):
    Department_name = models.CharField(max_length=250, unique=True, blank=True, null=True)

    def __str__(self):
        return self.Department_name + "Department"

class Rooms(models.Model):
    Room_location = models.CharField(max_length=250, null=True,blank=True)

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
    Doctor_department = models.ForeignKey(Departments,on_delete=models.CASCADE, related_name="doctor_department")
    Doctor_specialization = models.CharField(max_length=250, null=True, blank=True)
    Doctor_phone_number = models.CharField(max_length=250, null=True, blank=True)
    Doctor_email_address = models.EmailField(default="firstname.lastname@hospitalmanagement.com", null=True, blank=True)
    Doctor_location = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.Doctor_firstname + self.Doctor_lastname + " Account Details"
    


class Patient(models.Model):
    Patient_lastname = models.CharField(max_length=250,null=True, blank=True)
    Patient_firstname = models.CharField(max_length=250,null=True, blank=True)
    Patient_phone_number = models.CharField(max_length=120, null=True, blank=True)
    Patient_address = models.CharField(max_length=350,null=True,blank=True)
    Patient_age = models.IntegerField(max_length=1000, null=True,blank=True)
    Patient_gender = models.CharField(max_length=25, choices=GENDER,default="UNDECIDED")
    Patient_room = models.ForeignKey(Rooms, on_delete=models.CharField, null=True, blank=True)

    def __str__(self):
        return self.Patient_lastname + self.Patient_firstname + "Details"

class Bills(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank= True)
    amount_paid = models.FloatField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name + self.amount_paid 

