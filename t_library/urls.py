from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from libraryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginpage, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dash-admin'),

    path('livru/', include('livru.urls')),
    path('author/', include('libraryapp.urls')),
    path('staff/', include('staff.urls')),
    path('empresta/', include('empresta.urls')),
    path('estudante/', include('estundate.urls')),
    path('dep/', include('departamentu.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
