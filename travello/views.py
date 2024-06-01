from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'


    return render(request, 'index.html', {'dest1': dest1})
