from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Profile, Image, Comment
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ImageForm, CommentForm, ProfileForm

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    all_comments = Comment.objects.all()
    all_profiles = Profile.objects.all()
    return render(request, 'index.html',{'images': images, 'all_comments': all_comments, 'all_profiles' : all_profiles})

# Message
def messages(request):
    return render(request, 'main/messages.html',{ 'images': images})

@login_required(login_url='/accounts/login/')
def get_comments(request,comments):
    images = Image.objects.filter(comments__comment = comments)
    all_comments = Comment.objects.all()
    form = CommentForm()
    message = f"{comments}"
    return render(request, 'comments.html', {"message":message, "images":images, 'all_categories': all_comments, 'form' : form})

# Search function
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_user = Profile.search_by_username(search_term)
        message = f"{search_term}"
        context = {
            'message': message,
            'searched_user': searched_user
        }
        return render(request, 'search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})
