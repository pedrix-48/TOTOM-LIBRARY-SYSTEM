from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    return render(request, 'loginpage.html')

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
