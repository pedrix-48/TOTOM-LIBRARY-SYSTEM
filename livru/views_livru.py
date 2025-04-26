from django.shortcuts import render
from libraryapp.models import Livru

def lista_livru(request):
    livrus = Livru.objects.all()
    context = {
        'livrus': livrus
    }
    return render(request, 'lista_livru.html', context)
