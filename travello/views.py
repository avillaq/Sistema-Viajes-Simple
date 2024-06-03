from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import DestinosTuristicos
from .forms import DestinosTuristicosForm
import os

# Create your views here.
def index(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'dests': dests})

def lista_destinos(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'lista_destinos.html', {'dests': dests})

def añadir_destinos(request):
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    form = DestinosTuristicosForm()
    return render(request, 'añadir_destinos.html', {'form':form})

def editar_destinos(request, id_destino):
    destino = DestinosTuristicos.objects.get(id=id_destino)
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    form = DestinosTuristicosForm(instance=destino)
    return render(request, 'editar_destinos.html', {'form':form})

def eliminar_destinos(request, id_destino):
    destino = DestinosTuristicos.objects.get(id=id_destino)
    img_url = destino.imagenCiudad.url
    
    destino.delete()
    os.remove('.'+img_url)
    return redirect('lista_destinos')
    