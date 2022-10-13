from django.db import models

# Create your models here.
class Cabinet(models.Model):
    nom_gcl = models.CharField(max_length=200)
    nom_juridique = models.CharField(max_length=200)
    siret = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "{}".format(self.nom_gcl)
