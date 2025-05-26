from django.shortcuts import redirect, render
from libraryapp.models import Estudante
from django.contrib.auth.decorators import login_required 
from .forms_est import AddEstudanteForm
from django.contrib import messages

@login_required(login_url='login') 
def lista_estudante(request):
    estudantes = Estudante.objects.all()
    form = AddEstudanteForm()
    return render(request, 'lista_estudante.html' ,{"estudantes" : estudantes, "form": form})

def add_estudante(request):
    if request.method == "POST":
        form = AddEstudanteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !!")
            return redirect('lista-estudante')
    else:
        form = AddEstudanteForm()
    return render(request, 'add_estudante.html', {"form": form})

def edit_estudante(request, pk):
    pass