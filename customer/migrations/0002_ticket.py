# Generated by Django 3.1 on 2020-08-29 12:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('TickerId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ShowId', models.UUIDField(editable=False)),
                ('CustomerId', models.UUIDField(editable=False)),
            ],
        ),
    ]