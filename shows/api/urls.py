from django.urls import path
from .views import ViewShows, checkExpired, CreateShows

urlpatterns = [
    path('shows/', ViewShows.as_view(), name='shows'),
    path('addshows/', CreateShows.as_view(), name='addshows'),
    path('expired/', checkExpired.as_view(), name='expired'),
]
