from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    date_of_birth=models.DateTimeField()
    email=models.CharField(max_length=1000)
    phone_number=PhoneNumberField(blank=True)

