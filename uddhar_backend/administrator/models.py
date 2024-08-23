from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Boolean fields to select the type of account.
    is_admin = models.BooleanField(default=False)
    is_affected = models.BooleanField(default=False)
    is_health_shelter = models.BooleanField(default=False)
