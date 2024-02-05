from django.db import models
from django.core.validators import RegexValidator

class Persona(models.Model):
  dni_regex = RegexValidator(regex=r'^\+?1?\d{8}', message = ("Debe de ingresar los 8 digitos de DNI"))
  
  nombres = models.CharField(max_length=100, null=True)
  apellidos = models.CharField(max_length=250, null=True)
  dni = models.CharField(validators=[dni_regex], max_length=8, unique=True)
  correo = models.EmailField(max_length=254, unique=True)
  
  def __str__(self):
    return f"{self.dni} - {self.apellidos}" 
  
class Sello(models.Model):
  
  nombre = models.CharField(max_length=150)
  logo = models.ImageField(upload_to='logo/')
  
  def __str__(self):
    return f"{self.nombre}"
	