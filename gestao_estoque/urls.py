from django.urls import path
from . import views

urlpatterns = [
    path("",views.quantidadeprod,name="quantidade-em-estoque"),
    path("cadastrar-produto/",views.cadastrar_produto,name="cadastrar-produto"),
    path("excluir-produto/",views.excluirprod,name="cadastrar-produto"),
    path("cadastrar-estoque/",views.estoque,name="estoque"),
    path("ver-estoque/",views.verestoque,name="estoque"),
    
    
]