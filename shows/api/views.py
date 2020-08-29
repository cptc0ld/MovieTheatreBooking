from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Shows
from .serializers import ShowSerializer


class ViewShows(APIView):

    def get(self, request, format=None):
        if(request.query_params["all"] == "true"):
            shows = Shows.objects.all()
            serializers = ShowSerializer(shows, many=True)
            return Response(serializers.data)
        try:
            time = request.query_params["time"]
            date = request.query_params["date"]
            shows = Shows.objects.filter(StartTime=time).filter(Date=date)
        except:
            shows = {
                'message': "Fields Missing..."
            }
            return Response(shows)
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)
