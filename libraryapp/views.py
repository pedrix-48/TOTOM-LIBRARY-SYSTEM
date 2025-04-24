from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, logout, login # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import AdminLoginForm 
from .models import Livru, Author, Staff, Empresta 

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
                login(request, user)
                return redirect('dashboard')
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
    return render(request, 'logout.html')

# @login_required(login_url='login') # rai hela ba orsda ba hadia nia bug
def dashboard(request):
    return render(request, 'dashboard.html')

def lista_livru(request):
    livrus = Livru.objects.all()
    context = {
        'livrus': livrus
    }
    return render(request, 'lista_livru.html', context)

def lista_author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'lista_author.html', context)

def lista_staff(request):
    return render(request, 'lista_staff.html')

def lista_empresta(request):
    return render(request, 'lista_empresta.html')
