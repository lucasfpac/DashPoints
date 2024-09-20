from rest_framework.permissions import AllowAny  # remove after
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import status


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve_by_cpf_cnpj(self, request, cpf_cnpj=None):
        try:
            # Verifica o cliente pelo CPF/CNPJ exato (sem espaços ou formatações extras)
            customer = Customer.objects.get(cpf_cnpj=cpf_cnpj.strip())
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
    permission_classes = [AllowAny]


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
