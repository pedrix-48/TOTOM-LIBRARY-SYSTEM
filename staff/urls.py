from django.urls import path
from . import views_staff as views

urlpatterns = [
    path('list/', views.lista_staff, name='lista-staff'),
]
