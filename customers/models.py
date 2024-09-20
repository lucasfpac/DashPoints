from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    full_name = models.CharField(max_length=255, default="Nome não informado")
    cpf_cnpj = models.CharField(unique=True, max_length=18, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    cep = models.CharField(max_length=9, default='00000-000')
    city = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2)
    missingstore = models.CharField(max_length=100, blank=True, null=True)
    selected_store = models.ForeignKey('points.Store', on_delete=models.CASCADE, null=True, blank=True, related_name='customers')

    def __str__(self):
        return f"{self.full_name}"

    def get_selected_store(self):
        from points.models import Store  # Importação movida para cá
        return Store.objects.filter(id=self.selected_store.id).first() if self.selected_store else None
