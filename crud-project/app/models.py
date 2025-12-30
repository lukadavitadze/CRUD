from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=150)
    gmail = models.CharField(max_length=200)
    time = models.CharField(max_length=10)