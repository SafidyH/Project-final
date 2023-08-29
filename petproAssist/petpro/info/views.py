#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
#from .forms import OwnerSignUpForm, ProviderSignUpForm

def signup_owner(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Custom logic for handling Owner registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup_owner.html', {'form': form})

def signup_provider(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Custom logic for handling ServiceProvider registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup_provider.html', {'form': form})

#def signup_owner_form(request):
 #   if request.method == 'POST':
 #       form = OwnerSignUpForm(request.POST)
  #      if form.is_valid():
   #         user = form.save()
            # Logique spécifique pour l'inscription des propriétaires
    #        return redirect('login')
 #   else:
  #      form = OwnerSignUpForm()
  #  return render(request, 'signup_owner.html', {'form': form})

#def signup_provider_form(request):
 #   if request.method == 'POST':
  #      form = ProviderSignUpForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
            # Logique spécifique pour l'inscription des prestataires
     #       return redirect('login')
 #   else:
  #      form = ProviderSignUpForm()
   # return render(request, 'signup_provider.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Votre template de page de connexion

# Create your views here.
