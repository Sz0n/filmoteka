from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from .views import FillDB, HomeView


class TestUrls(SimpleTestCase):

    def test_fill_db_url(self):
        url = reverse('fill_db')
        self.assertEquals(resolve(url).func.view_class, FillDB)

    def test_main_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

# Create your tests here.
