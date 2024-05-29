import uuid

from django.db import models

from users.models import User


class Ticket(models.Model):
    status_choice=(
        ('Active','Active'),
        ('Completed','Completed'),
        ('Pending','Pending')
    )
    ticket_number = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete= models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(null=True, blank=True)
    accepted_date = models.DateTimeField(null= True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    ticket_status = models.CharField(max_length=50, choices=status_choice)

    def __str__(self):
        return self.title