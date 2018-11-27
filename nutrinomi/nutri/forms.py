from django import forms
from nutri.models import Patient, Statistics, Diet

class CalculateForm(forms.Form):
    carbohydrates = forms.FloatField(label='carbohydrates', required=True)
    protein = forms.FloatField(label='protein', max_value=7000, required=True)
    lipid = forms.FloatField(label='lipid', required=True)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['gener', 'name', 'birth_date', 'address', 'phone']


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistics
        fields = ['weight', 'height','diet']

class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['name','description','quantity_cal']
