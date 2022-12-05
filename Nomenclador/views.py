from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def get_region(request):
    regiones = list(Region.objects.values())

    if len(regiones) > 0:
        data = {'message': 'Success', 'regiones': regiones}
    else:
        data = {'message': 'Not Found'}

    return JsonResponse(data)


def get_provincias(request, region_id):
    provincias = list(Provincia.objects.filter(region_id=region_id).values())

    if len(provincias) > 0:
        data = {'message': 'Success', 'provincias': provincias}
    else:
        data = {'message': 'Not Found'}

    return JsonResponse(data)


def get_municipios(request, provincia_id):
    municipios = list(Municipio.objects.filter(provincia_id=provincia_id).values())

    if len(municipios) > 0:
        data = {'message': 'Success', 'municipios': municipios}
    else:
        data = {'message': 'Not Found'}

    return JsonResponse(data)


def home(request):
    return render(request, 'index.html', status=200)
