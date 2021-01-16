from django.urls import path
from .views import HomeView, FillDB

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fill_db/', FillDB.as_view(), name='fill_db'),
]
