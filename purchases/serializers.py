from rest_framework import serializers
from .models import Purchases, Store
from events.models import Events

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address']

class PurchasesSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    store_name = serializers.CharField(source='store.name', read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Events.objects.all())


    class Meta:
        model = Purchases
        fields = ['id', 'customer', 'date', 'invoice', 'value', 'store', 'store_name', 'event', 'created_at']

