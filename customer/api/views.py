from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        return Response(serializers.data, status=status.HTTP_200_OK)


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
        return Response(serializers.data, status=status.HTTP_200_OK)


class TicketBooking(APIView):
    def get(self, request, format=None):
        try:
            time = request.query_params["time"]
        except:
            response = {
                'Message': 'Enter time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            date_time_obj = datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
        except:
            response = {
                'Message': 'Enter valid time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            show = ShowModel.Shows.objects.filter(
                StartTime=date_time_obj).get().showid
        except:
            response = {
                'Message': 'No shows found'
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

        try:
            ticket = Ticket.objects.filter(ShowId=show)
            serializers = TicketSerializer(ticket, many=True)
            return Response(serializers.data)
        except:
            response = {
                'Message': 'No ticket found'
            }
            return Response(response)
        serializers = TicketSerializer(ticket, many=True)
        return Response(serializers.data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        # data = TicketSerializer(request.data, many=True)
        try:
            customerno = Customer.objects.filter(
                phone=request.data["phone"]).get().id
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                username=request.data["username"], phone=request.data["phone"])
            customer.save()
            customerno = customer.phone
        try:
            time = request.data["starttime"]
        except:
            response = {
                'Message': 'Enter time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_time_obj = datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
        except:
            response = {
                'Message': 'Enter valid time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            show = ShowModel.Shows.objects.filter(
                MovieName=request.data["moviename"]).filter(StartTime=date_time_obj).get().showid
        except:
            response = {
                'Message': 'No shows found'
            }
            return Response(response, status=status.HTTP_200_OK)
        if(show == None):
            return Response('{"message": "no movie availabe"}', status=status.HTTP_204_NO_CONTENT)

        print(customerno)

        tempshow = ShowModel.Shows.objects.get(showid=show)
        if(tempshow.count == 0):
            response = {
                'Message': 'All tickets booked'
            }
            return Response(response, status=status.HTTP_200_OK)

        tempshow.count -= 1
        tempshow.save()

        NewTicket = Ticket.objects.create(ShowId=show, CustomerId=customerno)
        NewTicket.save()

        response = {
            'TicketId': NewTicket.TicketId
        }
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        try:
            ticket = Ticket.objects.get(TicketId=id)
            show = ShowModel.Shows.objects.get(showid=ticket.ShowId)
            show.count += 1
            show.save()
        except (Ticket.DoesNotExist, ShowModel.Shows.DoesNotExist):
            return Response({
                "Message": str(id) + " Does not Exist"
            }, status=status.HTTP_400_BAD_REQUEST)
        ticket.delete()

        return Response({
            "Message": "Deleted Ticket with Tid: " + str(id)
        }, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        try:
            time = request.data["time"]
        except:
            response = {
                'Message': 'Enter time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_time_obj = datetime.strptime(
                time, '%H:%M:%S %Y-%m-%d')
        except:
            response = {
                'Message': 'Enter valid time'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            ticket = Ticket.objects.get(TicketId=id)

            show = ShowModel.Shows.objects.filter(
                showid=ticket.ShowId).get()
        except:
            response = {
                'Message': 'Ticket not found'
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        show.StartTime = date_time_obj

        show.save()
        return Response({
            "Message": "Updated timing for this ticket to " + time
        }, status=status.HTTP_200_OK)
