from django.contrib import admin
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'listing', 'listing_id', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing', 'contact_date')
    list_per_page = 25


admin.site.register(models.Contact, ContactAdmin)
