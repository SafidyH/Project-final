from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Proprietaire, Prestataire, Service, Animal
from django.contrib.auth.forms import AuthenticationForm

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

