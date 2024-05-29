# Generated by Django 5.0.3 on 2024-03-22 11:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(blank=True, null=True)),
                ('accepted_date', models.DateField(blank=True, null=True)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('ticket_status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=15)),
            ],
        ),
    ]
