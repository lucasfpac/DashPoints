from django.contrib import admin
from points.models import Points

class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'store', 'value', 'created_at')
    search_fields = ['user', 'store', 'value', 'created_at']
admin.site.register(Points, PointsAdmin)    