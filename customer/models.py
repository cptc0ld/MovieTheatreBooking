from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.username


class Ticket(models.Model):
    TicketId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    ShowId = models.UUIDField(editable=False)
    CustomerId = models.UUIDField(editable=False)
