from django.http import HttpResponseRedirect
from .forms import EquipementForm, EquipeDirectForm, ListeEquipementForm
from django.shortcuts import render
from . import models

def formulaireliste(request):
    if request.method == "POST":
        form = ListeEquipementForm(request)
        if form.is_valid():
            return HttpResponseRedirect("listeequipements/traitement/")
        else:
            return render(request, 'listeequipements/formulaireliste.html', {'form': form})
    else:
        form = ListeEquipementForm()
        return render(request, 'listeequipements/formulaireliste.html', {'form': form})




def traitementliste(request):
    if request.method == "POST":
        pForm = ListeEquipementForm(request.POST)
        if pForm.is_valid():
            equipementok = pForm.save()
            return render(request, 'listeequipements/traitementliste.html', {'equipementok':equipementok})
        else:
            return render(request, 'listeequipements/formulaireliste.html', {'form': pForm})



def afficheliste(request, id):
     equipement = models.ListeEquipement.objects.get(pk=id)
     liste = models.LesEquipement.objects.filter(typeobjet=id)
     return render(request,"listeequipements/detailsliste.html",{"equipement": equipement, "liste": liste})



def updateliste(request, id):
    livre=models.ListeEquipement.objects.get(pk=id)
    form = ListeEquipementForm(livre.dico())
    return render(request, "listeequipements/formulaireliste.html",{"form":form, "id": id})


def updatetraitementliste(request, id):
    lform = ListeEquipementForm(request.POST)
    if lform.is_valid():
        equipement = lform.save(commit = False)
        equipement.id = id
        equipement.save()
        return HttpResponseRedirect("/taupeachat/accueil/")
    else:
        return render(request, "listeequipements/formulaireliste.html",{"form" : lform, "id": id})


def deleteliste(request, id):
     livre = models.ListeEquipement.objects.get(pk=id)
     livre.delete()
     return HttpResponseRedirect("/taupeachat/accueil/")





def index(request):
    listetypeequipe = list(models.ListeEquipement.objects.all())
    return render(request, "equipements/ajoutsadmin.html",{"listetypeequipe" : listetypeequipe})

def indexdeux(request):
    listetypeequipe = list(models.ListeEquipement.objects.all())
    return render(request, "equipements/listecatego.html",{"listetypeequipe" : listetypeequipe})








def accueilliste(request):
    listetypeequipe = list(models.ListeEquipement.objects.all())
    return render(request, "listeequipements/accueilliste.html",{"listetypeequipe" : listetypeequipe})


def accueilequipe(request):
   listeequipe=list(models.LesEquipement.objects.all())
   return render(request, "equipements/accueil.html",{"listeequipe":listeequipe})




def formulaireequipe(request):
     if request.method == "POST":
         form = EquipementForm(request)
         if form.is_valid():
             return HttpResponseRedirect("traitement/")
         else:
             return render(request, 'equipements/formulaire.html', {'form': form})
     else:
         form = EquipementForm()
         return render(request, 'equipements/formulaire.html', {'form': form})


def traitementequipe(request):
    if request.method == "POST":
        pForm = EquipementForm(request.POST)
        if pForm.is_valid():
            equipmnt = pForm.save()
            return render(request, 'equipements/traitement.html', {'equipmnt': equipmnt})
        else:
            return render(request, 'livre/formulaire.html', {'form': pForm})


def afficheequipe(request, id):
     equipementok = models.LesEquipement.objects.get(pk=id)
     return render(request,"equipements/affiche.html",{"equipementok": equipementok})


def deleteequipe(request, id):
    livre = models.LesEquipement.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/taupeachat/accueilequipe/")


def updateequipe(request, id):
     biblio=models.LesEquipement.objects.get(pk=id)
     form = EquipementForm(biblio.dico())
     return render(request, "equipements/formulaire.html",{"form":form, "id": id})


def updatetraitementequipe(request, id):
     lform = EquipementForm(request.POST)
     if lform.is_valid():
         bibli = lform.save(commit = False)
         bibli.id = id
         bibli.save()
         return HttpResponseRedirect("/taupeachat/accueilequipe")
     else:
         return render(request, "equipements/formulaire.html",{"form" : lform, "id": id})





def formulairedirect(request, id):
         form = EquipeDirectForm()
         return render(request, 'equipements/formulairedirect.html', {'form': form, "id":id})


def traitementdirect(request, id):
    typeobjet = models.ListeEquipement.objects.get(pk=id)
    if request.method == "POST":
         pForm = EquipeDirectForm(request.POST)
         if pForm.is_valid():
             livre = pForm.save(commit=False)
             livre.typeobjet = typeobjet
             livre.typeobjet_id = id
             livre.save()
             return render(request, 'equipements/traitementdirect.html', {'livre': livre, "id":id})
         else:
             return render(request, 'equipements/formulairedirect.html', {'form': pForm, "id":id})