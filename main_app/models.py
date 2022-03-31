from django.db import models

# Create your models here.
class Note(models.Model):
    title: models.CharField(max_length=100)
    text: models.CharField(max_length=300)
