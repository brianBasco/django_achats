from typing import Sequence

from django import forms
from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Achat, Cabinet

""" Modèle de formulaire non utilisé, à garder pour l'exemple"""
class CabinetForm(forms.Form):
    nom_gcl = forms.CharField(label='nom gcl',max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    nom_juridique = forms.CharField(label='nom juridique',max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))

    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(CabinetForm, self).clean()
         
        # extract the username and text field from the data
        nom_gcl = self.cleaned_data.get('nom_gcl')
 
        # conditions to be met for the username length
        if len(nom_gcl) < 3:
            self._errors['nom_gcl'] = self.error_class([
                'Minimum 3 characters required'])
         
        # return any errors if found
        return self.cleaned_data
        

""" Formulaire actuellement utilisé """
class CabinetV2Form(ModelForm):
    class Meta:
        model = Cabinet
        fields = '__all__'
        labels = {
            'nom_gcl': _('Nom GCL'),
            'nom_juridique': _('Nom juridique'),
            'code_postal': _('Code postal'),
        }
        help_texts = {
            'nom_gcl': _('Le nom GCL.'),
        }
    

class AchatForm(ModelForm):

    class Meta:
        model = Achat
        exclude = ['date_devis', 'valide', 'commentaire']
        #fields = '__all__'
        labels = {
            'cabinet_facturation' : _('Facturation'),
            'cabinet_livraison' : _('Livraison'),
            'ref_interne' : _('Ref interne'),
            'materiel' : _('Matériel'),
            'date_devis' : _('Date'),
            'valide' : _('validé')
        }


# Pour la nomenclature : 
# un achat pour le devis et une commande lorsque l'ordre d'achat est passé
class CommandeForm(ModelForm):

    class Meta:
        model = Achat
        #exclude = ['date_devis', 'valide', 'commentaire']
        fields = '__all__'
        labels = {
            'cabinet_facturation' : _('Facturation'),
            'cabinet_livraison' : _('Livraison'),
            'ref_interne' : _('Ref interne'),
            'materiel' : _('Matériel'),
            'date_devis' : _('Date'),
            'valide' : _('validé')
        }
