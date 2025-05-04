from django.db import models 

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

class Estudante(models.Model):
    nre = models.CharField(max_length=11, primary_key=True)
    naran_estudante = models.CharField(max_length=50)
    sexu = models.CharField(max_length=1, choices=[('M','Mane'), ('F', 'Feto')])
    id_dep = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=4)
    nu_telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.naran_estudante

class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    naran_author = models.CharField(max_length=50)
    data_moris = models.DateField(default='2000-01-01')
    sexu = models.CharField(max_length=1, choices=[('M','Mane'), ('F', 'Feto')])
    email = models.CharField(max_length=50)
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

    def __str__(self):
        return self.titulu_livru

class Staff(models.Model):
    id_staff = models.CharField(max_length=20, primary_key=True)
    naran_staff = models.CharField(max_length=100)
    sexu = models.CharField(max_length=1, choices=[('M','Mane'), ('F', 'Feto')])
    nu_telefone = models.CharField(max_length=11)
    hela_fatin = models.CharField(max_length=49)

    def __str__(self):
        return self.naran_staff

class Empresta(models.Model):
    id_empresta = models.CharField(max_length= 10, primary_key=True)
    nre = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    id_livru = models.ForeignKey(Livru, on_delete=models.CASCADE)
    id_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    data_empresta = models.DateField()
    data_devolve = models.DateField()

