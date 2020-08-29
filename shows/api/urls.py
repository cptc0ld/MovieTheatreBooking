from django.urls import path
from .views import ViewShows

urlpatterns = [
    path('shows/', ViewShows.as_view()),

]
