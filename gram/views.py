from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Image, Comment
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ImageForm, ProfileForm, CommentForm, MessageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    all_comments = Comment.objects.all()
    all_profiles = Profile.objects.all()
    return render(request, 'index.html',{'images': images, 'all_comments': all_comments, 'all_profiles' : all_profiles})


# Explore
@login_required(login_url='/accounts/login/')
def explore(request):
    images = Image.objects.all()
    all_profiles = Profile.objects.all()
    return render(request, 'main/explore.html',{'images': images,'all_profiles' : all_profiles })

# Message
@login_required(login_url='/accounts/login/')
def messages(request):
    images = Image.objects.all()
    messageform = MessageForm()
    return render(request, 'main/messages.html',{'images': images, 'messageform':messageform})

@login_required(login_url='/accounts/login/')
def comments(request):
    images = Image.objects.all()
    form = CommentForm()
    return render(request, 'main/comments.html', {"form":form})

# Search function
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_username = Image.search_by_profile(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categorys": searched_username})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{ 'message': message})

# profile form
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'registration/login.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'registration/regisration_form.html')


def logout_view(request):
    logout(request)

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return render(request, 'registration/login.html')
