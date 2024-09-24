from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchasesViewSet, StoreViewSet, generate_voucher_pdf

# Criação do router para registrar as rotas automáticas
router = DefaultRouter()
router.register(r'purchases', PurchasesViewSet)  # Rota para compras
router.register(r'stores', StoreViewSet)  # Rota para lojas

# Definição das URLs
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas geradas pelo router
    path('voucher/pdf/<int:voucher_id>/', generate_voucher_pdf, name='voucher_pdf'),  # Rota para gerar o PDF do voucher
]
