from django.urls import path
from . import views_staff as views

urlpatterns = [
    path('list/', views.lista_staff, name='lista-staff'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('edit-staff/<str:id_staff>', views.edit_staff, name='edit-staff'),
    path('del-staff/<str:id_staff>', views.del_staff, name='del-staff'),
    path('del-all-staff', views.del_all_staff, name='del-all-staff'),
]
