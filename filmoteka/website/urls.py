from django.urls import path
from .views import HomeView, FillDB, show_movie

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fill_db/', FillDB.as_view(), name='fill_db'),
    path('movies/<str:title>', show_movie, name='show_movie'),
]
