from datetime import date, timezone
from email.policy import default
from statistics import mode
from django.db import models
from django.forms import ValidationError

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

class Achat(models.Model):
    cabinet_facturation = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name="factures")
    cabinet_livraison = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name="livraisons")
    ref_interne = models.CharField(max_length=100)
    materiel = models.TextField()
    date_devis = models.DateField(auto_now_add=True)
    valide = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "achat ref interne : {}".format(self.ref_interne)

    