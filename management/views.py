from django.shortcuts import redirect, render
from management.models import Alloted_Beds, Department, Doctor, Donors, Medicine, Patient
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome_page(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('departments_page')
    return render(request,'management/Pages/login_page.html')

@login_required(login_url=welcome_page)
def departments_page(request):
    departments = Department.objects.all()
    context ={
        'departments':departments
    }
    return render(request,'management/Pages/departments_page.html',context)

@login_required(login_url=welcome_page)
def doctors_page(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'management/Pages/doctors_page.html',context)

@login_required(login_url=welcome_page)
def patient_page(request):
    patients = Patient.objects.all()
    context = {
        'patients':patients
    }
    return render(request,'management/Pages/patient_page.html',context)

@login_required(login_url=welcome_page)
def financial_activities(request):
    return render(request,'management/Pages/financial_activities_page.html')

@login_required(login_url=welcome_page)
def medicines(request):
    medicines = Medicine.objects.all()
    context = {
        'medicines': medicines
    }
    return render(request,'management/Pages/medicine_page.html',context)

@login_required(login_url=welcome_page)
def donors_page(request):
    donors = Donors.objects.all()
    context = {
        'donors':donors
    }
    return render(request,'management/Pages/donor_page.html',context)

@login_required(login_url=welcome_page)
def beds_page(request):
    alloted_beds = Alloted_Beds.objects.all()
    context = {
        'alloted_beds':alloted_beds
    }
    return render(request,'management/Pages/beds_page.html',context)

@login_required(login_url=welcome_page)
def reports_page(request):
    return render(request,'management/Pages/reports_page.html')

# This view is responsible to get the current logged user profile data
@login_required(login_url=welcome_page)
def profile_page(request):
    profile_details = Doctor.objects.get(Doctor_user_instance=request.user)
    doctors_patient = Patient.objects.filter(Patient_doctor=profile_details)
    print(doctors_patient)
    context = {
        'doctors_patient':doctors_patient,
        'profile_details':profile_details
    }
    return render(request,'management/Pages/profile_page.html', context)

# This view is responsible to get the Doctors patients details
def patient_details_page(request,pk):
    patient_data = Patient.objects.get(id=pk)
    checked_in = Alloted_Beds.objects.get(Alloted_patient=patient_data)
    print(checked_in.Alloted_time)
    context = {
        'patient_data':patient_data
    }
    return render(request,'management/Pages/patients_details.html',context)

def logout_user(request):
    logout(request)
    return redirect('login_page')