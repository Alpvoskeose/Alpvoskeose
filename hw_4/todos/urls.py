from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-lists/', views.todo_lists, name='todo_lists'),
    path('todo-lists/create/', views.create_todo_list, name='create_todo_list'),
    path('todo-lists/<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:pk>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todo-lists/<int:pk>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todos/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
    path('todos/<int:pk>/edit/', views.edit_todo, name='edit_todo'),
]
