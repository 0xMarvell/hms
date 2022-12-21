from django.urls import path
from . import views

urlpatterns = [
    path('patient-records', views.view_patient_records, name='patient-records'),
    path('filter-records', views.filter_patient_records, name='filter-records'),
    # path('pending-appointments', views.pending_appointments, name='pending-appointments'),
]