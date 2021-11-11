import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MovieApp.models import Movies, Ratings
from MovieApp.serializers import MovieSerializer, RatingSerializer

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


