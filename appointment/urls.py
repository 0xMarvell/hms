from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('request-appointment', views.request_appointment, name='request-appointment'),
    path('pending-appointments', views.pending_appointments, name='pending-appointments'),
]