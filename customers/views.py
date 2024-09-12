from rest_framework.permissions import AllowAny #remove after
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny] 
    

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
