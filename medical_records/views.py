from django.shortcuts import render

# Create your views here.

def view_patient_records(request):
    return render(request, 'medical_records/patient_records.html')


def filter_patient_records(request):
    return render(request, 'medical_records/filter_patient_records.html')