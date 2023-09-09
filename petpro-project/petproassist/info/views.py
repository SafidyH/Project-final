#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, CustomAuthenticationForm, ProfilForm, PublicationForm, TarifForm, MessageForm, CommentForm, PublicationSearchForm #UserLoginForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Profil, Publication, Tarif, Message, Comment  # Import modèle de profil
from django.db.models import Q
import json
from django.conf import settings
from django.contrib.auth.models import User
#from django.http import HttpResponseForbidden

#def some_view(request):
 #   if not user_has_permission(request.user):
  #      return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    # Code de la vue

# from .forms import CustomAuthenticationForm

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

@login_required
def profil(request):
    # Récupérez l'utilisateur connecté et son profil
    user = request.user
    profile = user.userprofile
    
    if not profil.profile_completed:
        return redirect('edit_profile')  # Rediriger vers la page d'édition du profil si le profil n'est pas complet

    # Affichez d'autres informations de profil si nécessaire
    return render(request, 'profil.html', {'user': user, 'profile': profile})

def register(request):
    profil = None
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profil = ProfilForm(request.POST, request.FILES)
        if form.is_valid() and profil.is_valid(): #and profil.is_valid() / j'ai remodifier
            user = form.save()
            profil = profil.save(commit=False) #commit=False
            profil.user = user
            profil.save()
            login(request, user)
            return redirect('profil')
    else:
        form = UserRegistrationForm()
        profil = ProfilForm()  #j'ai rajouté
    return render(request, 'register.html', {'form': form, 'profil' : profil})

#def register(request):
 #   profil = None
  #  if request.method == 'POST':
   #     form = UserRegistrationForm(request.POST)
#        profil = Profil(request.POST, request.FILES)
 #       if form.is_valid() : #and profil.is_valid()
  #          user = form.save()
   #         profil = profil.save() #commit=False
    #        profil.user = user
     #       profil.save()
      #      login(request, user)
 #           return redirect('profil')
  #  else:
   #     form = UserRegistrationForm()
    #return render(request, 'register.html', {'form': form, 'profil' : profil}) 

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

@permission_required #('nom_de_permission')
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            # Essayez d'abord l'authentification par e-mail
            user = form.get_user()
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

    return render(request, 'login.html', {'form': form})

#def profil(request):
    # Afficher le profil de l'utilisateur connecté
    #return render(request, 'profil.html')



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

@login_required
def dashboard(request):
    # Afficher les publications des utilisateurs
    publications = Publication.objects.all()
    
    # Afficher les tarifs des utilisateurs
    tarifs = Tarif.objects.all()

    # Afficher les messages privés de l'utilisateur actuel
    user_messages = Message.objects.filter(receiver=request.user)

    # Gérer les actions de l'utilisateur (par exemple, création de publications)
    if request.method == 'POST':
        if 'publication' in request.POST:
            publication_form = PublicationForm(request.POST)
            if publication_form.is_valid():
                new_publication = publication_form.save(commit=False)
                new_publication.user = request.user
                new_publication.save()
                return redirect('dashboard')
            
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = request.user
                publication_id = request.POST.get('publication_id')
                # Vous devrez peut-être obtenir la publication associée au commentaire
                # et l'assigner ici.
                try:
            # Obtenez la publication associée à l'ID
                    publication = Publication.objects.get(id=publication_id)
                    new_comment.publication = publication
                except Publication.DoesNotExist:
            # Gérez l'erreur si la publication n'existe pas
                    pass

                new_comment.save()
                return redirect('dashboard')

        if 'message' in request.POST:
            message_form = MessageForm(request.POST)
            if message_form.is_valid():
                new_message = message_form.save(commit=False)
                new_message.sender = request.user
                new_message.receiver = User.objects.get(username=request.POST['receiver_username'])
                new_message.save()
                return redirect('dashboard')
            
        if 'tarif' in request.POST:
            tarif_form = TarifForm(request.POST)
            if tarif_form.is_valid():
                tarif = tarif_form.save(commit=False)
                tarif.user = request.user
                tarif.save()
                return redirect('dashboard')
        # Ajoutez d'autres actions utilisateur ici (par exemple, création de tarifs, commentaires, etc.)

    else:
        publication_form = PublicationForm()
        message_form = MessageForm()
        tarif_form = TarifForm()
        comment_form = CommentForm() 
        # Ajoutez d'autres formulaires ici (par exemple, formulaire de tarifs, commentaires, etc.)

    # Créez un formulaire de recherche dans les publications
    search_form = PublicationSearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        publications = Publication.objects.filter(content__icontains=search_query)

    return render(request, 'dashboard.html', {
        'publications': publications,
        'tarifs': tarifs,
        'user_messages': user_messages,
        'publication_form': publication_form,
        'message_form': message_form,
        'search_form': search_form,
        'tarif_form': tarif_form,
        'comment_form': comment_form,  # Ajoutez le formulaire de tarif à la contexte
        'search_form': search_form,
    })

@login_required
def view_publication(request, publication_id):
    # Afficher une publication spécifique et ses commentaires
    publication = Publication.objects.get(id=publication_id)
    comments = Comment.objects.filter(publication=publication)
    comment_form = CommentForm()

    # Gérer les commentaires de l'utilisateur sur la publication
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.publication = publication
            new_comment.save()
            return redirect('view_publication', publication_id=publication.id)

    return render(request, 'view_publication.html', {
        'publication': publication,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def view_comments(request, publication_id):
    # Afficher les commentaires d'une publication spécifique
    publication = Publication.objects.get(id=publication_id)
    comments = Comment.objects.filter(publication=publication)
    comment_form = CommentForm()

    # Gérer les commentaires de l'utilisateur sur la publication
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.publication = publication
            new_comment.save()
            #messages.success(request, 'Votre commentaire a été publié avec succès.')

            return redirect('view_comments', publication_id=publication.id)

    return render(request, 'comments/view_comments.html', {
        'publication': publication,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def view_tarifs(request):
    # Afficher les tarifs des utilisateurs
    tarifs = Tarif.objects.all()
    return render(request, 'view_tarifs.html', {'tarifs': tarifs})

@login_required
def create_tarif(request):
    if request.method == 'POST':
        tarif_form = TarifForm(request.POST)
        if tarif_form.is_valid():
            tarif = tarif_form.save(commit=False)
            tarif.user = request.user
            tarif.save()
            return redirect('view_tarifs')  # Redirigez l'utilisateur vers la liste des tarifs après la création

    else:
        tarif_form = TarifForm()

    return render(request, 'create_tarif.html', {'tarif_form': tarif_form})

@login_required
def view_messages(request):
    # Afficher les messages privés de l'utilisateur actuel
    user_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'view_messages.html', {'user_messages': user_messages})

@login_required
def view_message_detail(request, message_id):
    # Afficher le détail d'un message privé spécifique
    message = Message.objects.get(id=message_id)
    return render(request, 'view_message_detail.html', {'message': message})

def lire_donnees_json():
    chemin_fichier_json = settings.JSON_DATA_FILE

    with open(chemin_fichier_json, 'r') as fichier_json:
        donnees = json.load(fichier_json)

    return donnees