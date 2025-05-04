from django.shortcuts import render, redirect
from libraryapp.models import Livru
from libraryapp.forms import LivruForm
from django.contrib import messages

def lista_livru(request):
    livrus = Livru.objects.all()
    context = {
        'livrus': livrus
    }
    return render(request, 'lista_livru.html', context)

def add_livru(request):
    if request.method == "POST":
        form = LivruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success("Guarda Dados Susesu !")
            return redirect("lista-livru")
        else:
            print(form.errors)
    else:
        form = LivruForm()
        
    return render(request, "add_livru.html", {'form' : form})
