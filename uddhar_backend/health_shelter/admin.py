from django.contrib import admin
from .models import HealthShelterPost, HealthShelterUser


@admin.register(HealthShelterUser)
class HealthShelterUserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "latitude",
        "longitude",
        "contact_number",
        "alternative_contact_number",
    )
    search_fields = ("name", "address")
    ordering = ("name",)
    readonly_fields = ("user",)


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
