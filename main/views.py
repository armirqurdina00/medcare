from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient

def home(request):
    patients = Patient.objects.all()
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
        return render(request, 'patient.html', {'patient': patient})
    else:
        messages.error(request, 'You must be logged in to view that page.')
        return redirect('home')