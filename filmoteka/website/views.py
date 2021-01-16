from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from .models import Movie
from .modules.scraping_logic import Scrape


# Create your views here.
class FillDB(View):
    template_name = "main.html"

    def get(self, *args):
        sc = Scrape
        urls = sc.scrape_urls()
        try:
            for url in urls:
                movie = sc.scrape_movie(url)
                Movie.objects.create(title=movie[0], short_description=movie[1], time=movie[2], genre=movie[3],
                                     year=movie[4], premiere=movie[5], director=movie[6], country=movie[7],
                                     poster=movie[8],
                                     full_description=movie[9], boxoffice=movie[10], budget=movie[11],
                                     distribution=movie[12], studio=movie[13])
            messages.info(self.request, 'DB has been filled successfully')

        except Exception as e:
            print(type(e))
            print(e)
        messages.info(self.request, '"Filling DB failed"')

        return render(self.request, self.template_name, {})


class HomeView(View):
    template_name = "main.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})
