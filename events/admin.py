from django.contrib import admin
from events.models import Events

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'voucher_value')
    search_fields = ('id', 'name', 'start_date', 'end_date', 'voucher_value')
admin.site.register(Events, EventAdmin)