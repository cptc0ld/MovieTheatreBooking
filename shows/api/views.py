from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Shows
from .serializers import ShowSerializer


class ViewShows(APIView):

    def get(self, request, format=None):
        shows = Shows.objects.all()
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)
