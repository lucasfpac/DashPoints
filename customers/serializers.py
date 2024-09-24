from rest_framework import serializers
from .models import Customer
from purchases.models import Purchases

class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ['id'] 

class CustomerSerializer(serializers.ModelSerializer):
    purchases = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'cpf_cnpj', 'email', 'phone', 'cep', 'city', 'uf', 'missingstore', 'selected_store', 'purchases']

    def get_purchases(self, obj):
        return Purchases.objects.filter(customer=obj).values_list('id', flat=True)
