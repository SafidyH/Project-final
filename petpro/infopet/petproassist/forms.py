from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Animal,Publication, Comment

class RegistrationForm(UserCreationForm):
    animals = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_owner', 'last_name', 'first_name', 'animals' ,'address','tel' ,'comment']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        user.animals.set(self.cleaned_data['animals'])  # Set the many-to-many relationship after user is saved
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser

class UpdateUserForm(forms.ModelForm):
    animals = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'animals' ,'address','tel' ,'comment']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']