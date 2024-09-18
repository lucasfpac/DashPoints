from rest_framework.permissions import AllowAny  # remove after
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], url_path='cpf_cnpj')
    def get_by_cpf_cnpj(self, request):
        cpf_cnpj = request.query_params.get('cpf_cnpj', None)
        if cpf_cnpj:
            try:
                customer = Customer.objects.get(cpf_cnpj=cpf_cnpj)
                serializer = self.get_serializer(customer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Customer.DoesNotExist:
                return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'CPF/CNPJ is required'}, status=status.HTTP_400_BAD_REQUEST)


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
