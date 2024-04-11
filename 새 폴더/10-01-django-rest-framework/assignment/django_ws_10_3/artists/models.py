from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    agency = models.TextField()
    debut_date = models.DateField()
    is_group = models.BooleanField()