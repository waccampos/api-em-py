from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.login, name='login'),
    path('funcionario/', views.login, name='login'),
    path('usuario/esqueci-a-senha/', views.esquecisenha, name='esquecisenha'),
]