from django.shortcuts import render,redirect
from .models import Profile, Image, Comment
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PostPictureForm
# Create your views here.

def welcome(request):
    return render(request,"base.html")

@login_required(login_url='/accounts/login/')
def home(request):
    posts = Image.get_all()
    
    return render(request, 'index.html', { 'posts': posts })

def post(request):
    posts = Image.get_all()
    
    return render(request, 'index.html', { 'posts': posts})




def image_form(request):
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            form.save()
            return redirect('welcome') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 


