from django.db import models
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
from django import forms

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

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


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.titre
    # Ajoutez d'autres champs comme la date de publication.

def view_publication(request, publication_id):
    publication = Publication.objects.get(pk=publication_id)
    comments = publication.comments.all()

class Tarif(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs comme la description du service.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    # Ajoutez d'autres champs comme la date et l'heure du message.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    content = models.TextField()
    comments = GenericRelation(Comment)


