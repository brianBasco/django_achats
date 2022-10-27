
from asyncio.windows_events import NULL
from contextlib import nullcontext
from queue import Empty

from django.core.mail import send_mail
from django.forms import NullBooleanField
from django.http import HttpResponse
from django.shortcuts import redirect, render

from achats.forms import AchatForm, CabinetV2Form, CommandeForm
from achats.models import Achat, Cabinet


# Create your views here.
def index(request):
    form = AchatForm()
    return render(request, 'home/index.html', {'form': form})

"""Lors d'un achat, le visuel du mail à envoyé est affiché"""
def achat(request):
    form = AchatForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            achat = Achat()
            #l'instance est remplie avec le retour de l'enregistrement
            achat = form.save()
            return render(request, 'generation/index.html', {'achat' : achat})

    
    return render(request, 'home/index.html', {'form' : form} )



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


# ajouter de la recherche suivant des critères
def suivi_achats(request):
    #Affichage des achats
    achats = Achat.objects.all()
    # options avec valide et dates
    options = request.GET.dict()
    #print (options)
    print("options is empty ?? :" + str(not bool(options)))
    if options :
        print (options)
        achats = Achat.objects.filter(valide=options['valide'])
    
    return render(request, 'suivi_achats/index.html', {'achats': achats})

def modifier_achat(request, id: int):
    achat = Achat.objects.get(pk=id)
    form = CommandeForm(instance=achat)
    if request.method == "POST":
        form = CommandeForm(request.POST, instance=achat)
        if form.is_valid():
            achat = form.save(commit = False)
            achat.save()
            return redirect(to=suivi_achats)
    return render(request, 'suivi_achats/form.html', {'form' : form})

def envoyer_mail(request):

    #récupération de POST
    _subject = "GCL - Devis Ref interne : " + request.POST.get("sujet") 
    _message = request.POST.get("message")
    _from = "from@example.com"
    _to = ['bast620@gmail.com']
    send_mail(
    _subject,
    _message,
    _from,
    _to,
    fail_silently=False,)
    # renvoyer un flash message : Mail envoyé !
    return redirect(to=index)
