from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def home(request):
    return redirect('todo_lists')

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists})

def todo_list_detail(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    todos = todo_list.todos.all()
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def delete_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', pk=todo_list.pk)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'todos/create_todo_list.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list_detail', pk=todo.todo_list.pk)

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', pk=todo.todo_list.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})
