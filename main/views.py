from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
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
        return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    return redirect('home')