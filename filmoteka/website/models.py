from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=False)
    short_description = models.CharField(max_length=255, default='')
    time = models.CharField(max_length=10, default='')
    genre = models.CharField(max_length=255, default='')
    year = models.CharField(max_length=4, default='')
    premiere = models.CharField(max_length=255, default='')
    director = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    poster = models.CharField(max_length=255, default='')
    full_description = models.CharField(max_length=1024, default='')
    boxoffice = models.CharField(max_length=255, default='')
    budget = models.CharField(max_length=255, default='')
    distribution = models.CharField(max_length=255, default='')
    studio = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title.lower()

    def directors_as_list(self):
        return self.director.split(',')

    def genres_as_list(self):
        return self.genre.split(',')

    def countries_as_list(self):
        return self.country.split(',')

    def boxoffice_as_list(self):
        return self.boxoffice.split(',')

    def studios_as_list(self):
        return self.studio.split(',')

# Create your models here.
