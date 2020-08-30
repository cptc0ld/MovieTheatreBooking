import json
from django.urls import reverse
from customer.api.serializers import CustomerSerializer, TicketSerializer
from customer.models import Customer, Ticket
from shows.models import Shows
from rest_framework import status
from rest_framework.test import APITestCase
import datetime


class ViewCustomerTests(APITestCase):
    time = "00:00:00 2021-12-12"
    customerno = '+910000000000'
    moviename = "Test Movie"
    username = "Test User"

    def setUp(self):

        date_time_obj = datetime.datetime.strptime(
            self.time, '%H:%M:%S %Y-%m-%d')

        show = Shows.objects.create(
            MovieName=self.moviename, Screen="1", Duration="120", StartTime=date_time_obj)
        show.save()

        customer = Customer.objects.create(
            username=self.username, phone=self.customerno)
        customer.save()

        NewTicket = Ticket.objects.create(
            ShowId=show.showid, CustomerId=customer.id)
        NewTicket.save()

    def test_view_customers(self):
        url = reverse('customers')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_customer_by_id(self):
        ticket = Ticket.objects.all().first()
        url = reverse('customer', args=[str(ticket.TicketId)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_booking(self):
        url = reverse('tickets')
        response = self.client.get(url + '?time=' + self.time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {'phone': self.customerno,
                'username': self.username,
                'starttime': self.time,
                'moviename': self.moviename
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_with_id(self):
        ticket = Ticket.objects.all().first()
        url = reverse('ticket', args=[ticket.TicketId])
        data = {
            'time': "00:00:00 2022-12-12"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
