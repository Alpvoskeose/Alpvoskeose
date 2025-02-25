from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:list_posts')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list_posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})

@login_required
def post_detil(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST' and 'delete' in request.POST:
            post.delete()
            return redirect('posts:list_posts')
        
        if request.method == 'POST' and 'edit' in  request.POST:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:list_posts')
        
        else:
            form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form, 'post': post})
    
    return render(request, 'viev_post.html', {'post': post})