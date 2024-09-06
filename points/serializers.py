from rest_framework import serializers
from .models import Points, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address']

class PointsSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())  # Dropdown de lojas

    class Meta:
        model = Points
        fields = ['id', 'user', 'store', 'value', 'date', 'created_at']
