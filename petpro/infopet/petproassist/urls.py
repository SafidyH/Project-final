from django.urls import path
from . import views
from .views import home_view, HomePageView , UpdateUserView , CreatePublicationView, publication_detail_view, profile_view,create_comment , list_publications
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('publications/', list_publications, name='list_publications'),
    path('create-publication/', CreatePublicationView.as_view(), name='create_publication'),
    path('publication/<int:pk>/', publication_detail_view, name='publication_detail'),
    path('comment/<int:pk>/create/', create_comment, name='create_comment'),

]
