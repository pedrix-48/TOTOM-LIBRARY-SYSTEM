from django.shortcuts import redirect, render, get_object_or_404
from libraryapp.models import Estudante, Periodo
from django.contrib.auth.decorators import login_required 
from .forms_est import AddEstudanteForm, EditEstudanteForm
from django.contrib import messages

@login_required(login_url='login') 
def lista_estudante(request):
    estudantes = Estudante.objects.all()
    form = AddEstudanteForm()
    periodo = Periodo.objects.all()
    return render(request, 'lista_estudante.html' ,{"estudantes" : estudantes, "form": form, "periodo" : periodo})

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

def edit_estudante(request, nre):
    estudante = get_object_or_404(Estudante, nre = nre)
    form = EditEstudanteForm(instance = estudante)
    if request.method == "POST":
        form = EditEstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !!")
            return redirect('lista-estudante')
        else:
            messages.error(request, form.errors)
        
    return render(request, "edit_estudante.html", {"form" : form, "estudante" : estudante})

def delete_estudante(request, nre):
    if request.method == "POST":
        estudante = get_object_or_404(Estudante, nre=nre)
        estudante.delete()
        return redirect('lista-estudante')