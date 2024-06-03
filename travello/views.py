from django.shortcuts import render
from django.http import HttpResponse
from .models import DestinosTuristicos
from .forms import DestinosTuristicosForm

# Create your views here.
def index(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'dests': dests})

def lista_destinos(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'lista_destinos.html', {'dests': dests})

def añadir_destinos(request):
    form = DestinosTuristicosForm()
    return render(request, 'añadir_destinos.html', {'form':form})