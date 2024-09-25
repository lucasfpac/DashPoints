from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    voucher_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        
    def __str__(self):
        return f"Evento {self.name} de: {self.start_date}, até: {self.end_date} valor para troca = {self.voucher_value}"