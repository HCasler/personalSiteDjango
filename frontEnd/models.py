from django.db import models

# Create your models here.

class PageText(models.Model):
    name = models.CharField(max_length=254, unique=True)
    lastUpdated = models.DateTimeField(max_length=60000)
    text = models.TextField()
