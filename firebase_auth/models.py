# """Declare models for YOUR_APP app."""

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) 

class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)