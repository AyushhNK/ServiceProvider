from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_service = models.BooleanField(null=True, blank=True, default=False)
    is_customer = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.username