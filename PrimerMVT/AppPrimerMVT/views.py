from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

from AppPrimerMVT.models import Familiares
import datetime

def mi_familia(request):

    fecha_nacimiento1=datetime.datetime(1982, 2, 6)
    fecha_nacimiento2=datetime.datetime(1985, 4, 18)
    fecha_nacimiento3=datetime.datetime(2007, 5, 15)
    familiar_1 = Familiares(nombre="Fernando Zeballos", parentesco="padre", edad="40",fecha_nacimiento=datetime.datetime.strftime(fecha_nacimiento1, "%d/%m/%Y"))
    familiar_2 = Familiares(nombre="Giovanna Fagundez", parentesco="madre", edad="37",fecha_nacimiento=datetime.datetime.strftime(fecha_nacimiento2, "%d/%m/%Y"))
    familiar_3 = Familiares(nombre="Melany Zeballos", parentesco="hermana", edad="15",fecha_nacimiento=datetime.datetime.strftime(fecha_nacimiento3, "%d/%m/%Y"))
    contexto = {"familiar1": familiar_1, "familiar2": familiar_2, "familiar3": familiar_3}
    return render(request, "AppPrimerMVT/familia.html", contexto)
