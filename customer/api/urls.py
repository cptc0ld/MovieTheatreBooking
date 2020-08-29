from django.urls import path
from .views import ViewCustomers, TicketBooking

urlpatterns = [
    path('customers/', ViewCustomers.as_view()),
    path('bookticket/', TicketBooking.as_view()),
]
