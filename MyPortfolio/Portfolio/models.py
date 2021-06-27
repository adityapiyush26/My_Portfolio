from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200, unique=True)
    message = models.TextField(max_length=400)
