from django.shortcuts import render
from django.http import HttpResponse

# For developement purposes, a file with fake data
# a list with dictionaries, projects
projects = [
    {
        'name':
        'EDS La Estrella',
        'contractor':
        'HL Ingenieros',
        'date_start':
        'Diciembre 30, 2018',
        'date_finish':
        'Enero 15, 2019',
        'scope':
        'Desmonte de fascias canopy y aviso Esso. Instalación fascia, totem y aviso precios. Construccion cimentación'
    },
    {
        'name':
        'EDS Aurora',
        'contractor':
        'Rótulos y Montajes',
        'date_start':
        'Diciembre 30, 2018',
        'date_finish':
        'Enero 15, 2019',
        'scope':
        'Desmonte de fascias canopy y aviso Esso. Instalación fascia, totem y aviso precios. Construccion cimentación'
    },
    {
        'name':
        'EDS Copacabana',
        'contractor':
        'PMP Avisos',
        'date_start':
        'Diciembre 30, 2018',
        'date_finish':
        'Enero 15, 2019',
        'scope':
        'Desmonte de fascias canopy y aviso Esso. Instalación fascia, totem y aviso precios. Construccion cimentación'
    },
]


# Create your views here.
def home(request):
    content = {'projects': projects}
    return render(request, 'projects/home.html', content)


def about(request):
    return render(request, 'projects/about.html')
