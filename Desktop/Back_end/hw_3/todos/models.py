from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)  # Заголовок задачи
    description = models.TextField()  # Описание задачи
    due_date = models.DateField()  # Срок выполнения
    status = models.BooleanField(default=False)  # Статус (выполнено/не выполнено)

    def __str__(self):
        return self.title
