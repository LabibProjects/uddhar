from django.contrib import admin
from affected.models import AffectedRequest, AffectedUser


@admin.register(AffectedUser)
class AffectedUserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "address",
        "latitude",
        "longitude",
        "contact_number",
        "alternative_contact_number",
        "blood_group",
    )


@admin.register(AffectedRequest)
class AffectedRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "rescuer_user",
        "category",
        "number_of_people",
        "description",
        "requested_on",
        "latitude",
        "longitude",
        "contact_number",
        "alternative_contact_number",
        "name",
        "status",
        "rescuer_positions",
        "rescuer_descriptions",
        "rescue_updated_times",
        "rescue_active_from",
    )
    list_display_links = ("user", "rescuer_user")
    search_fields = (
        "user",
        "rescuer_user",
        "category",
        "number_of_people",
        "description",
        "requested_on",
        "latitude",
        "longitude",
        "contact_number",
        "alternative_contact_number",
        "name",
        "status",
        "rescuer_positions",
        "rescuer_descriptions",
        "rescue_updated_times",
        "rescue_active_from",
    )
    list_per_page = 25
