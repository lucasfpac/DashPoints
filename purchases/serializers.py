from rest_framework import serializers
from .models import Purchases, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address']

class PurchasesSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    store_name = serializers.CharField(source='store.name', read_only=True)


    class Meta:
        model = Purchases
        fields = ['id', 'customer', 'date', 'invoice', 'value', 'store', 'store_name', 'created_at']

