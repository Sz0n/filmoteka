import urllib.parse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .models import Movie
from .modules.scraping_logic import Scrape
from difflib import SequenceMatcher


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


def main(request):
    template_name = 'main.html'

    if 'search_bar' in request.POST:
        return search_bar(request)

    return render(request, template_name, {})


def show_movie(request, title):
    template_name = 'show_movie.html'

    founded_film = Movie.objects.get(title__iexact=urllib.parse.unquote(title))

    return render(request, template_name, {'movie': founded_film})


def search_bar(request):
    search_phrase = request.POST["search_bar"]
    if not len(search_phrase) > 0:
        request.session['wanted'] = None
    else:
        request.session['wanted'] = search_phrase
    return redirect('movies_list')


def movies_list(request):
    template_name = 'movie_list.html'
    wanted = request.session.get('wanted')
    all_movies = Movie.objects.all()

    search_result = []
    try:
        genre = request.GET.get('movie_genre')
        if genre is None:
            search_result = list(Movie.objects.filter(title__contains=wanted))
            search_genre = list(Movie.objects.filter(genre__contains=wanted))
            if len(search_result) < len(search_genre):
                search_result = search_genre
                messages.info(request, 'Wyniki dla: ' + wanted)
            elif not len(search_result) > 0:
                for a in all_movies:
                    if SequenceMatcher(None, a.title, wanted.title()).ratio() > 0.5:
                        search_result.append(a)
                if not len(search_result) > 0:
                    messages.warning(request, 'Brak wyników dla: ' + wanted)
                else:
                    messages.info(request, 'Wyniki dla: ' + wanted)
            else:
                messages.info(request, 'Wyniki dla: ' + wanted)

        else:
            search_result = list(Movie.objects.filter(genre__contains=genre))
            messages.info(request, 'Wyniki dla: ' + genre)
    except Exception as e:
        print(e)
        messages.warning(request, "Cos poszło nie takk.. :c")
    return render(request, template_name, {'search_result': search_result})
