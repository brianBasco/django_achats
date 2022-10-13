from django.shortcuts import render
from achats.models import Cabinet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cabinets(request):
    cabinets = Cabinet.objects.all()
    context = {'cabinets': cabinets}
    return render(request, 'cabinets/index.html', context=context)
