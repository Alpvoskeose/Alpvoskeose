from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

# Получить список задач
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Получить задачу по id
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return redirect('todo_list')  # Перенаправляем на список задач
