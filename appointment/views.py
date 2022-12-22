from django.shortcuts import render

from .models import PatientDetail

# Create your views here.

def dashboard(request):
    return render(request, 'appointment/available_health_workers.html')


def request_appointment(request):
    if request.method == 'POST':
        appointment = PatientDetail(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone_number=request.POST['phone'],
            emergency_contact_name=request.POST['emergency_full_name'],
            emergency_contact_phone_number=request.POST['emergency_phone'],
            symptoms=request.POST['desc'],
            # preferred_date=request.POST['date'],
            preferred_date_and_time=request.POST['time'],

        )

        appointment.save()

    return render(request, 'appointment/patient_details.html')

def pending_appointments(request):
    return render(request, 'appointment/pending_appointments.html')