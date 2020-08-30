import json
from django.urls import reverse
from customer.api.serializers import CustomerSerializer, TicketSerializer
from customer.models import Customer, Ticket
from shows.models import Shows
from rest_framework import status
from rest_framework.test import APITestCase
import datetime


class ViewShowTests(APITestCase):
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

    def test_view_show(self):
        url = reverse('shows')

        response = self.client.get(url + '?all=true')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(url + '?all=false&time=' + self.time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_expired(self):
        url = reverse('expired')

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
