from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Patient, Statistics, Diet
from .forms import PatientForm, StatisticForm

@login_required
def index(request):
    patients = Patient.objects.filter(user=request.user)
    context = {'patients': patients}
    return render(request, 'nutri/index.html', context)


@login_required
def nutrilogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('nutri:index'))


@login_required
def patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    statistics = Statistics.objects.filter(patient=patient)
    context = {'patient': patient, 'statistics': statistics}
    return render(request, 'nutri/profile.html', context)

@login_required
def add_statistic(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    diets = Diet.objects.all()
    form = None
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        print(form)
        if form.is_valid():
            stat = form.save(commit=False)
            stat.patient = patient
            stat.save()
            stat.algorithm()
            return HttpResponseRedirect(reverse('nutri:patient',
                                        args=(patient_id,)))
    context = {'patient': patient,'diets':diets ,'form': form}
    return render(request, 'nutri/statistic-form.html', context)


@login_required
def add_patient(request):
    form = None
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return HttpResponseRedirect(reverse('nutri:index'))
    context = {'form': form}
    return render(request, 'nutri/add-patient.html', context)
