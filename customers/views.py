from rest_framework.permissions import AllowAny  # remove after
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve_by_cpf_cnpj(self, request, cpf_cnpj=None):
        try:
            customer = Customer.objects.get(cpf_cnpj=cpf_cnpj)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=404)
    permission_classes = [AllowAny]


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
