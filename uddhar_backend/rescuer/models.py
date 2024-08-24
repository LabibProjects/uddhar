from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class RescuerUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rescuer_user"
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    contact_number = models.CharField(max_length=200, blank=True, null=True)
    category = ArrayField(models.CharField(max_length=200), blank=True, null=True)
