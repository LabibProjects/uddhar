from django.contrib import admin
from .models import HealthShelterPost


@admin.register(HealthShelterPost)
class HealthShelterPostAdmin(admin.ModelAdmin):
    list_display = (
        "address",
        "latitude",
        "longitude",
        "food_available_days",
        "people_capacity",
        "people_occupied",
        "water_level",
        "medicine_available",
        "sanitary_pads_available",
        "created_on",
    )
    list_filter = ("water_level", "medicine_available", "sanitary_pads_available")
    search_fields = ("address",)
    ordering = ("created_on",)
    date_hierarchy = "created_on"
    readonly_fields = ("created_on",)
