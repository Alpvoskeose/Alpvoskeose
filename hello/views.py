from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ad
from .forms import AdForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Ad, Comment
from .forms import CommentForm

@login_required
def add_comment(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment = Comment.objects.create(
                ad=ad,
                user=request.user,
                content=content
            )
            return redirect('ad_detail', pk=ad.id)  # Перенаправление на страницу объявления

    return HttpResponse("Ошибка при добавлении комментария", status=400)
@login_required
def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    comments = ad.comments.all()  # Получаем все комментарии для этого объявления

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ad = ad
            comment.user = request.user
            comment.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = CommentForm()

    return render(request, 'hello/ad_detail.html', {'ad': ad, 'comments': comments, 'form': form})
# Проверка, является ли пользователь суперпользователем
def is_superuser(user):
    return user.is_superuser

# Декоратор для суперпользователя
@user_passes_test(is_superuser)
@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  # Привязка объявления к пользователю
            ad.save()
            messages.success(request, 'Объявление успешно создано!')
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'hello/ad_create.html', {'form': form})
# Приветственная страница
def welcome(request):
    return render(request, 'hello/welcome.html')

# Страница регистрации
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно! Вы можете войти в свой аккаунт.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'hello/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление после успешного входа
            else:
                messages.error(request, 'Неверный логин или пароль!')
        else:
            messages.error(request, 'Ошибка при отправке формы')
    else:
        form = AuthenticationForm()

    return render(request, 'hello/login.html', {'form': form})
# Страница выхода
def logout_view(request):
    logout(request)
    return redirect('welcome')

# Главная страница с объявлениями
@login_required
def home(request):
    ads = Ad.objects.all()  # Получаем все объявления
    return render(request, 'hello/home.html', {'ads': ads})

# Создание нового объявления
@login_required


def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  # если нужно назначить текущего пользователя
            ad.save()
            return redirect('ad_list')  # Перенаправляем на страницу со списком студклубов
    else:
        form = AdForm()
    return render(request, 'hello/ad_create.html', {'form': form})

# Редактирование объявления
@login_required
def ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)  # Передаем текущие данные в форму
        if form.is_valid():
            form.save()
            return redirect('ad_list')  # Перенаправляем на страницу списка после успешного редактирования
    else:
        form = AdForm(instance=ad)  # При GET-запросе показываем форму с текущими данными
    
    return render(request, 'hello/ad_edit.html', {'form': form, 'ad': ad})


# Удаление объявления
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    
    if not ad.id:  # Проверка, что id существует
        messages.error(request, 'Объявление не найдено.')
        return redirect('ad_list')

    if request.user != ad.user:  # Проверка на права пользователя
        messages.error(request, 'У вас нет прав для удаления этого объявления.')
        return redirect('ad_list')

    ad.delete()
    messages.success(request, 'Объявление успешно удалено!')
    return redirect('ad_list')



# Страница списка всех объявлений
@login_required

def ad_list(request):
    ads = Ad.objects.all()  # Получаем все объявления
    return render(request, 'hello/ad_list.html', {'ads': ads})
