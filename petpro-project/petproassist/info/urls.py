from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profil

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('publications/', views.publication_list, name='publication_list'),
    path('tarifs/', views.tarif_list, name='tarif_list'),
    path('messages/', views.message_list, name='message_list'),
    path('commentaires/', views.comment_list, name='comment_list'),
    path('login/', views.login_view, name='login'),
    path('register/', profil.as_view(template_name='registration/register.html'), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    # Ajoutez d'autres URL pour vos vues ici
]