from django.contrib import admin
from .models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'contact')  # Поля для отображения в списке
    search_fields = ('title', 'description')  # Поля для поиска
    list_filter = ('created_at',)  # Фильтрация по дате
