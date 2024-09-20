from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchasesViewSet, StoreViewSet, generate_voucher_pdf

router = DefaultRouter()
router.register(r'purchases', PurchasesViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('voucher/pdf/<int:voucher_id>/', generate_voucher_pdf, name='voucher_pdf'),

    
]
