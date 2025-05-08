from django.urls import path
from . import views_dep as views

urlpatterns = [
    path('', views.lista_dep, name='lista-dep'),
]
