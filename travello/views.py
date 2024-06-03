from django.shortcuts import render
from django.http import HttpResponse
from .models import DestinosTuristicos

# Create your views here.
def index(request):
    dests = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'dests': dests})
