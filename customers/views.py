from rest_framework.permissions import AllowAny #remove after
from rest_framework import viewsets
from .models import Customer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from rest_framework import generics

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['get'])
    def get_by_cpf_cnpj(self, request):
        cpf_cnpj = request.query_params.get('cpf_cnpj', None)
        if cpf_cnpj is not None:
            try:
                customer = Customer.objects.get(cpf_cnpj=cpf_cnpj)
                serializer = self.get_serializer(customer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Customer.DoesNotExist:
                return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'CPF/CNPJ is required'}, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [AllowAny] 
    

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
