from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

class Joueur(AbstractUser):
    email = models.EmailField(blank=True)
    nom = models.CharField(max_length=100, blank=True)
    prenom = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

class Seance(models.Model):
    code = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=200)
    date_debut = models.DateTimeField()
    ETAT_CHOICES = [('dispo', 'Disponible'), ('non_dispo', 'Non disponible')]
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default='non_dispo')
    organisateur = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='seances_organisees')
    participants = models.ManyToManyField(Joueur, related_name='seances_participees', blank=True)

    def clean(self):
        if self.date_debut.date() != timezone.now().date():
            raise ValidationError("La date de début doit être aujourd’hui.")
        if len(str(self.code)) != 4:
            raise ValidationError("Le code de la séance doit contenir exactement 4 chiffres.")

    def __str__(self):
        return f"{self.titre} (Code: {self.code})"

class Session(models.Model):
    date = models.DateField()
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, related_name='sessions')
    participants = models.ManyToManyField(Joueur, related_name='sessions')

    def __str__(self):
        return f"Session du {self.date} - Séance {self.seance.code}"
