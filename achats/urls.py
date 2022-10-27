from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('achat', views.achat, name='achat'),
    path('cabinets', views.cabinets, name='cabinets'),
    path('cabinets/form', views.postCabinet, name='postCabinet'),
    path('suivi_achats', views.suivi_achats, name='suivi_achats'),
    path('envoyer_mail', views.envoyer_mail, name='envoyer_mail'),
    path('modifier_achat/<int:id>', views.modifier_achat, name="modifier_achat")
]
