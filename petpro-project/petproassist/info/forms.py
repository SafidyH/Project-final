from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Proprietaire, Prestataire, Service, Animal
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=[('prestataire', 'Prestataire'), ('proprietaire', 'Propriétaire')], required=True, widget=forms.RadioSelect)

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

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    statut = forms.ChoiceField(choices=[('proprietaire', 'Propriétaire'), ('prestataire', 'Prestataire')])
    
    class Meta:
        model = User
        fields = ['nom', 'prenoms', 'email', 'statut', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)