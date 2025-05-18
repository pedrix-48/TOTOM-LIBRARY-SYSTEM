from libraryapp.models import StaffUser

def filter_user(request):
    obj =  StaffUser.objects.filter(user = request.user).first()
    return obj