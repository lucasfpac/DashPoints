from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cpf_cnpj', 'email', 'phone', 'cep', 'city', 'uf', 'missingstore', 'selected_store')
    search_fields = ('full_name', 'cpf_cnpj', 'email', 'city')

admin.site.register(Customer, CustomerAdmin)
