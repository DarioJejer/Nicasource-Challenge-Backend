from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from MovieApp.models import Movies, Ratings

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movies
        fields = ('Id',
        'Title',
        'Release',
        'Plot')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('Id',
        'Rating',
        'Comment')