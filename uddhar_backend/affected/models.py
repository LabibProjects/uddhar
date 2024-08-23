from django.db import models
from django.conf import settings


class AffectedUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="affected_user"
    )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=200)
    alternative_contact_number = models.CharField(max_length=200)


class Affected(models.Model):
    user = models.ForeignKey(
        AffectedUser,
        on_delete=models.CASCADE,
        related_name="affected",
        blank=True,
        null=True,
    )
    status = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    number_of_people = models.IntegerField(default=0)
    requested_on = models.DateTimeField(auto_now_add=True)
    # will be taken from the user model if logged in
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=200)
    alternative_contact_number = models.CharField(max_length=200)
