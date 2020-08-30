from django.test import SimpleTestCase
from django.urls import resolve, reverse
from customer.api import views


class TestUrls(SimpleTestCase):

    def test_customers_all_url(self):
        url = reverse('customers')
        self.assertEquals(resolve(url).func.view_class, views.ViewCustomers)

    def test_customer_url(self):
        url = reverse('customer', args=[
                      '720dc4f5-1df2-4686-8f31-702aca10e9f9'])
        self.assertEquals(resolve(url).func.view_class,
                          views.ViewCustomersbyTid)

    def test_ticket_all_url(self):
        url = reverse('tickets')
        self.assertEquals(resolve(url).func.view_class, views.TicketBooking)

    def test_ticket_url(self):
        url = reverse('ticket', args=['720dc4f5-1df2-4686-8f31-702aca10e9f9'])
        self.assertEquals(resolve(url).func.view_class, views.TicketBooking)
