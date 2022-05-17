from django.db import models


class ListeEquipement(models.Model):
    nom = models.CharField(max_length=100)
    prixmoyen = models.IntegerField(blank=False)
    description = models.CharField(max_length = 100)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "prixmoyen":self.prixmoyen, "description":self.description}




class LesEquipement(models.Model):
    modeles = models.CharField(max_length=100)
    marques = models.CharField(max_length=100)
    prix = models.IntegerField(blank=False)
    poids = models.IntegerField(blank=False)
    typeobjet = models.ForeignKey("ListeEquipement", on_delete=models.CASCADE, null=True)

    def __str__(self):
        chaine = f"-> {self.typeobjet}, de la marque {self.marques} dont le modèle précis est '{self.modeles}'"
        return chaine



    def dico(self):
        return {"modeles":self.modeles, "marques":self.marques, "prix":self.prix, "poids":self.poids, "typeobjet":self.typeobjet}

