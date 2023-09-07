from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse_ville = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=15)
    photo_de_profil = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    profile_completed = models.BooleanField(default=False)  # Champ pour indiquer si le profil est complet

    def __str__(self):
        return self.user.username

class Animal(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom   

class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)  # Vous pouvez créer un modèle Adresse séparé
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15)
    animaux = models.ManyToManyField(Animal, choices=(
        ('chien', 'Chien'),
        ('chat', 'Chat'),
        ('poule', 'Poule'),
        ('oiseau', 'Oiseau'),
        ('lapin', 'Lapin'),
        ('poisson', 'Poisson'),
        ('autre', 'Autre'),
    ))
    besoins = models.ManyToManyField('Service', related_name='proprietaires')
    commentaire = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username

    
class Prestataire(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)  # Encore une fois, envisagez un modèle Adresse
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15)
    type_services = models.ManyToManyField(Service, related_name='prestataires')
    tarifs = models.DecimalField(max_digits=10, decimal_places=2)
    references = models.DecimalField(max_digits=3, decimal_places=2)
    commentaire = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username





