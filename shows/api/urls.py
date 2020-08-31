from django.urls import path
from .views import ViewShows, checkExpired, CreateShows, Home

urlpatterns = [
    path('api/shows/', ViewShows.as_view(), name='shows'),
    path('api/addshows/', CreateShows.as_view(), name='addshows'),
    path('api/expired/', checkExpired.as_view(), name='expired'),
    path('', Home.as_view(), name='home')
]
