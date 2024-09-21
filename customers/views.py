from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]  # Permissão aberta temporariamente

    # Método para buscar o cliente pelo CPF ou CNPJ
    def retrieve_by_cpf_cnpj(self, request, cpf_cnpj=None):
        cpf_cnpj = cpf_cnpj.strip()  # Remover espaços antes e depois
        try:
            # Filtra o cliente com CPF ou CNPJ exatamente igual
            customer = Customer.objects.get(cpf_cnpj=cpf_cnpj)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            # Retorna 404 se o cliente não for encontrado
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]  # Permissão aberta temporariamente
