from django.urls import path

from . import views

urlpatterns = [
    path('accueil/',views.accueilliste),
    path('ajoutsadmin/', views.index),
    path('listecatego/', views.indexdeux),
    path('formulaire/', views.formulaireliste, name='formulaire'),
    path('traitement/', views.traitementliste),
    path('affiche/<int:id>/', views.afficheliste),
    path('delete/<int:id>/', views.deleteliste),
    path('update/<int:id>/', views.updateliste),
    path('updatetraitement/<int:id>/', views.updatetraitementliste),

    path('formulairedirect/<int:id>/', views.formulairedirect),
    path('traitementdirect/<int:id>/', views.traitementdirect),

    path('accueilequipe/', views.accueilequipe),
    path('formulaireequipe/', views.formulaireequipe),
    path('traitementequipe/', views.traitementequipe),
    path('afficheequipe/<int:id>/', views.afficheequipe),
    path('deleteequipe/<int:id>/', views.deleteequipe),
    path('updateequipe/<int:id>/', views.updateequipe),
    path('updatetraitementequipe/<int:id>/', views.updatetraitementequipe),
]
