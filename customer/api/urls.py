from django.urls import path
from .views import ViewCustomers, TicketBooking, ViewCustomersbyTid
import uuid
urlpatterns = [
    path('customers/', ViewCustomers.as_view(), name='customers'),
    path('customers/<uuid:tid>', ViewCustomersbyTid.as_view(), name="customer"),
    path('ticket/', TicketBooking.as_view(), name="tickets"),
    path('ticket/<uuid:id>', TicketBooking.as_view(), name="ticket"),
]
