from django import forms
from nutri.models import Patient, Statistics

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['gener', 'name', 'birth_date', 'address', 'phone']


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistics
        fields = ['weight', 'height','diet']
