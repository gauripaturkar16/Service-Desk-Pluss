from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_engineer=models.BooleanField(default=False)

    def __str__(self):
        return self.username
