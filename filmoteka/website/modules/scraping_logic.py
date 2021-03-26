import requests
import bs4


class Scrape:

    @staticmethod
    def scrape_urls():

        base_url = 'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page='

        movies_url = []
        for page_num in range(11):
            req = requests.get(base_url + str(page_num))
            soup = bs4.BeautifulSoup(req.text, 'html.parser')
            for films in soup.findAll('div', 'filmPreview__card'):
                movies_url.append(films.find(class_='filmPreview__link').get('href'))

        return movies_url

    @staticmethod
    def scrape_movie(movie_url):
        movie = []

        req = requests.get('https://www.filmweb.pl' + movie_url)
        soup = bs4.BeautifulSoup(req.text, 'html5lib')

        title = soup.find('h1', itemprop="name")\
            .find('span')

        year = soup.find('span', class_="filmCoverSection__year")

        duration = soup.find('span', class_='filmCoverSection__filmTime')\
            .get('data-duration')

        short_description = soup.find('div', class_='filmPosterSection__plot')

        genres = soup.find('div', class_='filmPosterSection__info filmInfo')\
            .find('div', class_='filmInfo__info')\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")\
            .findAll('a')

        premiere = soup.find('div', class_='filmPosterSection__info filmInfo')\
            .find('div', class_='filmInfo__info')\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")

        directors = soup.findAll('a', itemprop="director")

        countries = soup.find('div', class_='filmPosterSection__info filmInfo')\
            .find('div', class_='filmInfo__info')\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")\
            .find_next_sibling('div', class_="filmInfo__info")\
            .findAll('a', href=True)

        poster = soup.find('div', class_='page__group')\
            .find_next_sibling('div', class_='page__group')\
            .find('a', class_='filmPosterSection__link')\
            .find('img')\
            .get('content')

        full_description = soup.find('div', attrs={'class': 'page__group', 'data-group': 'g9'})\
            .find('span', class_='descriptionSection__moreText')
        if full_description is None:
            full_description = soup.find('div', attrs={'class': 'page__group', 'data-group': 'g9'})\
                .find('p', class_='descriptionSection__text')

        try:
            boxoffice = soup.find('div', class_="filmOtherInfoSection__group")\
                .find_next('div', class_="filmInfo__group")\
                .find_next('div', class_='boxoffice')\
                .find_parent('div')
        except AttributeError:
            boxoffice = ''

        try:
            budget = soup.find(text='budżet').next_element.text
        except AttributeError:
            budget = ''

        try:
            distribution = soup.find(text='dystrybucja').next_element.text
        except AttributeError:
            distribution = ''

        try:
            studio_link = soup.find(text='studio')\
                .next_element\
                .find('a', href=True)\
                .get('href')

            req_studio_link = requests.get("https://www.filmweb.pl" + studio_link)

            soup_studio_link = bs4.BeautifulSoup(req_studio_link.text, 'html.parser')

            studios = soup_studio_link.find('ul', class_='filmStudiosSection__list')\
                .findAll('div', class_='filmStudiosSection__title')

            studio = (','.join(s.text for s in studios))
        except AttributeError:
            studios = soup.find(text='studio').next_element
            studio = studios.text.replace(' / ', ',')

        genre = (','.join(g.text for g in genres))
        director = (','.join(g.text for g in directors))
        country = (','.join(g.text for g in countries))
        boxoffice = (','.join(b.text for b in boxoffice))

        movie.append(title.text)
        movie.append(short_description.text)
        movie.append(duration)
        movie.append(genre)
        movie.append(year.text)
        movie.append(premiere.text.strip())
        movie.append(director.strip())
        movie.append(country)
        movie.append(poster)
        movie.append(full_description.text)
        movie.append(boxoffice)
        movie.append(budget)
        movie.append(distribution)
        movie.append(studio)

        return movie
