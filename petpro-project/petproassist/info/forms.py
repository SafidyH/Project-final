from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Proprietaire, Prestataire, Service, Animal, Publication, Tarif, Message, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

class CustomAuthenticationForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=[('prestataire', 'Prestataire'), ('proprietaire', 'Propriétaire')], required=True, widget=forms.RadioSelect)

class UserRegistrationForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    statut = forms.ChoiceField(choices=[('proprietaire', 'Propriétaire'), ('prestataire', 'Prestataire')])
    first_name = forms.CharField(max_length=30, required=True, help_text='Requis. Entrez votre prénom.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requis. Entrez votre nom de famille.')
    email = forms.EmailField(max_length=254, required=True, help_text='Requis. Entrez une adresse email valide.')
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        help_text="Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être trop courant."
    )
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput,
        help_text="Entrez le même mot de passe que ci-dessus, pour vérification."
    )
    STATUT_CHOICES = (
        ('proprietaire', 'Propriétaire'),
        ('prestataire', 'Prestataire de service'),
    )
    statut = forms.ChoiceField(choices=STATUT_CHOICES, required=True, help_text='Choisissez votre statut.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Requis. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.',
            'password1': 'Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être trop courant.',
            'password2': 'Entrez le même mot de passe que ci-dessus, pour vérification.'
        }

    #class Meta:
       # model = User
        #fields = ['username', 'last_name', 'first_name', 'email', 'statut', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['adresse_ville', 'numero_telephone', 'photo_de_profil', 'profile_completed']

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['animaux', 'besoins', 'commentaire']

class PrestataireForm(forms.ModelForm):
    class Meta:
        model = Prestataire
        fields = ['type_services', 'tarifs', 'references', 'commentaire']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nom']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['content']  # Ajoutez d'autres champs

class Publication(models.Model):
    # Champs de votre modèle Publication
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    # ...

    # Ajoutez GenericRelation pour activer les commentaires
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.titre
class PublicationSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Rechercher des publications')

def view_publication(request, publication_id):
    publication = Publication.objects.get(pk=publication_id)
    comments = publication.comments.all()
    comment_form = CommentForm()  # Affichez ce formulaire dans votre modèle de modèle de publication
    # ...

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ['service_name', 'price']  # Ajoutez d'autres champs

class Tarif(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs comme la description du service.

    def __str__(self):
        return self.service_name

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']  # Ajoutez d'autres champs

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    content = models.TextField()
    # Ajoutez d'autres champs comme la date du commentaire.

    def __str__(self):
        return f"Commentaire de {self.user} sur {self.publication}"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Ajoutez d'autres champs

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    # Ajoutez d'autres champs comme la date et l'heure du message.

    def __str__(self):
        return f"De {self.sender} à {self.receiver}"