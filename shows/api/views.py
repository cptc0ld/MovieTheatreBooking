from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Shows
from .serializers import ShowSerializer
import datetime
from datetime import timezone


class CreateShows(APIView):

    def post(self, request, format=None):
        try:
            movie = request.data["moviename"]
            screen = request.data["screen"]
            dur = request.data["duration"]
            time = request.data["starttime"]
        except:
            shows = {
                'message': "all parameter required"
            }
            return Response(shows)
        try:
            date_time_obj = datetime.datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
        except:
            shows = {
                'message': "Enter Valid date time format(%H:%M:%S %Y-%m-%d)"
            }
            return Response(shows)
        try:
            show = Shows.objects.create(
                MovieName=movie, Screen=screen, Duration=dur, StartTime=date_time_obj)
            show.save()
        except:
            shows = {
                'message': "Unknown error"
            }
            return Response(shows)
        shows = Shows.objects.all()
        serializers = ShowSerializer(shows, many=True)
        return Response(serializers.data)


class ViewShows(APIView):

    def get(self, request, format=None):
        try:
            request.query_params["all"]
        except:
            shows = {
                'message': "all parameter required"
            }
            return Response(shows)
        if(request.query_params["all"] == "true"):
            shows = Shows.objects.all()
            serializers = ShowSerializer(shows, many=True)
            return Response(serializers.data)
        try:
            time = request.query_params["time"]
            date_time_obj = datetime.datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
        except:
            shows = {
                'message': "Enter Valid date time format(%H:%M:%S %Y-%m-%d)"
            }
            return Response(shows)
        try:
            shows = Shows.objects.filter(StartTime=date_time_obj)
        except:
            shows = {
                'message': "No shows available"
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
