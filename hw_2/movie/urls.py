from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:id>/', views.movie_detail, name='movie_detail'),
]
