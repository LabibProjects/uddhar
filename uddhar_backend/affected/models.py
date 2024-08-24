from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.conf import settings


class AffectedUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="affected_user"
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    contact_number = models.CharField(max_length=200, blank=True, null=True)
    alternative_contact_number = models.CharField(max_length=200, blank=True, null=True)
    blood_group = models.CharField(max_length=200, blank=True, null=True)


class AffectedRequest(models.Model):
    user = models.ForeignKey(
        AffectedUser,
        on_delete=models.CASCADE,
        related_name="affected",
        blank=True,
        null=True,
    )
    rescuer_user = models.ForeignKey(
        "rescuer.RescuerUser",
        on_delete=models.CASCADE,
        related_name="rescuer",
        blank=True,
        null=True,
    )

    CATEGORY = (
        ("food", "Food"),
        ("water", "Water"),
        ("shelter", "Shelter"),
        ("medical_help", "Medical Help"),
        ("boat", "Boat"),
        ("helicopter", "Helicopter"),
        ("speed_boat", "Speed Boat"),
    )
    # food, water, shelter, medical help, array of these
    images = ArrayField(models.URLField(), blank=True, null=True)
    category = ArrayField(models.CharField(max_length=200))
    number_of_people = models.IntegerField(default=0)
    description = models.CharField(max_length=500, blank=True, null=True)
    requested_on = models.DateTimeField(auto_now_add=True)
    # will be taken from the user model if logged in
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=200)
    alternative_contact_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    # rescuer operations
    STATUS = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
    )
    status = models.CharField(max_length=200, default="pending")
    rescuer_positions = JSONField(default=list, blank=True)
    rescuer_descriptions = ArrayField(
        models.CharField(max_length=200), default=list, blank=True
    )
    rescue_updated_times = ArrayField(models.DateTimeField(), default=list, blank=True)
    rescue_active_from = models.DateTimeField(blank=True, null=True)
