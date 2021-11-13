from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from MovieApp.models import Movies, Ratings, Users

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movies
        fields = ('Id',
        'Title',
        'Release',
        'Plot',
        'Poster')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('Id',
        'Rating',
        'Comment',
        'Date',
        'User',
        'Movie')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('Id',
        'Username',
        'Password',
        "IsAdmin")