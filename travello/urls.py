from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_destinos', views.lista_destinos, name='lista_destinos'),
    path('añadir_destinos', views.añadir_destinos, name='añadir_destinos')
]