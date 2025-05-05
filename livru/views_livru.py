from django.shortcuts import render, redirect
from libraryapp.models import Livru
from libraryapp.forms import LivruForm
from django.contrib import messages

def lista_livru(request):
    livrus = Livru.objects.all()
    form = LivruForm
    context = {
        'livrus': livrus,
        'form' : form,
    }
    return render(request, 'lista_livru.html', context)

def add_livru(request):
    if request.method == "POST":
        form = LivruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-livru")
        else:
            print(form.errors)
    else:
        form = LivruForm()
        
    return render(request, "add_livru.html", {'form' : form})

def delete_livru(request, id_livru):
    livru = Livru.objects.get(id_livru = id_livru)
    if request.method == "POST":
        livru.delete()
        return redirect("lista-livru")
    
def edit_livru(request, id_livru):
    livru = Livru.objects.get(id_livru = id_livru)
    form = LivruForm(instance = livru)
    if request.method == "POST":
        form = LivruForm(request.POST, instance = livru)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-livru")
        else:
            print(form.errors)
    context = {
        "form" : form,
        "livru" : livru
    }
    return render(request, "edit_livru.html", context)

def detail_livru(request, titulu_livru):
    livru = Livru.objects.get(titulu_livru = titulu_livru)
    context = {
        "livru" : livru
    }
    return render(request, "detail_livru.html", context)
