from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница
def index(request):
    return redirect('threads_list')

# Список всех Thread
def threads_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads_list')
    else:
        form = ThreadForm()
    return render(request, 'threads_list.html', {'threads': threads, 'form': form})

# Детали конкретного Thread
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm(initial={'thread': thread})
    return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление Thread
def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads_list')

# Редактирование Thread
def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread_edit.html', {'form': form, 'thread': thread})

# Удаление Post
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование Post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})
