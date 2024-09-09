from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class VerificationToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    is_service = models.BooleanField(null=True, blank=True, default=False)
    is_customer = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.username