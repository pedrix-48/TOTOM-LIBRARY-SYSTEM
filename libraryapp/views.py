from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.decorators import login_required 
from .forms import AdminLoginForm, AuthorForm
from .models import Author

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if form.is_valid():
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'loginpage.html')
    else:
        form = AdminLoginForm()
    context = {
        'form': form
    }
    return render(request, 'loginpage.html', context)

def admin_logout(request):
    logout(request)
    return render(request, 'logout.html')

# @login_required(login_url='login') # rai hela ba orsda ba hadia nia bug
def dashboard(request):
    return render(request, 'dashboard.html')

def lista_author(request):
    form = AuthorForm()
    authors = Author.objects.all()
    context = {
        'authors': authors,
        'form': form,
    }
    return render(request, 'author/lista_author.html', context)

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guarda Dados Susesu !')
            return redirect('lista-author')
        else:
            print(form.errors)
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'author/add_author.html', context)

def edit_author(request, id_author):
    author = Author.objects.get(id_author=id_author)
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guarda Dados Susesu !')
            return redirect('lista-author')
        else:
            print(form.errors)
    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/edit_author.html', context)

def delete_author(request, id_author):
    author = Author.objects.get(id_author=id_author)
    if request.method == 'POST':
        author.delete()
        return redirect('lista-author')
    
def profile_author(request,naran_author):
    author = Author.objects.get(naran_author=naran_author)
    context = {
        'author': author
    }
    return render(request, 'author/profile_author.html', context)

def edit_profile_photo(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST' and 'foto_profile' in request.FILES:
        author.foto_profile = request.FILES['foto_profile']
        author.save()
    return redirect('profile-author', id_author=author.id_author)

def edit_detalla_profile(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guarda Dados Susesu !')
            return redirect('profile-author', id_author=author.id_author)
    else:
        form = AuthorForm(instance=author)
    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/profile_author.html', context)

def edit_deskrisaun_profile(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST':
        author.deskrisaun = request.POST.get('deskrisaun')
        author.save()
        return redirect('profile-author', id_author=author.id_author)
    return redirect('profile_author', id_author=author.id_author)


