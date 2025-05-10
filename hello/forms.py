from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ad



class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'short_description', 'description', 'contact', 'image']  # Поля для формы    
# Форма для регистрации пользователя
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Стандартные поля регистрации

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем placeholder для всех полей
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

# Форма для создания и редактирования объявления
class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'short_description', 'description', 'contact', 'image']  # Поля для создания и редактирования объявления
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок объявления'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание объявления'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем placeholder для всех полей формы
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
