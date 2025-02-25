from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=225)
    picture = models.FileField(upload_to='images/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thered = models.ForeignKey(Thread, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title