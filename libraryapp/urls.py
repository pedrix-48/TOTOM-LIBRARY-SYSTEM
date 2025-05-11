from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.lista_author, name='lista-author'),
    path('add/', views.add_author, name='add-author'),
    path('<str:id_author>/edit/', views.edit_author, name='edit-author'),
    path('<str:id_author>/delete/', views.delete_author, name='del-author'),
    path('del-all-author', views.del_all_author, name='del-all-author'),
    path('edit-photo/<str:id_author>/', views.edit_profile_photo, name='edit-foto-author'),
    path('delete-photo/<str:id_author>/', views.del_foto_profile_author, name='del-foto-author'),
    path('edit-detail/<str:id_author>/', views.edit_detalla_profile, name='edit-detalla'),
    path('edit-deskripsi/<str:id_author>/', views.edit_deskrisaun_profile, name='edit-desk'),
    path('profile/<str:id_author>/', views.profile_author, name='profile-author'),
]
