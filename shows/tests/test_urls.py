from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shows.api import views


class TestUrls(SimpleTestCase):

    def test_show_all_url(self):
        url = reverse('shows')
        self.assertEquals(resolve(url).func.view_class, views.ViewShows)

    def test_customer_url(self):
        url = reverse('expired')
        self.assertEquals(resolve(url).func.view_class,
                          views.checkExpired)
