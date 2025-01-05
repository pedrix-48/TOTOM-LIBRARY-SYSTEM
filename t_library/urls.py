
from django.contrib import admin
from django.urls import path
from libraryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('', views.loginpage, name = 'login'),
    path('logout', views.admin_logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dash-admin'),
    path('listalivru', views.lista_livru, name = 'lista-livru'),
    path('listauthor', views.lista_author, name = 'lista-author'),
    path('listastaff', views.lista_staff, name = 'lista-staff'),
    path('listaempresta', views.lista_empresta, name = 'lista-empresta'),
]
