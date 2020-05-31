from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Profile, Image, Comment
from django.conf import settings
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
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_user = Image.search_by_name(search_term)
        message = f"{search_term}"
        context = {
            'message': message,
            'searched_user': searched_user
        }
        return render(request, 'search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})

# profile form
def image_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = ProfileForm()
    return render(request, 'main/image_form.html', {'form' : form})

