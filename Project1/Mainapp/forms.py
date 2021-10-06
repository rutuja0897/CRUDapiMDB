#from django.forms import ModelForm
#from .models import *
from django import forms
import phonenumbers
#from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class UserRegistrationForm(forms.ModelForm):
    #phone_number=forms.IntegerField(required=True)
    phone_number=PhoneNumberField()

    class Meta:
        model=User
        fields="__all__"

    def clean_phone(self):
        phone_number=self.cleaned_data.get("phone_number")
        z= phonenumbers.parse(phone_number,"SG")
        if not phonenumbers.is_valid_number(z):
            raise forms.ValidationError("Number not in SG format")
        return phone_number
