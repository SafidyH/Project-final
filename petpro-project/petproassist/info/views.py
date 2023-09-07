#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import Profil  # Import modèle de profil
from django.db.models import Q
from .forms import CustomAuthenticationForm


@login_required #(login_url='/votre_page_de_connexion/')
def dashboard(request):
    search_term = request.GET.get('search', '')

    # Filtrer les profils par nom en utilisant Q objects pour rechercher de manière insensible à la casse
    profils = Profil.objects.filter(Q(user__username__icontains=search_term))

    return render(request, 'dashboard.html', {'profils': profils, 'search_term': search_term})

#@login_required
#def dashboard(request):
    # Récupérez tous les profils existants
 #   profils = Profil.objects.all()
    
  #  return render(request, 'dashboard.html', {'profils': profils})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profil = Profil(request.POST, request.FILES)
        if form.is_valid() and profil.is_valid():
            user = form.save()
            profil = profil.save(commit=False)
            profil.user = user
            profil.save()
            login(request, user)
            return redirect('profil')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form, 'profil' : profil})

#def login_view(request):
#    if request.method == 'POST':
 #       form = UserLoginForm(request.POST)
  #      if form.is_valid():
#            email = form.cleaned_data['email']
 #           password = form.cleaned_data['password']
  #          user = authenticate(request, email=email, password=password)
   #         if user is not None:
    #            login(request, user)
     #           return redirect('profil')
#    else:
 #       #form = UserLoginForm()
  #      form = CustomAuthenticationForm()
   # return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            # Essayez d'abord l'authentification par e-mail
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is None:
                # Si l'authentification par e-mail a échoué, essayez l'authentification par nom d'utilisateur
                username = form.cleaned_data['username']
                user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirigez l'utilisateur vers la page de profil après la connexion
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

#def profil(request):
    # Afficher le profil de l'utilisateur connecté
    #return render(request, 'profil.html')

@login_required
def profil(request):
    # Récupérez l'utilisateur connecté et son profil
    user = request.user
    profile = user.userprofile
    
    if not profil.profile_completed:
        return redirect('edit_profile')  # Rediriger vers la page d'édition du profil si le profil n'est pas complet

    # Affichez d'autres informations de profil si nécessaire
    return render(request, 'profil.html', {'user': user, 'profile': profile})

@login_required
def edit_profile(request):
    user = request.user
    profil = user.userprofile

    if request.method == 'POST':
        profil_form = Profil(request.POST, request.FILES, instance=profil)
        if profil_form.is_valid():
            profil_form.save()
            profil.profile_completed = True
            profil.save()
            return redirect('profile')  # Redirection vers la page de profil après l'édition du profil
    else:
        profil_form = Profil(instance=profil)

    return render(request, 'edit_profile.html', {'user': user, 'profil_form': profil_form})

def logout_view(request):
    logout(request)
    return redirect('login')