from django.contrib.auth.forms import UserCreationForm
from django import forms

class OwnerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    # Ajoutez des champs spécifiques pour les propriétaires (nom, prénom, etc.)

    class Meta:
        model = User  # Assurez-vous d'utiliser votre modèle User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class ProviderSignUpForm(UserCreationForm):
    skills = forms.CharField(max_length=100)
    experience = forms.IntegerField()
    # Ajoutez d'autres champs spécifiques pour les prestataires

    class Meta:
        model = User  # Assurez-vous d'utiliser votre modèle User
        fields = ('username', 'skills', 'experience', 'password1', 'password2')
    # Ajoutez des champs spécifiques pour les prestataires (compétences, expérience, etc.)
