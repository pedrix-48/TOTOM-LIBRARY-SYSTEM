from django.urls import path
from . import views_est as views

urlpatterns = [
    path('list/', views.lista_estudante, name='lista-estudante'),
    path('add-estudante/', views.add_estudante, name='add-estudante'),
    path('edit-estudante/<str:nre>', views.edit_estudante, name='edit-estudante'),
    path('del-estudante/<str:nre>', views.delete_estudante, name='del-estudante'),
]
