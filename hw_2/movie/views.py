from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().values('id', 'title', 'description', 'producer', 'duration')
    return JsonResponse(list(movies), safe=False)

def movie_detail(request, id):
    movie = Movie.objects.filter(id=id).values('id', 'title', 'description', 'producer', 'duration').first()
    if movie:
        return JsonResponse(movie)
    return JsonResponse({'error': 'Movie not found'}, status=404)
