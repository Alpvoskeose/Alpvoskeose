from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Post
from django.views import View
from django.forms import Form, CharField, Textarea

# Формы
class PostForm(Form):
    title = CharField(max_length=255)
    description = CharField(widget=Textarea)
    author = CharField(max_length=100)

# Список всех постов
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        data = [{'id': post.id, 'title': post.title, 'author': post.author} for post in posts]
        return JsonResponse(data, safe=False)

# Получение поста по id
class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        data = {'id': post.id, 'title': post.title, 'description': post.description, 'author': post.author}
        return JsonResponse(data)

# Создание нового поста
@csrf_exempt
class PostCreateView(View):
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                author=form.cleaned_data['author']
            )
            return JsonResponse({'id': post.id, 'title': post.title}, status=201)
        return JsonResponse({'error': 'Invalid data'}, status=400)

# Удаление поста
@csrf_exempt
class PostDeleteView(View):
    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully'})

