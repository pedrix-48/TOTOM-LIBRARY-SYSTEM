from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from libraryapp.models import Staff
from .forms_staff import StaffForm
from django.contrib.auth.hashers import make_password
import openpyxl as xl

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
    return render(request, "add_staff.html", {"form" : form})

def import_staff_xl(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel_file")
        if excel_file.name.endswith(".xlsx"):
            wb = xl.load_workbook(excel_file)
            sheet = wb.active

            for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                try:
                    # Make sure row has exactly 8 values
                    if len(row) != 8:
                        raise ValueError(f"Row {row_num} has {len(row)} columns, expected 8.")

                    naran_staff, username, password, data_moris, sexu, nu_telefone, email, hela_fatin = row

                    Staff.objects.create(
                        naran_staff=naran_staff,
                        username=username,
                        password=make_password(password),
                        data_moris=data_moris,
                        sexu=sexu,
                        nu_telefone=str(nu_telefone),
                        email=email,
                        hela_fatin=hela_fatin,
                    )
                except Exception as e:
                    messages.error(request, f"Falla Atu Importa Linha {row_num}: {row} - {e}")
        else:
            messages.error(request, "Formatu File Invalidu, Favor Upload File Ho Formatu Excel")
    return redirect("lista-staff")


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
    
def profile_staff(request, id_staff):
    staff = Staff.objects.get(id_staff = id_staff)
    return render(request, "profile_staff.html", {"staff" : staff})

def edit_foto_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff = id_staff)
    if request.method == "POST" and "foto_staff" in request.FILES:
        staff.foto_staff = request.FILES['foto_staff']
        staff.save()
        messages.success(request, "Troka Foto Profile Susesu !")
        return redirect("profile-staff", id_staff = id_staff)
    return render(request, "profile_staff.html", {"staff" : staff})

def del_foto_staff(request, id_staff):
    staff = get_object_or_404(Staff,id_staff = id_staff)
    if request.method == "POST":
        if staff.foto_staff:
            staff.foto_staff.delete(save = False)
        staff.foto_staff = None
        staff.save()
        messages.success(request, "Apaga Foto Profile Susesu !")
    return redirect("profile-staff", id_staff = id_staff)

    


