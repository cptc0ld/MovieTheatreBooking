from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Shows
from .serializers import ShowSerializer
import datetime
from datetime import timezone


class ViewShows(APIView):

    def get(self, request, format=None):
        if(request.query_params["all"] == "true"):
            shows = Shows.objects.all()
            serializers = ShowSerializer(shows, many=True)
            return Response(serializers.data)
        try:
            time = request.query_params["time"]
            date_time_obj = datetime.datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
            shows = Shows.objects.filter(StartTime=time)
        except:
            shows = {
                'message': "Fields Missing..."
            }
            return Response(shows)
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)


class checkExpired(APIView):

    def get(self, request, format=None):
        shows = Shows.objects.all()
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)

    def put(self, request, format=None):
        shows = Shows.objects.filter(IsExpired=False)
        for show in shows:
            time = show.StartTime

            currenttime = datetime.datetime.utcnow()
            utc_time = currenttime.replace(tzinfo=timezone.utc)

            if(utc_time - time >= datetime.timedelta(hours=8, minutes=0)):
                show.IsExpired = True
                show.save()
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)

    def delete(self, request, format=None):
        shows = Shows.objects.filter(IsExpired=True)
        for show in shows:
            show.delete()
        shows = Shows.objects.all()
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)
