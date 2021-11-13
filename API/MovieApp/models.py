from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Movies(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Release = models.DateField()
    Plot = models.CharField(max_length=1000)
    Poster = models.CharField(max_length=1000)

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Ratings(models.Model):
    Id = models.AutoField(primary_key=True)
    Rating = models.IntegerField()
    Date = models.DateField()
    Comment = models.CharField(max_length=500)
    Movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
