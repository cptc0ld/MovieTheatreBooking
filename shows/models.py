from django.db import models
import uuid
# Create your models here.


class Shows(models.Model):
    showid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    MovieName = models.CharField(max_length=20, blank=False)
    Screen = models.CharField(max_length=20, blank=False)
    Duration = models.CharField(max_length=20, blank=False)
    StartTime = models.DateTimeField(max_length=20, blank=False)
    count = models.IntegerField(default=20)
