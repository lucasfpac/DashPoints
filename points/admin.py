from django.contrib import admin
from points.models import Purchases, Store

class PointAdmin(admin.ModelAdmin):
    list_display = ('customer','store', 'value', 'created_at')
    search_fields = ['customer','store', 'value', 'created_at']
admin.site.register(Purchases, PointAdmin)    

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
admin.site.register(Store, StoreAdmin)