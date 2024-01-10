from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile_authors

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BioForm(forms.ModelForm):
    class Meta:
        model = Profile_authors
        fields = ['bio']
        labels = {'bio': 'Bio'}

class ProfileConfirmationForm(forms.ModelForm):
    class Meta:
        model = Profile_authors
        fields = ['confirmation']