from django.db import models
import datetime

# Create your models here.
class Note(models.Model):
    title: models.CharField(max_length=100)
    text: models.CharField(max_length=300)
    created_at = models.DateTimeField(default= datetime.datetime.now())
   
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text