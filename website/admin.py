from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(Record, RecordAdmin)