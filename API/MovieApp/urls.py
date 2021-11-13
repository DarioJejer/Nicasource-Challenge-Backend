from django.conf.urls import url
from MovieApp import views

urlpatterns=[
    url(r'^movie/$', views.movieApi),
    url(r'^movie/([0-9]+)$',views.movieApi),
    
    url(r'^rating/$', views.ratingApi),
    
    url(r'^user/$', views.userApi),
]