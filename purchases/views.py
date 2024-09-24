from rest_framework.permissions import AllowAny  # remove after
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Purchases, Store
from .serializers import PurchasesSerializer, StoreSerializer


class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [AllowAny]

    # Sobrescrevendo o método list para permitir filtro por customer
    def list(self, request, *args, **kwargs):
        customer_id = request.query_params.get('customer', None)
        
        if customer_id is not None:
            # Filtra as compras pelo ID do cliente
            purchases = Purchases.objects.filter(customer_id=customer_id)
            if purchases.exists():
                serializer = self.get_serializer(purchases, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "No purchases found for this customer."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Se não houver customer_id na query string, retorna todas as compras
            return super().list(request, *args, **kwargs)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]


def generate_voucher_pdf(request, voucher_id):
    # Busca o voucher com base no ID fornecido
    voucher = Purchases.objects.get(id=voucher_id)
    
    # Contexto a ser enviado para o template HTML
    context = {
        'id': voucher_id,
        'voucher': voucher,
        'store': voucher.store,
        'customer': voucher.customer,
        'date': voucher.date,
        'value': voucher.value,
    }
    
    # Carrega o template HTML e renderiza com o contexto
    template = get_template('voucher_template.html')
    html = template.render(context)

    # Configura a resposta HTTP para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="voucher_{voucher_id}.pdf"'

    # Converte o HTML em PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Retorna o PDF se tudo estiver certo, senão um erro
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=400)
    
    return response
