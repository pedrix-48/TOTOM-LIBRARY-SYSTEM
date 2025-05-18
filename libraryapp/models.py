from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.contrib.auth.models import User

class Admin_user(models.Model):
    naran_admin = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    foto_profile = models.ImageField( blank=True)

class Departamento(models.Model):
    id_dep = models.CharField(max_length=5, primary_key=True)
    naran_dep = models.CharField(max_length=50)

    def __str__(self):
        return self.naran_dep
class Periodo(models.Model):
    tinan_periodo = models.CharField(max_length=4, unique=True)

    def __str__ (self):
        return self.tinan_periodo

class Estudante(models.Model):
    nre = models.CharField(max_length=11, primary_key=True)
    naran_estudante = models.CharField(max_length=50)
    sexu = models.CharField(max_length=4, choices=[('Mane','Mane'), ('Feto', 'Feto')])
    id_dep = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nu_telefone = models.CharField(max_length=11)
    data_moris = models.DateField(default="2000-01-01")
    email = models.EmailField(blank=True, max_length=50)
    hela_fatin = models.CharField(max_length= 30)

    def __str__(self):
        return self.naran_estudante

class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    naran_author = models.CharField(max_length=50)
    data_moris = models.DateField(default='2000-01-01')
    email = models.EmailField(max_length=50, blank=True)
    sexu = models.CharField(max_length=4, choices=[('Mane','Mane'), ('Feto', 'Feto')])
    nasaun = models.CharField(max_length=20, default="Timor Leste")
    deskrisaun = models.TextField(default="Hau Gosta Han Hudi :)")
    foto_profile = models.ImageField( blank=True)

    def __str__(self):
        return self.naran_author

class Livru(models.Model):
    id_livru = models.AutoField(primary_key=True)
    titulu_livru = models.CharField(max_length=100)
    data_publish = models.DateField(default= '2000-01-01')
    nasaun = models.CharField(max_length=20, default="Timor Leste")
    tipu_livru = models.CharField(max_length=11, choices=[
            ("Novel","Novel"), 
            ("Light Novel","Light Novel"), 
            ("Manga","Manga"), 
            ("Education", "Education"), 
            ("History", "History"), 
            ("Thesis","Thesis"),
            ("Children","Children"),
        ],
        default="Novel"
    )
    foto_livru = models.ImageField(blank=True)
    sypnosis = models.TextField(default="BUKU NE TERBAIIIIKKK !!!")
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def short_sypnosis(self):
        plain_text = strip_tags(self.sypnosis)
        return Truncator(plain_text).words(20, truncate='...')


    def __str__(self):
        return self.titulu_livru

class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    naran_staff = models.CharField(max_length=100)
    data_moris = models.DateField(default= '2000-01-01')
    sexu = models.CharField(max_length=4, choices=[('Mane','Mane'), ('Feto', 'Feto')])
    nu_telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, default="")
    hela_fatin = models.CharField(max_length=50)
    foto_staff = models.ImageField(blank=True)

    def __str__(self):
        return self.naran_staff

class StaffUser(models.Model):
    id_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

'''  Se Fix
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []


    # def has_perm(self, perm, obj = None):
    #     return True
    
    # def has_module_perms(self, perm, obj = None):
    #     return True

    # def __str__(self):
    #     return self.naran_staff
'''

class Empresta(models.Model):
    id_empresta = models.CharField(max_length= 10, primary_key=True)
    nre = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    id_livru = models.ForeignKey(Livru, on_delete=models.CASCADE)
    id_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    data_empresta = models.DateField()
    data_devolve = models.DateField()



