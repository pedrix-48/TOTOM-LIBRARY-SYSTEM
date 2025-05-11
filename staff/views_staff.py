from django.shortcuts import render, redirect
from django.contrib import messages
from libraryapp.models import Staff
from .forms_staff import StaffForm
from django.contrib.auth.hashers import make_password

def lista_staff(request):
    staffs = Staff.objects.all()
    form = StaffForm()
    context = {
        "staffs" : staffs,
        "form" : form
    } 
    return render(request, 'lista_staff.html', context)

def add_staff(request):
    staff = Staff()
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.password = make_password(form.cleaned_data['password'])
            staff.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-staff")
        else:
            messages.error(request, form.errors)
    else:
        form = StaffForm()
    context = {
        "form" : form
    }
    return render(request, "add_staff.html", context)

def edit_staff(request, id_staff):
    staff = Staff.objects.get(id_staff = id_staff)
    form = StaffForm(instance = staff)
    if request.method == "POST":
        form = StaffForm(request.POST, instance = staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-staff")
        else:
            messages.error(request, form.errors)
    return render(request, "edit_staff.html", {"staff" : staff, "form" : form})


def del_staff(request, id_staff):
    staff = Staff.objects.get(id_staff=id_staff)
    if request.method == "POST":
        staff.delete()
        return redirect('lista-staff')
    
def del_all_staff(request):
    staffs = Staff.objects.all()
    if request.method == "POST":
        staffs.delete()
        return redirect("lista-staff")
    


