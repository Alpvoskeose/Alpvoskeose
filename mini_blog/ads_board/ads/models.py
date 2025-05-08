from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100)  # Название объявления
    description = models.TextField()          # Описание объявления
    contact = models.CharField(max_length=100)  # Контактные данные (например, телефон)
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True)  # Изображение
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

