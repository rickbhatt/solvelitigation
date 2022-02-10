from django.contrib import admin

from . models import VisitorCount

@admin.register(VisitorCount)
class VistorAdmin(admin.ModelAdmin):
   list_display = ("ip", "date_of_record")
   ordering = ("-date_of_record",)
   search_fields = ("ip",)
