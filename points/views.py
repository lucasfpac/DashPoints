from rest_framework.permissions import AllowAny #remove after
from rest_framework import viewsets
from .models import Points, Store
from .serializers import PointsSerializer, StoreSerializer

class PointsViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
    permission_classes = [AllowAny] 


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny] 
