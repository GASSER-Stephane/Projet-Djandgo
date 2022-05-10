from django.http import HttpResponseRedirect
from .forms import LivreForm, BiblioForm, LivreDirectForm
from django.shortcuts import render
from . import models

def formulaire(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            return HttpResponseRedirect("traitement/")
        else:
            return render(request, 'livre/formulaire.html', {'form': form})
    else:
        form = LivreForm()
        return render(request, 'livre/formulaire.html', {'form': form})


def traitement(request):
    if request.method == "POST":
        pForm = LivreForm(request.POST)
        if pForm.is_valid():
            livre = pForm.save()
            return render(request, 'livre/traitement.html', {'livre': livre})
        else:
            return render(request, 'livre/formulaire.html', {'form': pForm})


def affiche(request, id):
    livre =models.Livre.objects.get(pk=id)
    return render(request,"livre/affiche.html",{"livre": livre})


def index(request):
    liste=list(models.Livre.objects.all())
    return render(request, "livre/index.html",{"livre": liste})


def update(request, id):
    livre=models.Livre.objects.get(pk=id)
    form = LivreForm(livre.dico())
    return render(request, "livre/formulaire.html",{"form":form, "id": id})


def updatetraitement(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit = False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect("/livre/")
    else:
        return render(request, "livre/formulaire.html",{"form" : lform, "id": id})


def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/livre/")





def accueil(request):
    biblio=list(models.Biblio.objects.all())
    return render(request, "Biblio/accueil.html",{"biblio": biblio})


def formulairebiblio(request):
    if request.method == "POST":
        form = BiblioForm(request)
        if form.is_valid():
            return HttpResponseRedirect("traitement/")
        else:
            return render(request, 'Biblio/formulairebiblio.html', {'form': form})
    else:
        form = BiblioForm()
        return render(request, 'Biblio/formulairebiblio.html', {'form': form})


def traitementbiblio(request):
    if request.method == "POST":
        pForm = BiblioForm(request.POST)
        if pForm.is_valid():
            Biblio = pForm.save()
            return render(request, 'Biblio/traitementbiblio.html', {'biblio': Biblio})
        else:
            return render(request, 'Biblio/formulairebiblio.html', {'form': pForm})


def affichebiblio(request, id):
    Biblio =models.Biblio.objects.get(pk=id)
    liste=list(models.Livre.objects.filter(bibliotheque_id=id))
    return render(request,"Biblio/affichebiblio.html",{"biblio": Biblio, "liste": liste})


def deletebiblio(request, id):
    biblio = models.Biblio.objects.get(pk=id)
    biblio.delete()
    return HttpResponseRedirect("/livre/accueil")


def updatebiblio(request, id):
    biblio=models.Biblio.objects.get(pk=id)
    form = BiblioForm(biblio.dico())
    return render(request, "Biblio/formulairebiblio.html",{"form":form, "id": id})


def updatetraitementbiblio(request, id):
    lform = BiblioForm(request.POST)
    if lform.is_valid():
        bibli = lform.save(commit = False)
        bibli.id = id
        bibli.save()
        return HttpResponseRedirect("/livre/accueil")
    else:
        return render(request, "Biblio/formulairebiblio.html",{"form" : lform, "id": id})





def formulairedirect(request, id):
        form = LivreDirectForm()
        return render(request, 'livre/livredansbiblio.html', {'form': form, "id":id})


def traitementdirect(request, id):
    if request.method == "POST":
        pForm = LivreDirectForm(request.POST)
        if pForm.is_valid():
            livre = pForm.save(commit=False)
            livre.bibliotheque_id = id
            livre.bibliotheque = models.Biblio.objects.get(pk=id)
            livre.save()
            return render(request, 'livre/traitementdirect.html', {'livre': livre, "id":id})
        else:
            return render(request, 'livre/livredansbiblio.html', {'form': pForm, "id":id})