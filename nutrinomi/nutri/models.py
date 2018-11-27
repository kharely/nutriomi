from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
    

class Diet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    quantity_cal = models.FloatField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)   


class Statistics(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(max_length=5)
    height = models.FloatField(max_length=6)
    miffin = models.FloatField(validators=[
        MinValueValidator(0.0), MaxValueValidator(10000.0)], default=0.0)
    harris = models.FloatField(validators=[
        MinValueValidator(0.0), MaxValueValidator(10000.0)],default=0.0)
    valencia = models.FloatField(validators=[
        MinValueValidator(0.0), MaxValueValidator(10000.0)], default=0.0)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def years_old(self):
        age = self.timestamp - self.patient.birth_date
        days_difference = age.days
        age_num = days_difference/365.2425
        age = float(age_num)
        return age

    def algorithm(self):
        w = self.weight
        h = self.height
        if self.patient.gener == 'MA':
            harris = 66.473 + (13.7516 * w) + (5.0033 * h) - (6.755 * self.years_old())
            miffin = (10 * w) + (6.25 * h) - (5 * self.years_old()) + 5
            valencia = (13.37 * w) + 747
        else:
            harris = 655.0955 + (9.5634 * w) + (1.8495 * h) - (4.6756 * self.years_old())
            miffin = (10 * w) + (6.25 * h) - (5 * self.years_old()) + 161
            valencia = (14.21 * w) + 429
        self.harris = round(harris)
        self.miffin = round(miffin)
        self.valencia = round(valencia)
        self.save()
