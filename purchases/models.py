from django.db import models
import datetime

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Purchases(models.Model): 
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, default=1) 
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  
    invoice = models.CharField(max_length=255, default="N/A") 
    value = models.DecimalField(max_digits=10, decimal_places=2)  
    date = models.DateField(default=datetime.date.today) 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.customer} - {self.value} na loja {self.store.name}"
