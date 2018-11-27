from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Patient, Statistics, Diet
from .forms import PatientForm, StatisticForm, DietForm, CalculateForm

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
    statistics = Statistics.objects.filter(patient=patient).order_by("-timestamp")
    context = {'patient': patient, 'statistics': statistics, 
              }
    return render(request, 'nutri/profile.html', context)


@login_required
def cal(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    statistics = Statistics.objects.filter(patient=patient).order_by("-timestamp")
    context = {'patient':patient, 'statistics':statistics}
    return render(request, 'nutri/cal.html', context)


@login_required
def stat(request, stat_id):
    stat = get_object_or_404(Statistics, pk=stat_id)
    miffin = stat.miffin/stat.weight
    harris = stat.harris/stat.weight
    valencia = stat.valencia/stat.weight
    context = {'stat': stat, 'miffin': miffin, 'harris': harris, 'valencia': valencia}
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            carbohydrates = form.cleaned_data['carbohydrates']
            carb_m = (miffin/carbohydrates)/4
            carb_h = (harris/carbohydrates)/4
            carb_v = (valencia/carbohydrates)/4
            protein = form.cleaned_data['protein']
            pro_m = (miffin/protein)/4
            pro_h = (harris/protein)/4
            pro_v = (valencia/protein)/4
            lipid = form.cleaned_data['lipid']
            lip_m = (miffin/lipid)/9
            lip_h = (harris/lipid)/9
            lip_v = (valencia/lipid)/9
            context = {'stat':stat, 'miffin':miffin, 'harris':harris, 'valencia':valencia,
                       'carb_m': carb_m, 'carb_h': carb_h,'carb_v':carb_v,
                       'pro_m': pro_m, 'pro_h': pro_h, 'pro_v': pro_v,
                       'lip_m': lip_m, 'lip_h': lip_h, 'lip_v':lip_v,}
    return render(request, 'nutri/calories-per-weight.html', context)


@login_required
def diet(request, diet_id):
    diet = get_object_or_404(Diet, pk=diet_id)
    context = {'diet': diet}
    return render(request, 'nutri/diet.html', context)


@login_required
def all_diets(request):
    diets = Diet.objects.all()
    return render(request, 'nutri/all-diets.html', {'diets':diets})


@login_required
def diet_form(request):
    form = None
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('nutri:diets'))
    context = {'form': form}
    return render(request, 'nutri/diet-form.html', context)


@login_required
def add_statistic(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    diets = Diet.objects.all()
    form = None
    if request.method == 'POST':
        form = StatisticForm(request.POST)
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
