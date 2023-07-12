from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=30)
    operario = models.CharField(max_length=30)
    email = models.EmailField()
    equipo = models.CharField(max_length=30)
    fecha = models.DateField()
    resultado = models.CharField(max_length=30)
    def __str__(self):
        return f"laboratorio: {self.laboratorio} - operario: {self.operario} - email: {self.email} - equipo: {self.equipo} - fecha: {self.fecha} - resultado: {self.resultado}"

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    institucion = models.CharField(max_length=30)
    informe = models.CharField(max_length=200)
    mamografia = models.CharField(max_length=30)
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email} - institucion: {self.institucion} - informe: {self.informe} - mamografia: {self.mamografia}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)