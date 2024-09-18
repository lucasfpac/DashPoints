from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=18, blank=True, null=True) 
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    cep = models.CharField(max_length=9, default='00000-000')
    city = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2) 
    missingstore = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return f"{self.full_name}"
