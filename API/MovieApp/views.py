import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MovieApp.models import Movies, Ratings, Users
from MovieApp.serializers import MovieSerializer, RatingSerializer, UserSerializer

# Create your views here.
@csrf_exempt
def movieApi(request, id=0):
    if request.method == 'GET':
        movies = Movies.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)

    elif request.method == 'POST':
        movie_data=JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie=Movies.objects.get(Id=movie_data['Id'])
        movie_serializer = MovieSerializer(movie,data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        movie=Movies.objects.get(Id=id)
        movie.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def ratingApi(request, id=0):
    if request.method == 'GET':
        ratings = Ratings.objects.all()
        ratings_serializer = RatingSerializer(ratings, many=True)
        return JsonResponse(ratings_serializer.data, safe=False)

    elif request.method == 'POST':
        ratings_data=JSONParser().parse(request)
        ratings_serializer = RatingSerializer(data=ratings_data)
        if ratings_serializer.is_valid():
            ratings_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        ratings_data = JSONParser().parse(request)
        ratings=Ratings.objects.get(Id=ratings_data['Id'])
        ratings_serializer = RatingSerializer(ratings,data=ratings_data)
        if ratings_serializer.is_valid():
            ratings_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        ratings=Ratings.objects.get(Id=id)
        ratings.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        users_data=JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users=Users.objects.get(Id=users_data['Id'])
        users_serializer = UserSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        users=Users.objects.get(Id=id)
        users.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

