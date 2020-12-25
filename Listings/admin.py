from django.contrib import admin
from . import models


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'price', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(models.Listing, ListingsAdmin)