from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    producer = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
