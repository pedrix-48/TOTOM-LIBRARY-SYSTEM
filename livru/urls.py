from django.urls import path
from . import views_livru as views

urlpatterns = [
    path('list/', views.lista_livru, name='lista-livru'),
    path('add/', views.add_livru, name='add-livru'),
    path('<int:id_livru>/delete/', views.delete_livru, name='del-livru'),
    path('<str:id_livru>/edit/', views.edit_livru, name='edit-livru'),
    path('detail/<str:titulu_livru>/', views.detail_livru, name='det-livru'),
    path('edit-cover/<str:titulu_livru>/', views.edit_cover_livru, name='edit-cover'),
    path('edit-info/<str:titulu_livru>/', views.edit_info_livru, name='edit-info'),
    path('edit-sypnosis/<str:titulu_livru>/', views.editSypnosisLivru, name='edit-syp'),
]
