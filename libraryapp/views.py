from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AdminLoginForm 

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if form.is_valid():
            if user is not None:
                return render(request, 'dashboard.html')
            else:
                return render(request, 'loginpage.html')
    else:
        form = AdminLoginForm()
    context = {
        'form': form
    }
    return render(request, 'loginpage.html', context)

def admin_logout(request):
    logout(request)
    return render(request, 'loginpage.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def lista_livru(request):
    return render(request, 'lista_livru.html')

def lista_author(request):
    return render(request, 'lista_author.html')

def lista_staff(request):
    return render(request, 'lista_staff.html')

def lista_empresta(request):
    return render(request, 'lista_empresta.html')
