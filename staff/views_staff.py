from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from libraryapp.models import Staff, StaffUser, User
from .forms_staff import StaffForm, EditDetallaFormStaff, UserEditForm, BootstrapPasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
import openpyxl as xl


@login_required(login_url='login')
def lista_staff(request):
    staffs = Staff.objects.all()
    form = StaffForm()
    
    staff_data = []
    for staff in staffs:
        try:
            staff_user = StaffUser.objects.get(id_staff=staff)
            username = staff_user.user.username
            password = staff_user.user.password 
        except StaffUser.DoesNotExist:
            username = "—"  # Or leave blank
            password = "—"  # Or leave blank
        
        staff_data.append({
            'staff': staff,
            'username': username,
            'password': password,
        })

    context = {
        "staffs": staff_data,  # list of dicts
        "form": form
    } 
    return render(request, 'lista_staff.html', context)

@login_required(login_url='login')
def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-staff")
        else:
            messages.error(request, form.errors)
    else:
        form = StaffForm()
    return render(request, "add_staff.html", {"form" : form})


@login_required(login_url='login')
def import_staff_xl(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel_file")
        if excel_file.name.endswith(".xlsx"):
            wb = xl.load_workbook(excel_file)
            sheet = wb.active

            for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                try:
                    # Make sure row has exactly 8 values
                    if len(row) != 6:
                        raise ValueError(f"Row {row_num} has {len(row)} columns, expected 6.")

                    naran_staff, data_moris, sexu, nu_telefone, email, hela_fatin = row

                    Staff.objects.create(
                        naran_staff=naran_staff,
                        # username=username,
                        # password=make_password(password),
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

@login_required(login_url='login')
def edit_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff=id_staff)
    
    try:
        staff_user = StaffUser.objects.get(id_staff=staff)
        user = staff_user.user
    except StaffUser.DoesNotExist:
        messages.error(request, "Staff Laiha !")
        return redirect("lista-staff")
    
    if request.method == "POST":
        staff_form = StaffForm(request.POST, request.FILES, instance=staff)
        user_form = UserEditForm(request.POST, instance=user)
        
        if staff_form.is_valid() and user_form.is_valid():
            staff_form.save()
            username = user_form.cleaned_data['username']
            user.username = username
            user.save()
            
            messages.success(request, "Guarda Dados Susesu !")
            return redirect("lista-staff")
        else:
            if staff_form.errors:
                messages.error(request, staff_form.errors)
            if user_form.errors:
                messages.error(request, "user_form.errors")
    # else:
    #     staff_form = StaffForm(instance=staff)
    #     user_form = UserEditForm(instance=user)
    
    return render(request, "edit_staff.html", {
        # "staff_form": staff_form,
        # "user_form": user_form,
        "staff": staff,
        "user": user
    })

@login_required(login_url='login')
def del_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff=id_staff)
    
    try:
        staff_user = StaffUser.objects.get(id_staff=staff)
        user = staff_user.user
        user.delete()
        staff_user.delete()
    except StaffUser.DoesNotExist:
        messages.warning(request, "Staff user relationship not found.")
    staff.delete()
    return redirect("lista-staff")

@login_required(login_url='login')
def del_all_staff(request):
    staffs = Staff.objects.all()
    if request.method == "POST":
        staffs.delete()
        return redirect("lista-staff")

@login_required(login_url='login')
def profile_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff = id_staff)
    try:
        staff_user = StaffUser.objects.get(id_staff = staff)
        user = staff_user.user
        password = staff_user.user.password
    except StaffUser.DoesNotExist:
        user = None
    
    return render(request, "profile_staff.html", {"staff" : staff, "user" : user})

@login_required(login_url='login')
def edit_foto_staff(request, id_staff):
    staff = get_object_or_404(Staff, id_staff = id_staff)
    if request.method == "POST" and "foto_staff" in request.FILES:
        staff.foto_staff = request.FILES['foto_staff']
        staff.save()
        messages.success(request, "Troka Foto Profile Susesu !")
        return redirect("profile-staff", id_staff = id_staff)
    return render(request, "profile_staff.html", {"staff" : staff})

@login_required(login_url='login')
def del_foto_staff(request, id_staff):
    staff = get_object_or_404(Staff,id_staff = id_staff)
    if request.method == "POST":
        if staff.foto_staff:
            staff.foto_staff.delete(save = False)
        staff.foto_staff = None
        staff.save()
        messages.success(request, "Apaga Foto Profile Susesu !")
    return redirect("profile-staff", id_staff = id_staff)

@login_required(login_url='login')
def edit_detalla_staff(request, id_staff):
    pass

class EditPasswordStaff(PasswordChangeView):
    template_name = "edit_password.html"
    success_url = "/staff/list/"
    form_class = BootstrapPasswordChangeForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        staff = get_object_or_404(Staff, id_staff=self.kwargs['id_staff'])

        staff_user = get_object_or_404(StaffUser, id_staff=staff)
        kwargs['user'] = staff_user.user  # Now this works
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = get_object_or_404(Staff, id_staff=self.kwargs['id_staff'])
        context['staff'] = staff
        return context

