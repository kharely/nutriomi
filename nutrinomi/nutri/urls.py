from django.urls import path

from . import views

app_name = 'nutri'
urlpatterns = [
    path('',views.index, name='index'),
    path('paciente/<int:patient_id>/profile', views.patient, name='patient'),
    path('agregar/paciente', views.add_patient, name='add_patient'),
    path('paciente/<int:patient_id>/consulta', views.add_statistic, 
       name='add_statistic'),
    path('logout', views.nutrilogout, name='nlogout'),
    path('paciente/<int:patient_id>/cal', views.cal, name='cal'),
    path('cal/<int:stat_id>/per/weight', views.stat, name='cal_per_w'),
    path('diets', views.all_diets, name='diets'),
    path('diet/<int:diet_id>', views.diet, name='diet'),
    path('diet/add', views.diet_form, name='diet_form'),
]
