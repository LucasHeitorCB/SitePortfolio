from django.contrib import admin
from django.urls import path
from portfolio import views  # 👈 Correto, sem ponto no início

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
    path('converse/', views.converse, name='converse'),
]
