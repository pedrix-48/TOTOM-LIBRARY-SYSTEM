from django.shortcuts import render
from libraryapp.models import Estudante

def lista_estudante(request):
    estudantes = Estudante.objects.all()
    return render(request, 'lista_estudante.html' ,{"estudantes" : estudantes})
