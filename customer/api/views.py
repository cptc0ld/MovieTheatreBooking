from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..models import Customer, Ticket
import shows.models as ShowModel
from .serializers import CustomerSerializer, TicketSerializer
import json
from datetime import datetime


class ViewCustomers(APIView):

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers, many=True)
        return Response(serializers.data)


class ViewCustomersbyTid(APIView):

    def get(self, request, tid, format=None):
        try:
            ticket = Ticket.objects.filter(TicketId=tid).get()
        except Ticket.DoesNotExist:
            return Response({
                "Message": "Wrong tid"
            })
        customers = Customer.objects.filter(id=ticket.CustomerId)
        serializers = CustomerSerializer(customers, many=True)
        return Response(serializers.data)


class TicketBooking(APIView):
    def get(self, request, format=None):

        time = request.query_params["time"]
        date_time_obj = datetime.strptime(
            time, '%H:%M:%S %Y-%m-%d')

        show = ShowModel.Shows.objects.filter(
            StartTime=date_time_obj).get().showid
        ticket = Ticket.objects.filter(ShowId=show)
        serializers = TicketSerializer(ticket, many=True)
        return Response(serializers.data)

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
        tempshow = ShowModel.Shows.objects.get(showid=show)
        tempshow.count -= 1
        tempshow.save()
        response = {
            'TicketId': NewTicket.TicketId
        }
        return Response(response)

    def delete(self, request, id, format=None):
        try:
            ticket = Ticket.objects.get(TicketId=id)
            show = ShowModel.Shows.objects.get(showid=ticket.ShowId)
            show.count += 1
            show.save()
        except Ticket.DoesNotExist:
            return Response({
                "Message": str(id) + " Does not Exist"
            })
        ticket.delete()

        return Response({
            "Message": "Deleted Ticket with Tid: " + str(id)
        })

    def put(self, request, id, format=None):
        time = request.data["time"]

        date_time_obj = datetime.strptime(
            time, '%H:%M:%S %Y-%m-%d')

        ticket = Ticket.objects.get(TicketId=id)
        show = ShowModel.Shows.objects.filter(
            showid=ticket.ShowId).get()
        show.StartTime = date_time_obj

        show.save()
        return Response({
            "Message": "Updated timing for this ticket to " + time
        })
