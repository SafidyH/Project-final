from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from .views import profil
from django_comments_xtd import comments
#from django.contrib.comments.views import (
#    comments, comment_flag, comment_like, comment_approve
#)

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('publications/', views.publication_list, name='publication_list'),
    path('tarifs/', views.tarif_list, name='tarif_list'),
    path('messages/', views.message_list, name='message_list'),
    path('commentaires/', views.comment_list, name='comment_list'),
    #path('comments/', comments, name='comments'),
    #path('comments/flag/<int:comment_id>/', comment_flag, name='comment_flag'),
    #path('comments/like/<int:comment_id>/', comment_like, name='comment_like'),
    #path('comments/approve/<int:comment_id>/', comment_approve, name='comment_approve'),
    path('comments/', comments.comment, name='comments-xtd'),
    path('comments/flag/<int:comment_id>/', comments.flag, name='comments-flag'),
    path('comments/like/<int:comment_id>/', comments.like, name='comments-like'),
    path('comments/approve/<int:comment_id>/', comments.approve, name='comments-approve'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'), #profil.as_view(template_name='registration/register.html'), name='register'
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    # Ajoutez d'autres URL pour vos vues ici
]