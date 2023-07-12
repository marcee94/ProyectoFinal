from django.urls import path
from Oncoliq.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', loginWeb),
    path('inicio/', inicio),
    path('laboratorio/', laboratorio, name="Laboratorio"),
    path('medico/', medico, name="Medico"),
    path('paciente/', paciente, name="Paciente"),
    path('setLaboratorio/', setLaboratorio, name="setLaboratorio"),
    path('getLaboratorio/', getLaboratorio, name="getLaboratorio"),
    path('buscarLaboratorio/', buscarLaboratorio, name="buscarLaboratorio"),
    path('setMedico/', setMedico, name="setMedico"),
    path('getMedico/', getMedico, name="getMedico"),
    path('buscarMedico/', buscarMedico, name="buscarMedico"),
    path('setPaciente/', setPaciente, name="setPaciente"),
    path('getPaciente/', getPaciente, name="getPaciente"),
    path('buscarPaciente/', buscarPaciente, name="buscarPaciente"),
    path('eliminarLaboratorio/<nombre_laboratorio>', eliminarLaboratorio, name="eliminarLaboratorio"),
    path('editarLaboratorio/<nombre_laboratorio>', editarLaboratorio, name="editarLaboratorio"),
    path('eliminarMedico/<nombre_medico>', eliminarMedico, name="eliminarMedico"),
    path('editarMedico/<nombre_medico>', editarMedico, name="editarMedico"),
    path('eliminarPaciente/<nombre_paciente>', eliminarPaciente, name="eliminarPaciente"),
    path('editarPaciente/<nombre_paciente>', editarPaciente, name="editarPaciente"),
    path('login/', loginWeb, name="login"),
    path('registro/', registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name = 'Oncoliq/login.html'), name="logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),
]