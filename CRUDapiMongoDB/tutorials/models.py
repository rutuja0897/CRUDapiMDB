from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    summary = models.CharField(max_length=1000)
