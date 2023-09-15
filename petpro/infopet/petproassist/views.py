from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .models import CustomUser , Publication
from .forms import UpdateUserForm , PublicationForm, CommentForm

from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect, render

class HomePageView(TemplateView):
    template_name = 'home.html'

def home_view(request):
    publications = Publication.objects.all()
    return render(request, 'home.html', {'publications': publications})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('home')

    # Specify the URL parameter name for the user's PK
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        # Customize the queryset to return only the user who is currently logged in
        return CustomUser.objects.filter(pk=self.request.user.pk)

def profile_view(request, username):
    user = CustomUser.objects.get(username=username)
    publications = user.publications.all()
    return render(request, 'profile.html', {'user': user, 'publications': publications})

# def publication_detail_view(request, pk):
#     publication = Publication.objects.get(pk=pk)
#     comments = publication.comments.all()
#     comment_form = CommentForm()

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.publication = publication
#             comment.user = request.user
#             comment.save()
#             return redirect('publication_detail', pk=pk)
        
#     return render(request, 'publication_detail.html', {'publication': publication, 'comments': comments, 'comment_form': comment_form})

class CreatePublicationView(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication_form.html'
    success_url = reverse_lazy('home') 
    
    def form_valid(self, form):
        # Associate the publication with the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the publication detail view after successful publication creation
        # return reverse_lazy('profile', kwargs={'username': self.request.user.username})
        return reverse_lazy('home')
    
    
def create_comment(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    comments = publication.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.publication = publication
            comment.save()
            # return redirect('publication_detail', pk=publication.pk)  # Redirect to the publication detail view
            return redirect('create_comment', pk=publication.pk)
    else:
        form = CommentForm()

    return render(request, 'create_comment.html', {'form': form , 'publication': publication , 'comments': comments})

def list_publications(request):
    publications = Publication.objects.all()
    return render(request, 'publication_list.html', {'publications': publications})

def publication_detail_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    comments = publication.comments.all()
    return render(request, 'publication_detail.html', {'publication': publication, 'comments': comments})