from django.contrib import admin

from vps.models import Vps


@admin.register(Vps)
class VpsAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'cpu',
        'ram',
        'hdd',
        'status',
        'created_date',
    )
    list_editable = (
        'status',
    )
    list_filter = (
        'status',
    )
