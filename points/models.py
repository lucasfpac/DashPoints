from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
import datetime

class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='points')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.value} pontos na loja {self.store.name}"

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name