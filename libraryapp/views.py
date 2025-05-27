from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LoginView
from .forms import AdminLoginForm, AuthorForm, AuthorDetallaForm, EditAuthorDeskrisaunForm
from staff.forms_staff import LoginUserForm
from .models import Author, Livru

def homepage(request):
    livrus = Livru.objects.all()[:3]
    context = {
        "livrus" : livrus
    }
    return render(request, 'homepage.html', context)

def load_livru_hotu(request):
    livrus = Livru.objects.all()
    return render(request, "all_livru.html", {"livrus" : livrus})

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
                messages.error(request,"Username Ou Password Sei Sala !!")
    else:
        form = AdminLoginForm()
    context = {
        'form': form
    }
    return render(request, 'loginpage.html', context)

class StaffLoginView(LoginView): # HAU LAHATENE TAMBA SA MAK CLASS NEE BELE DIAK, SO MAROMAK MK HATENE :()
    form_class = LoginUserForm
    authentication_form = LoginUserForm
    template_name = 'loginpage.html'
    
    def form_valid(self,form):
        user = form.get_user()
        if user.is_staff:
            return super().form_valid(form)
        else:
            messages.error(self.request, "Ita La Autoriza Atu Asesu !")
            return redirect('login')
    
    def get_success_url(self):
        return super().get_success_url()
    

def admin_logout(request):
    logout(request)
    return render(request, 'logout.html')

@login_required(login_url='login') 
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login') 
def lista_author(request):
    form = AuthorForm()
    authors = Author.objects.all()
    context = {
        'authors': authors,
        'form': form,
    }
    return render(request, 'author/lista_author.html', context)


@login_required(login_url='login') 
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

@login_required(login_url='login') 
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

@login_required(login_url='login') 
def delete_author(request, id_author):
    author = Author.objects.get(id_author=id_author)
    if request.method == 'POST':
        author.delete()
        return redirect('lista-author')
    
@login_required(login_url='login') 
def del_all_author(request):
    author = Author.objects.all()
    if request.method == "POST":
        author.delete()
        return redirect("lista-author")

@login_required(login_url='login') 
def profile_author(request,id_author):
    author = Author.objects.get(id_author=id_author)
    context = {
        'author': author
    }
    return render(request, 'author/profile_author.html', context)

@login_required(login_url='login') 
def edit_profile_photo(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST' and 'foto_profile' in request.FILES:
        author.foto_profile = request.FILES['foto_profile']
        author.save()
        messages.success(request, "Troka Foto Profile Susesu !!")
    return redirect('profile-author', id_author=author.id_author)

@login_required(login_url='login') 
def del_foto_profile_author(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == "POST":
        if author.foto_profile:
            author.foto_profile.delete(save=False)
        author.foto_profile = None
        author.save()
        messages.success(request, "Apaga Foto Profile Susesu !!")
    return redirect("profile-author", id_author=id_author)

@login_required(login_url='login') 
def edit_detalla_profile(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST':
        form = AuthorDetallaForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guarda Dados Susesu !')
            return redirect('profile-author', id_author=author.id_author)
    else:
        form = AuthorDetallaForm(instance=author)
    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/profile_author.html', context)

@login_required(login_url='login') 
def edit_deskrisaun_profile(request, id_author):
    author = get_object_or_404(Author, id_author=id_author)
    if request.method == 'POST':
        form = EditAuthorDeskrisaunForm(request.POST, instance = author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guarda Dados Susesu !')
            return redirect('profile-author', id_author=author.id_author)
    else:
        form = EditAuthorDeskrisaunForm(instance = author)
    context = {
        "form" : form,
        "author" : author
    }
    return render(request, "author/profile_author.html", context)


