from django.urls import path
from . import views_empresta as views

urlpatterns = [
    path('list/', views.lista_empresta, name='lista-empresta'),
]
