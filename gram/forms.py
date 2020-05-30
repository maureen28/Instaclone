from django import forms
from .models import Image, Profile, Comment
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
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'title',
                   'my_image']


# profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio',
                  'profile_pic']