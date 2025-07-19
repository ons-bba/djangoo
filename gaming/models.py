from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_code_length(value):
    if len(str(value)) != 4:
        raise ValidationError('Code must be exactly 4 digits')

def validate_future_date(value):
    if value < timezone.now():
        raise ValidationError('Date must be today or in the future')

class Joueur(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

class Séance(models.Model):
    ETAT_CHOICES = [('dispo', 'Disponible'), ('non dispo', 'Non Disponible')]
    
    code = models.IntegerField(primary_key=True, validators=[validate_code_length])
    titre = models.CharField(max_length=100)
    date_début = models.DateTimeField(validators=[validate_future_date])
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='non dispo')
    organisateur = models.ForeignKey(Joueur, on_delete=models.CASCADE)

class Session(models.Model):
    séance = models.ForeignKey(Séance, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)