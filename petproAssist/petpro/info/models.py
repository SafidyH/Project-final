from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Autres champs pour le profil de l'Owner (nom, prénom, etc.)

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Autres champs pour le profil du Prestataire (nom, prénom, etc.)

class ServiceOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)

class VetNumber(models.Model):
    vet_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Autres champs pour les détails du vétérinaire

class CustomUser(AbstractUser):
    # Champs supplémentaires pour votre modèle User
    is_owner = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    # Autres champs spécifiques

    def __str__(self):
        return self.username
