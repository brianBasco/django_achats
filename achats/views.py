from django.shortcuts import render
from achats.models import Cabinet
from achats.forms import CabinetForm
from achats.forms import CabinetV2Form
from achats.forms import AchatForm
from achats.forms import MailForm

# Create your views here.
def index(request):
    form = AchatForm()
    return render(request, 'index.html', {'form': form})

"""Lors d'un achat, le visuel du mail à envoyé est affiché"""
def achat(request):
    form = AchatForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mail = MailForm()
            return render(request, 'generation/index.html', {'form' : mail})

    
    return render(request, 'index.html', {'form' : form} )



def cabinets(request):
    cabinets = Cabinet.objects.all()
    context = {'cabinets': cabinets}
    return render(request, 'cabinets/index.html', context=context)

def postCabinet(request):
    # a faire : 
    # si Get request : Afficher form vide : OK
    # Si Post request : récupérer les données : OK
    # valider les données : tester avec nom de plus de 3 lettres

    if request.method == 'POST':
        form = CabinetV2Form(request.POST)
        if form.is_valid():
            """nom_gcl = form.cleaned_data['nom_gcl']
            nom_juridique = form.cleaned_data['nom_juridique']
            data = {'nom_gcl': nom_gcl, 'nom_juridique': nom_juridique}
            form = CabinetForm(data)"""
            cabinet = form.save(commit = False)
            cabinet.save()
            return render(request, 'cabinets/form.html', {'form': form})
        else : 
            # récupérer les erreurs et les renvoyer
            return render(request, 'cabinets/form.html', {'form': form})

    #data = {'nom_gcl': 'un Nom gcl','nom_juridique': 'un Nom juridique'}
    form = CabinetV2Form()
    return render(request, 'cabinets/form.html', {'form': form})