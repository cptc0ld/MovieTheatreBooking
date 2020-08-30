from django.urls import path
from .views import ViewShows, checkExpired

urlpatterns = [
    path('shows/', ViewShows.as_view()),
    path('expired/', checkExpired.as_view()),
]
