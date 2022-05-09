from django.urls import path

from . import views

urlpatterns = [
    path('formulaire/', views.formulaire, name='formulaire'),
    path('formulairedirect/<int:id>/', views.formulairedirect, name='formulairedirect'),
    path('traitement/', views.traitement),
    path('traitementdirect/<int:id>', views.traitementdirect),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('',views.index),
    path('accueil/',views.accueil),
    path('formulairebiblio/', views.formulairebiblio, name="formulairebiblio"),
    path('traitementbiblio/', views.traitementbiblio),
    path('affichebiblio/<int:id>/', views.affichebiblio),
    path('deletebiblio/<int:id>/', views.deletebiblio),
    path('updatebiblio/<int:id>/', views.updatebiblio),
    path('updatetraitementbiblio/<int:id>/', views.updatetraitementbiblio),
]
