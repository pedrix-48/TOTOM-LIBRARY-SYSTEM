from django.shortcuts import render

def lista_estudante(request):
    return render(request, 'lista_estudante.html')
