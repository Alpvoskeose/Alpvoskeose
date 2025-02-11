from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all().values('id', 'title', 'text', 'author')
    return JsonResponse(list(articles), safe=False)

def article_detail(request, id):
    article = Article.objects.filter(id=id).values('id', 'title', 'text', 'author').first()
    if article:
        return JsonResponse(article)
    return JsonResponse({'error': 'Article not found'}, status=404)
