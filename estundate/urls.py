from django.urls import path
from . import views_est as views

urlpatterns = [
    path('list/', views.lista_estudante, name='lista-estudante'),
    path('add-estudante/', views.add_estudante, name='add-estudante'),
    path('import-estudante/', views.import_est_xl, name='import-est'),
    path('edit-estudante/<str:nre>', views.edit_estudante, name='edit-estudante'),
    path('del-estudante/<str:nre>', views.delete_estudante, name='del-estudante'),
    path('del-all-estudante', views.del_all_estudante, name='del-all-estudante'),
]
