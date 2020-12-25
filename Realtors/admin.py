from django.contrib import admin
from . import models


class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_editable = ('is_mvp',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.Realtor, RealtorsAdmin)
