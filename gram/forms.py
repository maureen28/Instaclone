from django import forms
from .models import Image, Profile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# To handle the creation of new users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Upload/ post
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption',
                   'my_image']


# Commentform
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comments']

# profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio',
                  'profile_pic']



class MessageForm(forms.Form):
    subject = forms.CharField(max_length=100)
    To = forms.CharField(max_length=100)
