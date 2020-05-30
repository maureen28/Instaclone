from django import forms
from .models import Image,Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# To handle the creation of new users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                   'password2']
# Upload/ post


# Commentform
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

# profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio',
                  'profile_pics']