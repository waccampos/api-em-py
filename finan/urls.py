from django.urls import path
from . import views

urlpatterns = [
    path("venda/",views.vender,name="venda"),
    path("comprar/",views.comprar,name="comprar"),
    
]