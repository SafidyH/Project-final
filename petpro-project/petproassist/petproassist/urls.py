"""
URL configuration for petproassist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from info import views
#from django.contrib.comments.urls import urlpatterns as comments_urls
#from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django_comments_xtd import comments
#from django.contrib.comments import urls as comments_urls
#from django.contrib.comments.urls import CommentURLResolver
#from django.contrib.comments import urls as comments_urls

#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profil/', views.profil, name='profil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'), 
    path('comments/', include('django_comments_xtd.urls')),
    #path('comments/', include(comments_urls)),
    #path('comments/', CommentURLResolver()),
    #path('comments/', comments.comment, name='comments-xtd'),
    #path('comments/flag/<int:comment_id>/', comments.flag, name='comments-flag'),
    #path('comments/like/<int:comment_id>/', comments.like, name='comments-like'),
    #path('comments/approve/<int:comment_id>/', comments.approve, name='comments-approve'),
    url(r"", include("info.urls")),
]
