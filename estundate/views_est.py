from django.shortcuts import render
from libraryapp.models import Estudante
from django.contrib.auth.decorators import login_required 

@login_required(login_url='login') 
def lista_estudante(request):
    estudantes = Estudante.objects.all()
    return render(request, 'lista_estudante.html' ,{"estudantes" : estudantes})
