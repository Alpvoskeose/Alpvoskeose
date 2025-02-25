from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.list_posts, name='list_posts'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:id>/', views.post_detil, name='post_detail'),
]
