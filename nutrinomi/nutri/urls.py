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
]
