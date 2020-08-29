from django.urls import path
from .views import ViewCustomers, TicketBooking, ViewCustomersbyTid
import uuid
urlpatterns = [
    path('customers/', ViewCustomers.as_view()),
    path('customers/<uuid:tid>', ViewCustomersbyTid.as_view()),
    path('ticket/', TicketBooking.as_view()),
    path('ticket/<uuid:id>', TicketBooking.as_view()),
]
