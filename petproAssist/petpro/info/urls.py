from django.urls import path
from . import views

app_name = 'petpro'  # Remplacez 'votre_app' par le nom de votre application

urlpatterns = [
    path('signup_owner/', views.signup_owner, name='signup_owner'),
    path('signup_provider/', views.signup_provider, name='signup_provider'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # ... Ajoutez d'autres URL ici
]
