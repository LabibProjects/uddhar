from django.contrib import admin
from affected.models import AffectedRequest


@admin.register(AffectedRequest)
class AffectedRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "status",
        "category",
        "number_of_people",
        "requested_on",
        "latitude",
        "longitude",
        "contact_number",
        "alternative_contact_number",
    )
    list_filter = ("status",)
    search_fields = (
        "user__name",
        "user__address",
        "contact_number",
        "alternative_contact_number",
    )
    ordering = ("-requested_on",)
    date_hierarchy = "requested_on"
    list_per_page = 20
    list_editable = ("status",)
    list_display_links = ("user",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "status",
                    "category",
                    "number_of_people",
                    "requested_on",
                    "latitude",
                    "longitude",
                    "contact_number",
                    "alternative_contact_number",
                )
            },
        ),
    )
    readonly_fields = ("requested_on",)
    actions = ["mark_as_pending", "mark_as_completed"]

    def mark_as_pending(self, request, queryset):
        queryset.update(status="pending")

    mark_as_pending.short_description = "Mark selected requests as pending"

    def mark_as_completed(self, request, queryset):
        queryset.update(status="completed")

    mark_as_completed.short_description = "Mark selected requests as completed"
