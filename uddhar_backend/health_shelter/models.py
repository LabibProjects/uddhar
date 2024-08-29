from django.db import models
from django.conf import settings


class HealthShelterUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="health_shelter_user",
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    contact_number = models.CharField(max_length=200, blank=True, null=True)
    alternative_contact_number = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class HealthShelterPost(models.Model):
    user = models.ForeignKey(
        HealthShelterUser, on_delete=models.CASCADE, related_name="posts_user"
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    food_available_days = models.IntegerField(blank=True, null=True)
    people_capacity = models.IntegerField(blank=True, null=True)
    people_occupied = models.IntegerField(blank=True, null=True)

    WATER_LEVEL = (
        ("low", "Low"),
        ("moderate", "Moderate"),
        ("high", "High"),
        ("very_high", "Very high"),
    )
    water_level = models.CharField(
        blank=True, null=True, max_length=200, choices=WATER_LEVEL
    )
    medicine_available = models.BooleanField(default=False)
    sanitary_pads_available = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
