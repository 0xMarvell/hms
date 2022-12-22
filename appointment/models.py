from django.db import models

# Create your models here.

class PatientDetail(models.Model):
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.IntegerField(unique=True,blank=False)
    emergency_contact_name = models.CharField(max_length=80,blank=False)
    emergency_contact_phone_number = models.IntegerField(blank=False)
    symptoms = models.TextField(max_length=500,blank=True)
    preferred_date_and_time = models.CharField(max_length=20,blank=False)
    diagnosis = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name 
