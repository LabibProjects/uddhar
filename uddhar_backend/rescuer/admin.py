from django.contrib import admin
from .models import RescuerUser 


@admin.register(RescuerUser)
class RescuerUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "address", "contact_number", "category")
    list_display_links = ("id", "user")
    search_fields = ("user", "name", "address", "contact_number", "category")
    list_per_page = 25

