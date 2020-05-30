from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostPictureForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'image']
