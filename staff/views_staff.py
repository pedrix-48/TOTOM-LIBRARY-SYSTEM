from django.shortcuts import render
from libraryapp.models import Staff

def lista_staff(request):
    staffs = Staff.objects.all()
    context = {
        "staffs" : staffs
    } 
    return render(request, 'lista_staff.html', context)




