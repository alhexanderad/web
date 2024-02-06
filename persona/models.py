from django.db import models
from django.core.validators import RegexValidator
from autoslug import AutoSlugField
from django.urls import reverse
import datetime
import uuid

def generar_uuid_slug(instance, **kwargs):
  return str(uuid.uuid4())

def concatenar_cert_uuid(instance, **kwargs):
  return f"{instance.n_certificado}-{generar_uuid_slug(instance, **kwargs)}"

class Persona(models.Model):
  dni_regex = RegexValidator(regex=r'^\+?1?\d{8}', message = ("Debe de ingresar los 8 digitos de DNI"))
  
  nombres = models.CharField(max_length=100, null=True)
  apellidos = models.CharField(max_length=250, null=True)
  dni = models.CharField(validators=[dni_regex], max_length=8, unique=True)
  correo = models.EmailField(max_length=254, unique=True)
  curso= models.CharField(max_length=255, unique=True)
  n_certificado = models.CharField(verbose_name='N° Certificado', max_length=5, null=True)
  fecha_emision = models.DateField(verbose_name="Fecha de Emision", default=datetime.date.today, blank=True, null=True)
  slug = AutoSlugField(populate_from=concatenar_cert_uuid, unique=True, editable=False)
  
  
  def __str__(self):
    return f"{self.dni} - {self.apellidos}" 
  
  def get_absolute_url(self):
		# Define la URL absoluta para un objeto Certificado
    return reverse('persona:slug', kwargs={'slug': self.slug})
  
class Sello(models.Model):
  
  nombre = models.CharField(max_length=150)
  logo = models.ImageField(upload_to='logo/')
  
  def __str__(self):
    return f"{self.nombre}"
	