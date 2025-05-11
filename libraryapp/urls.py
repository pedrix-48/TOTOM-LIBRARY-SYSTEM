from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.lista_author, name='lista-author'),
    path('add/', views.add_author, name='add-author'),
    path('<str:id_author>/edit/', views.edit_author, name='edit-author'),
    path('<str:id_author>/delete/', views.delete_author, name='del-author'),
    path('del-all-author', views.del_all_author, name='del-all-author'),
    path('edit-photo/<str:naran_author>/', views.edit_profile_photo, name='edit-foto'),
    path('delete-photo/<str:naran_author>/', views.del_foto_profile_author, name='del-foto'),
    path('edit-detail/<str:naran_author>/', views.edit_detalla_profile, name='edit-detalla'),
    path('edit-deskripsi/<str:naran_author>/', views.edit_deskrisaun_profile, name='edit-desk'),
    path('profile/<str:naran_author>/', views.profile_author, name='profile-author'),
]
