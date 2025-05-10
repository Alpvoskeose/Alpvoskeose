from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User  # Добавляем импорт User


class Ad(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)  # Краткое описание
    description = models.TextField()  # Полное описание
    contact = models.CharField(max_length=255, blank=True, null=True)  # Контактная информация
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True)  # Фото
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, который оставил комментарий
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)  # Объявление, к которому относится комментарий
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментария

    def __str__(self):
        return f'Комментарий от {self.user.username} к {self.ad.title}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Кастомная форма для регистрации
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label=_("Имя пользователя"),
        help_text=_("Не больше 150 символов. Только буквы, цифры и символы @/./+/-/_")
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label=_("Пароль"),
        help_text=_("Пароль должен содержать минимум 8 символов.")
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label=_("Подтверждение пароля"),
        help_text=_("Введите тот же пароль, что и выше, для подтверждения.")
    )
