from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'cpf', 'cnpj', 'phone', 'address', 'dob')
    search_fields = ['name', 'surname', 'cpf', 'cnpj', 'phone', 'address', 'dob']
# admin.site.register(Customer, CustomerAdmin)    