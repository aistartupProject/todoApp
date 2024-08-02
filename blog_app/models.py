from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50, default='방문자')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__ (self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 임시
class Ice(models.Model):
    name = models.CharField(max_length=100)
    price = models.TextField()
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
