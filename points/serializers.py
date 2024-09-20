from rest_framework import serializers
from .models import Purchases, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address']

class PurchasesSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())  # Dropdown de lojas

    class Meta:
        model = Purchases
        fields = ['id', 'customer', 'invoice', 'store', 'value', 'date', 'created_at']

