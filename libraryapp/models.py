from django.db import models



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

class Auhtor(models.Model):
    id_author = models.CharField(max_length=5, primary_key=True)
    naran_author = models.CharField(max_length=100)
    sexu = models.CharField(max_length=1, choices=[('M','Mane'), ('F', 'Feto')])
    email = models.CharField(max_length=20)
    nasaun = models.CharField(max_length=20)

    def __str__(self):
        return self.naran_author

class Livru(models.Model):
    id_livru = models.CharField(max_length=10, primary_key=True)
    naran_livru = models.CharField(max_length=100)
    data_publish = models.DateField()
    id_author = models.ForeignKey(Auhtor, on_delete=models.CASCADE)

    def __str__(self):
        return self.naran_livru

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





