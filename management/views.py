from multiprocessing import context
from traceback import print_tb
from django.shortcuts import redirect, render
from management.models import Alloted_Beds, Department, Doctor, Donors, Medicine, Patient
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from management.forms import NewUserForm,CreateDoctorPofile
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

# To update user profile
@login_required(login_url=welcome_page)
def update_user_profile(request,pk):
    user = User.objects.get(id=pk)
    Doctor.objects.get_or_create(Doctor_user_instance=user)
    this = Doctor.objects.get(Doctor_user_instance=user)

    profile_form = CreateDoctorPofile(instance=this)
    user_form = NewUserForm(instance=request.user)
    if request.method == 'POST':
        profile_form = CreateDoctorPofile(request.POST,instance=this)
        if profile_form.is_valid():
            updated_profile = profile_form.save(commit=False)
            updated_profile.Doctor_user_instance = user
            updated_profile.save()     
            return redirect('profile_page')        
    context = {
            'profile_form':profile_form,
            # 'user_form':user_form,
        }

    return render(request,'management/Pages/test_page.html',context)

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
        'patient_data':patient_data,
        'checked_id':checked_in,
    }
    return render(request,'management/Pages/patients_details.html',context)

# This viiew is responsible for the logout functionality
def logout_user(request):
    logout(request)
    return redirect('login_page')