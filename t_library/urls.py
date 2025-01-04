
from django.contrib import admin
from django.urls import path
from libraryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('', views.loginpage, name = 'login'),
    path('dashboard', views.dashboard, name = 'dash-admin'),
]
