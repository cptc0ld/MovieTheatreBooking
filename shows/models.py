from django.db import models
import uuid
# Create your models here.


class Shows(models.Model):
    showid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    MovieName = models.CharField(max_length=20, blank=False)
    Screen = models.CharField(max_length=20, blank=False)
    Duration = models.CharField(max_length=20, blank=False)
    StartTime = models.TimeField(max_length=20, blank=False)
    Date = models.DateField(max_length=20, blank=False)

    def save(self, *args, **kwargs):
        show = availableshows.objects.create(showid=self.showid)
        show.save()
        super(Shows, self).save(*args, **kwargs)


class availableshows(models.Model):
    showid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    count = models.IntegerField(default=20)
