from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.TextField(max_length=10)
    author = models.TextField()
    title = models.TextField()
