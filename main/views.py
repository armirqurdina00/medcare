from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
from .forms import AddPatientForm, RegisterForm

def home(request):
    patients = Patient.objects.filter(user=request.user.id)
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in. Welcome!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong credentials. Invalid username or password.')
            return redirect('home')
    else:    
        return render(request, "home.html", {'patients': patients})

def logout_user(request):
    logout(request)
    return redirect('home')

def patient_record(request, pk):
    if request.user.is_authenticated:
        patient = Patient.objects.get(id=pk)
        if request.user == patient.user:
            return render(request, 'patient.html', {'patient': patient})
        else:
            messages.error(request, "You can't access that page.")
            return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view that page.')
        return redirect('home')

def delete_patient(request, pk):
    if request.user.is_authenticated:
        patient = Patient.objects.get(id=pk)
        if request.user == patient.user:
            patient.delete()
            messages.success(request, 'Patient deleted successfully!')
            return redirect('home')
        else:
            messages.error(request, "You don't have permission to do that.")
            return redirect('home')
    else:
        messages.error('You must be logged in to do that.')
        return redirect('home')
    
def add_patient(request):
    form = AddPatientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                final_form = form.save(commit=False)
                final_form.user = request.user
                final_form.save()
                messages.success(request, "Patient added successfully.")
                return redirect('home')
        return render(request, "add_patient.html", {'form': form})
    else:
        messages.error(request, "You must be logged in!")
        return redirect('home')
    
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, "register.html", {'form': form})
    
    return render(request, "register.html", {'form': form})

def edit_patient(request, pk):
    if request.user.is_authenticated:
        current_patient = Patient.objects.get(id=pk)
        if request.user == current_patient.user:
            form = AddPatientForm(request.POST or None, instance=current_patient)
            if form.is_valid():
                form.save()
                messages.success(request, "Patient has been updated!")
                return redirect('home')
            return render(request, 'edit_patient.html', {'form': form})
        else:
            messages.error(request, "You can't access that page!")
            return redirect('home')
    else:
        messages.error(request, "You must be logged in!")
        return redirect('home')