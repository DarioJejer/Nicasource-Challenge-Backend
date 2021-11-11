from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Movies(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Release = models.DateField()
    Plot = models.CharField(max_length=1000)

class Ratings(models.Model):
    Id = models.AutoField(primary_key=True)
    Rating = models.IntegerField()
    Comment = models.CharField(max_length=500)
