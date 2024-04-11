from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length = 100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)

