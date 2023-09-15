from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_owner = models.BooleanField(default=False)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    animals = models.ManyToManyField('Animal', blank=True)
    def __str__(self):
        return self.username

class Animal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publication(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='publications')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.TextField()
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.user.username} on {self.publication.title}"