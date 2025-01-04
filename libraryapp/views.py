from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def dashboard(request):
    return render(request, 'dashboard.html')
