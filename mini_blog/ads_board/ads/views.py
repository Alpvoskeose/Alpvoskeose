from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Ad
from .forms import AdForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def home(request):
    # Получаем все объявления и выводим последние 8
    ads = Ad.objects.order_by('-created_at')[:8]
    return render(request, 'ads/home.html', {'ads': ads})

def add_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после добавления
    else:
        form = AdForm()
    return render(request, 'ads/add_ad.html', {'form': form})

def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную после сохранения
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})

def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    if request.method == 'POST':
        ad.delete()
        return redirect('home')  # Перенаправляем на главную страницу после удаления
    return render(request, 'ads/delete_ad.html', {'ad': ad})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)  # Получаем объявление по ID
    return render(request, 'ads/ad_detail.html', {'ad': ad})

# Декоратор для проверки, что пользователь авторизован и является суперпользователем
@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)  # Получаем объявление по ID
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу после сохранения
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad

# Декоратор для проверки, что пользователь авторизован и является суперпользователем
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)  # Получаем объявление по ID
    if request.method == 'POST':
        ad.delete()  # Удаляем объявление
        return redirect('home')  # Перенаправляем на главную страницу после удаления
    return render(request, 'ads/delete_ad.html', {'ad': ad})

# Представление для регистрации
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
            user.save()
            login(request, user)  # Вход пользователя после регистрации
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'ads/signup.html', {'form': form})

# Представление для входа (будет использовать стандартную форму Django)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'ads/login.html', {'form': form})