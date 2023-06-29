from django.urls import path
from . import views

urlpatterns = [
    path("chegada/",views.folhapontochegada,name="ponto"),
    path("saida/",views.folhapontosaida,name="ponto"),
]