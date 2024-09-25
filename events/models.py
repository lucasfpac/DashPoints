from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    voucher_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Evento {self.name} - valor para troca {self.voucher_value}"