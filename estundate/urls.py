from django.urls import path
from . import views_est as views

urlpatterns = [
    path('list/', views.lista_estudante, name='lista-estudante'),
]
