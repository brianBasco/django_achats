from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('achat', views.achat),
    path('cabinets', views.cabinets),
    path('cabinets/form', views.postCabinet),
    path('suivi_achats', views.suivi_achats),
]
