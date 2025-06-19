from django.shortcuts import redirect, render, get_object_or_404
from libraryapp.models import Estudante, Periodo
from django.contrib.auth.decorators import login_required 
from .forms_est import AddEstudanteForm, EditEstudanteForm
from django.contrib import messages
import openpyxl as xl

@login_required(login_url='login') 
def lista_estudante(request):
    estudantes = Estudante.objects.all()
    form = AddEstudanteForm()
    periodo = Periodo.objects.all()
    labels = [
        "Mecanica",
        "Electro Electronica",
        "Civil",
        "Informatica",
        "Geologia Petroleo"
    ]
    data = [
        Estudante.objects.filter(id_dep__naran_dep="Engenharia Mecanica").count(),
        Estudante.objects.filter(id_dep__naran_dep="Engenharia Electro Electronica").count(),
        Estudante.objects.filter(id_dep__naran_dep="Engenharia Civil").count(),
        Estudante.objects.filter(id_dep__naran_dep="Engenharia Informatica").count(),
        Estudante.objects.filter(id_dep__naran_dep="Engenharia Geologia e Petroleo").count()
    ]

    context = {
        "estudantes": estudantes,
        "form": form,
        "periodo": periodo,
        'labels': labels,
        'data': data
    }
    
    return render(request, 'lista_estudante.html' ,context)

    

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


@login_required(login_url='login')
def import_est_xl(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel_file")
        if excel_file.name.endswith(".xlsx"):
            wb = xl.load_workbook(excel_file)
            sheet = wb.active

            for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                try:
                    # Make sure row has exactly 8 values
                    if len(row) != 9:
                        raise ValueError(f"Row {row_num} has {len(row)} columns, expected 9.")

                    nre, naran_estudante, sexu, id_dep, periodo, nu_telefone, data_moris, email, hela_fatin= row

                    estudante = Estudante.objects.create(
                        nre=nre,
                        naran_estudante=naran_estudante,
                        sexu=sexu,
                        id_dep_id=id_dep,  
                        periodo_id=periodo,  
                        nu_telefone=str(nu_telefone),
                        data_moris=data_moris,
                        email=email,
                        hela_fatin=hela_fatin,
                    )
                    
                    estudante.save()
                except ValueError as ve:
                    messages.error(request, f"Falla Atu Importa Linha {row_num}: {ve}")

                except Exception as e:
                    messages.error(request, f"Falla Atu Importa Linha {row_num}: {row} - {e}")
        else:
            messages.error(request, "Formatu File Invalidu, Favor Upload File Ho Formatu Excel")
    return redirect("lista-estudante")

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
    
def del_all_estudante(request):
    estudante = Estudante.objects.all()
    if request.method == "POST":
        estudante.delete()
        return redirect('lista-estudante')
    
