from multiprocessing import context
from django.shortcuts import redirect, render
from management.models import Alloted_Beds, Birth_report, Department, Doctor, Donors, Medicine, Nurse, Patient
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from management.forms import NewUserForm,CreateDoctorPofile, CreateNurseProfile, AddPatient
from django.contrib.auth.models import User



#This view is responsible for loging the user into the management system 
def welcome_page(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('departments_page')
    return render(request,'management/Pages/login_page.html')

# This view is responsible for creating a new user instance
def sign_up_page(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('update_user_profile') 
    form = NewUserForm()   
    context = {
        'form':form
    }
    return render(request,'management/Pages/signup_page.html',context)

# To update Doctor profile
@login_required(login_url=welcome_page)
def update_user_profile(request,pk):
    user = User.objects.get(id=pk)
    Doctor.objects.get_or_create(Doctor_user_instance=user)
    this = Doctor.objects.get(Doctor_user_instance=user)
    profile_form = CreateDoctorPofile(instance=this)
    if request.method == 'POST':
        profile_form = CreateDoctorPofile(request.POST,instance=this)
        if profile_form.is_valid():
            updated_profile = profile_form.save(commit=False)
            updated_profile.Doctor_user_instance = user
            updated_profile.save()     
            return redirect('profile_page')  

    context = {
            'profile_form':profile_form,  
        }

    return render(request,'management/Pages/test_page.html',context)
# To update Nurse profile page
@login_required(login_url=welcome_page)
def update_nurse_profile(request,pk):
    user = User.objects.get(id=pk)
    Nurse.objects.get_or_create(Nurse_user_instance=user)
    that = Nurse.objects.get(Nurse_user_instance=user)
    user_form = CreateNurseProfile(instance=that)

    if request.method == 'POST':
        profile_form = CreateNurseProfile(request.POST,instance=that)
        if profile_form.is_valid():
            updated_profile = profile_form.save(commit=False)
            updated_profile.Nurse_user_instance = user
            updated_profile.save()     
            return redirect('nurse_profile')  
    context = {
        'user_form':user_form
    }
    return render(request,'management/Pages/update_nurse_profile.html', context)

# Add Patient To the Database by a current User
def add_patient(request):
    patient_form = AddPatient()

    context ={
        'patient_form':patient_form
    }
    return render(request,'management/Pages/add_patient.html',context)

# This view is responsibe for nurse profile
@login_required(login_url=welcome_page)
def nurse_profile(request):
    profile_details = Nurse.objects.get(Nurse_user_instance=request.user)
    context ={
        'profile_details':profile_details
    }
    return render(request,'management/Pages/nurse_profile_page.html',context)

# THis will display a list of all Departments
@login_required(login_url=welcome_page)
def departments_page(request):
    departments = Department.objects.all()
    context ={
        'departments':departments
    }
    return render(request,'management/Pages/departments_page.html',context)
# This will return a list of all the doctors 
@login_required(login_url=welcome_page)
def doctors_page(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'management/Pages/doctors_page.html',context)

# This will list all the patient from the database
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

# This will return a list of all medicine the pharmacy has
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
    birth_reports =Birth_report.objects.all()
    context = {
        'birth_reports':birth_reports
    }
    return render(request,'management/Pages/reports_page.html',context)

# This view is responsible to get the current logged user Doctors profile data
@login_required(login_url=welcome_page)
def profile_page(request):
    profile_details = Doctor.objects.get(Doctor_user_instance=request.user)
    doctors_patient = Patient.objects.filter(Patient_doctor=profile_details)
    print(profile_details.Profile_image.url)
    context = {
        'doctors_patient':doctors_patient,
        'profile_details':profile_details
    }
    return render(request,'management/Pages/profile_page.html', context)

# This view is responsible to get the Doctors patients details
@login_required(login_url=welcome_page)
def patient_details_page(request,pk):
    patient_data = Patient.objects.get(id=pk)
    checked_in = Alloted_Beds.objects.get(Alloted_patient=patient_data)
    print(checked_in.Alloted_time)
    context = {
        'patient_data':patient_data,
        'checked_id':checked_in,
    }
    return render(request,'management/Pages/patients_details.html',context)

# This viiew is responsible for the logout functionality
def logout_user(request):
    logout(request)
    return redirect('login_page')