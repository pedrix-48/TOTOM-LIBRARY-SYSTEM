from django.shortcuts import render, redirect, get_object_or_404
from libraryapp.models import Livru, Author
from .forms_livru import LivruForm, EditInfoDetailLivru, EditSypnosisLivruForm
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
            messages.error(form.errors)
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
    authors = Author.objects.all()
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
        "livru" : livru,
        'authors': authors
    }
    return render(request, "edit_livru.html", context)

def detail_livru(request, titulu_livru):
    livru = Livru.objects.get(titulu_livru = titulu_livru)
    form = EditInfoDetailLivru()
    context = {
        "livru" : livru,
        "form" : form,
    }
    return render(request, "detail_livru.html", context)

def edit_cover_livru(request, titulu_livru):
    livru = get_object_or_404(Livru, titulu_livru=titulu_livru)
    if request.method == "POST" and "foto_livru" in request.FILES:
        livru.foto_livru = request.FILES['foto_livru'] 
        livru.save()
        messages.success(request, "Troka Cover Livru Susesu !")
        return redirect("det-livru", titulu_livru=titulu_livru)
    context = {"livru": livru}
    return render(request, "detail_livru.html", context)

def edit_info_livru(request, titulu_livru):
    livru = get_object_or_404(Livru, titulu_livru = titulu_livru)
    if request.method == "POST":
        form = EditInfoDetailLivru(request.POST, request.FILES ,instance = livru)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("det-livru", titulu_livru = livru.titulu_livru)
    else:
        form = EditInfoDetailLivru(instance = livru)
    context = {
        "livru" : livru,
        "form" : form
    }
    return render(request, "detail_livru.html", context)

def editSypnosisLivru(request, titulu_livru):
    livru = get_object_or_404(Livru, titulu_livru = titulu_livru)
    if request.method == "POST":
        form = EditSypnosisLivruForm(request.POST,  request.FILES, instance = livru)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("det-livru", titulu_livru = titulu_livru)
    else:
        form = EditSypnosisLivruForm(instance = livru)
    context = {
        "form" : form,
        "livru" : livru
    }
    return render(request, "detail_livru.html", context)
