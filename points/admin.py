from django.contrib import admin
from points.models import Points

class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer','store', 'value', 'created_at')
    search_fields = ['user','customer','store', 'value', 'created_at']
admin.site.register(Points, PointAdmin)    