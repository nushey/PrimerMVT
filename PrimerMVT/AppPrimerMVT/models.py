from codecs import charmap_build
from email import charset
from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30)
    edad = models.CharField(max_length=3)
    fecha_nacimiento = models.DateField()