from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length = 100)
    #date_parution = models.DateField(blank=True, null=True)
    bibliotheque = models.ForeignKey("Biblio", on_delete=models.CASCADE, null=True)
    nombres_pages = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"Titre : {self.titre} | Auteur : {self.auteur}"
        return chaine

    def dico(self):
        return {"titre":self.titre, "auteur": self.auteur, "nombres_pages":self.nombres_pages, "resume":self.resume}



class Biblio(models.Model):
    nom = models.CharField(max_length=100)
    region = models.CharField(max_length = 100)
    #date_parution = models.DateField(blank=True, null=True)
    ville = models.CharField(max_length = 100)
    nombre_livre = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"Bibliothèque '{self.nom}' | Située dans la région {self.region}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "ville": self.ville, "nombre_livre":self.nombre_livre, "region":self.region}




class LivreDirect(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length = 100)
    #date_parution = models.DateField(blank=True, null=True)
    nombres_pages = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"Titre : {self.titre} | Auteur : {self.auteur}"
        return chaine