from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'appointment/available_health_workers.html')


def request_appointment(request):
    return render(request, 'appointment/patient_details.html')

def pending_appointments(request):
    return render(request, 'appointment/pending_appointments.html')