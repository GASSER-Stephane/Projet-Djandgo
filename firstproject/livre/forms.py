from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
#        fields = ('titre', 'auteur', 'date_parution', 'nombres_pages','resume')
        fields = ('titre', 'auteur', 'bibliotheque','nombres_pages','resume')

        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            #'date_parution' : _('date␣de␣parution'),
            'bibliotheque' : _('Bibliotheque'),
            'nombres_pages' : _('Nombres de pages'),
            'resume' : _('Résumé')
        }


class BiblioForm(ModelForm):
    class Meta:
        model = models.Biblio
        fields = ('nom','region','ville','nombre_livre')

        labels = {
            'nom' : _('Nom'),
            'region' : _('Région') ,
            'ville' : _('Ville'),
            'nombre_livre' : _('Nombre de livres')
        }


class LivreDirectForm(ModelForm):
    class Meta:
        model = models.Livre
#        fields = ('titre', 'auteur', 'date_parution', 'nombres_pages','resume')
        fields = ('titre', 'auteur','nombres_pages','resume')

        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'nombres_pages' : _('Nombres de pages'),
            'resume' : _('Résumé')
        }