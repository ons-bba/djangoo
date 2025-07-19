from django import forms
from .models import Seance

class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['code', 'titre', 'date_debut', 'etat', 'organisateur', 'participants']
        widgets = {
            'date_debut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'participants': forms.CheckboxSelectMultiple,
        }
