from django.urls import path
from . import views_staff as views
# from libraryapp.views import staff_login

urlpatterns = [
    # path('staff-login/', staff_login, name='staff-login'),
    path('list/', views.lista_staff, name='lista-staff'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('import-staff/', views.import_staff_xl, name='import-staff'),
    path('edit-staff/<str:id_staff>', views.edit_staff, name='edit-staff'),
    path('edit-password-staff/<str:id_staff>', views.EditPasswordStaff.as_view(), name='edit-password-staff'),
    path('del-staff/<str:id_staff>', views.del_staff, name='del-staff'),
    path('del-all-staff', views.del_all_staff, name='del-all-staff'),
    path('profile/<str:id_staff>', views.profile_staff, name='profile-staff'),
    path('edit-foto/<str:id_staff>/', views.edit_foto_staff, name='edit-foto-staff'),
    path('del-foto/<str:id_staff>/', views.del_foto_staff, name='del-foto-staff'),
]
