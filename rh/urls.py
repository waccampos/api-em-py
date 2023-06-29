from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-funcionarios/',views.cadastro_func,name='cadastro-funcionario')
]
