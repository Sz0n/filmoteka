from django.urls import path
from .views import FillDB, main, show_movie, movies_list, favourites

urlpatterns = [
    path('', main, name='home'),
    path('fill_db/', FillDB.as_view(), name='fill_db'),
    path('movies', movies_list, name='movies_list'),
    path('movies/<str:title>', show_movie, name='show_movie'),
    path('favourites', favourites, name='favourites')
]
