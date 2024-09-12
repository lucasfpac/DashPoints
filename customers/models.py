from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cpf = CPFField(masked=True, blank= True, null= True)  # To enable auto-mask xxx.xxx.xxx-xx
    cnpj = CNPJField(masked=True, blank= True, null= True)  # To enable auto-mask xx.xxx.xxx/xxxx-xx
    phone = PhoneNumberField(blank= True, null= True)
    address = models.CharField(max_length=50)
    dob = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return f"{self.name} {self.surname}"