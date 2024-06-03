from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    form = DestinosTuristicosForm()
    return render(request, 'añadir_destinos.html', {'form':form})

def editar_destinos(request, id):
    pass

def eliminar_destinos(request):
    pass