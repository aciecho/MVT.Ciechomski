from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
import datetime
from AppFamilia.models import Familiar

# Create your views here.
def familiares():
    diaHoy = datetime.datetime.now()
    familiar = Familiar(nombre='Alberto', edad=66, nacimiento='1956-08-20')
    familiar.save()
    familiar2 = Familiar(nombre='Patricia', edad=63, nacimiento='1959-10-24')
    familiar2.save()
    familiar3 = Familiar(nombre='Sofia', edad=32, nacimiento='1990-05-25')
    familiar3.save()
    familiar4 = Familiar(nombre='Ana', edad=29, nacimiento='1993-06-08')
    familiar4.save()
    diccionario= {"dia":diaHoy, "nombre":familiar.nombre, "edad":familiar.edad, "nacimiento":familiar.nacimiento, "nombre2":familiar2.nombre,"edad2":familiar2.edad,"nacimiento2":familiar2.nacimiento, "nombre3":familiar3.nombre,"edad3":familiar3.edad,"nacimiento3":familiar3.nacimiento }
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)