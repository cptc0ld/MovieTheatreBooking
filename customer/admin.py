from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Ticket


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('TicketId', 'ShowId', 'CustomerId')
