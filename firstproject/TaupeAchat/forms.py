from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ListeEquipementForm(ModelForm):
    class Meta:
        model = models.ListeEquipement
        fields = ('nom', 'prixmoyen', 'description')

        labels = {
            'nom': _('Objet'),
            'prixmoyen': _('Prix Moyen'),
            'description': _('Description')
        }


class EquipementForm(ModelForm):
    class Meta:
        model = models.LesEquipement
        fields = ('marques', 'modeles', 'prix', 'poids', 'typeobjet')

        labels = {
            'marques': _('Marque'),
            'modeles': _('Modèle'),
            'prix' : _('Prix'),
            'poids': _('Poids'),
            'typeobjet': _('Catégorie'),
        }


class EquipeDirectForm(ModelForm):
    class Meta:
        model = models.LesEquipement
        fields = ('marques', 'modeles', 'prix', 'poids')

        labels = {
            'marques': _('Marque'),
            'modeles': _('Modèle'),
            'prix' : _('Prix'),
            'poids': _('Poids')
        }

