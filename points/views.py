from rest_framework.permissions import AllowAny #remove after
from rest_framework import viewsets
from .models import Purchases, Store
from .serializers import PurchasesSerializer, StoreSerializer
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [AllowAny] 


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny] 

def generate_voucher_pdf(request, voucher_id):
    # Get the voucher data (replace Purchases with your actual model)
    voucher = Purchases.objects.get(id=voucher_id)
    
    # Prepare the context for the PDF (data to be displayed)
    context = {
        'id': voucher_id,
        'voucher': voucher,
        'store': voucher.store,
        'customer': voucher.customer,
        'date': voucher.date,
        'value': voucher.value,
    }
    
    # Load the HTML template for the voucher
    template = get_template('voucher_template.html')
    html = template.render(context)

    # Create a HTTP response with a PDF attachment
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="voucher_{voucher_id}.pdf"'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the PDF if everything is ok
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=400)
    
    return response