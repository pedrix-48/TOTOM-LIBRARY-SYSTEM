
from django.contrib import admin
from django.urls import path
from django.conf import settings
from libraryapp import views
from livru import views_livru as livru
from staff import views_staff as staff
from empresta import views_empresta as empresta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name = 'login'),
    path('logout', views.admin_logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dash-admin'),
    path('listalivru', livru.lista_livru, name = 'lista-livru'),
    # path url ne ba module autor nian
    path('listauthor', views.lista_author, name = 'lista-author'),
    path('author/<str:id_author>/edit/', views.edit_author, name = 'edit-author'),

    path('add-author/', views.add_author, name='add-author'),
    path('listastaff', staff.lista_staff, name = 'lista-staff'),
    path('listaempresta', empresta.lista_empresta, name = 'lista-empresta'),
]

