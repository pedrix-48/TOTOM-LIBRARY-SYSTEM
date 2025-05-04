
from django.contrib import admin
from django.urls import path
from django.conf import settings
from libraryapp import views
from livru import views_livru as livru
from staff import views_staff as staff
from empresta import views_empresta as empresta
from estundate import views_est as estudante
from departamentu import views_dep as dep
from libraryapp import views as author
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name = 'login'),
    path('logout', views.admin_logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dash-admin'),
    path('listalivru', livru.lista_livru, name = 'lista-livru'),
    #------------------------------------------------------------------
    # path url ne ba module autor nian
    path('listauthor', views.lista_author, name = 'lista-author'),
    path('add-author/', views.add_author, name='add-author'),
    path('author/<str:id_author>/edit/', views.edit_author, name = 'edit-author'),
    path('author/<str:id_author>/delete/', views.delete_author, name = 'del-author'),
    path('author/edit-photo/<str:id_author>/', views.edit_profile_photo, name='edit-foto'),
    path('author/edit-detalla/<str:id_author>/', views.edit_detalla_profile, name='edit-detalla'),
    path('author/edit-deskrisaun/<str:id_author>/', views.edit_deskrisaun_profile, name='edit-desk'),
    path('author/profile-author/<str:naran_author>/', author.profile_author, name='profile-author'),

    path('listastaff', staff.lista_staff, name = 'lista-staff'),
    path('listaempresta', empresta.lista_empresta, name = 'lista-empresta'),

    path('listestu', estudante.lista_estudante, name = 'lista-estudante'),

    
    path('dep', dep.lista_dep, name = 'lista-dep'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
