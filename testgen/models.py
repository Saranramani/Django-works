from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
