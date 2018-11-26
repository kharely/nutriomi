from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

class Patient(models.Model):
    FEMALE = 'FE'
    MALE = 'MA'
    GENER = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    gener = models.CharField(max_length=2, choices=GENER, default=FEMALE,)
    name = models.CharField(max_length=50)
    birth_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    
    def years_old(self):
        age = date.today() - self.birth_date
        days_difference = age.days
        age_num = days_difference/365.2425
        age = int(age_num)
        return age
 

class Diet(models.Model):
     name = models.CharField(max_length=20)
     description = models.CharField(max_length=500)
     quantity_cal = models.FloatField(max_length=5)
     timestamp = models.DateTimeField(auto_now_add=True)   


class Statistics(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    weight = models.CharField(max_length=5)
    height = models.CharField(max_length=6)
    miffin = models.FloatField(max_length=5)
    harris = models.FloatField(max_length=5)
    valencia = models.FloatField(max_length=5)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def algorithm(self):
        w = float(self.weight)
        h = float(self.height)
        if self.patient.gener.MALE:
            self.harris = 66.473 + (13.7516 * w) + (5.0033 * h) - (6.755 * self.patient.years_old )
            self.miffin = (10 * w) + (6.25 * h) - (5 * self.patient.years_old) + 5 
            self.valencia = (13.37 * w + 747)
        else:
            self.harris = 655.0955 + (9.5634 * w) + (1.8495 * h) - (4.6756 * self.patient.years_old)
            self.miffin = (10 * w) + (6.25 * h) - (5 * self.patient.years_old) + 161
            self.valencia = (14.21 * w + 429)
        self.save()
# calorias (kgs) = dependiendo que quieres harris/miffin/valencia
# calorias / peso


