from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..models import Customer, Ticket
import shows.models as ShowModel
from .serializers import CustomerSerializer, TicketSerializer
import json


class ViewCustomers(APIView):

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers, many=True)
        return Response(serializers.data)


class TicketBooking(APIView):

    def post(self, request, format=None):
        # data = TicketSerializer(request.data, many=True)
        try:
            customerno = Customer.objects.filter(
                phone=request.data["phone"]).get().id
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                username=request.data["username"], phone=request.data["phone"])
            customerno = customer.phone

        show = ShowModel.Shows.objects.filter(
            MovieName=request.data["moviename"]).filter(StartTime=request.data["starttime"]).filter(Date=request.data["date"]).get().showid

        if(show == None):
            return Response('{"message": "no movie availabe"}')

        print(customerno)

        NewTicket = Ticket.objects.create(ShowId=show, CustomerId=customerno)
        NewTicket.save()
        response = {
            'TicketId': NewTicket.TicketId
        }
        return Response(response)
