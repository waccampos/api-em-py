from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/',include('cadastro.urls')),
    path('login/',include('login.urls')),
    path('financeiro/',include('finan.urls')),
    path('gestao-estoque/',include('gestao_estoque.urls')),
    path('rh/',include('rh.urls')),
    path('ponto/',include('folhaponto.urls'))
]
