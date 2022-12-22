from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from appointment.views import dashboard
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(dashboard)
        else:
           return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect'}) 
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        # user has entered info and wants to create account
        if request.POST['password1'] == request.POST['password2']:
            patient = request.POST['acct_type'] == 'patient'
            health_worker = request.POST['acct_type'] == 'health-worker'
            user = User.objects_custom.create_user(
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                phone_number=request.POST['phone'],
                password=request.POST['password1'],
                is_patient=patient,
                is_health_worker=health_worker
            )   
            return redirect(login)
                
        else:
            return HTTPResponse({'error':'Passwords do not match. Please retype your password'})
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect(login)
