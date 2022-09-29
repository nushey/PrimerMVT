from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

from AppPrimerMVT.models import Familiares
import datetime

def mi_familia(request):

    familiar_1 = Familiares(nombre="Cecilia Zeballos", parentesco="Tía", edad="53",fecha_nacimiento=datetime.datetime(1969, 9, 22))
    contexto = {"familiar1": familiar_1}
    return render(request, "AppPrimerMVT/familia.html", contexto)
