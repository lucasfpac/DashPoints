from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CustomerCreateView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/cpf_cnpj/<str:cpf_cnpj>/', CustomerViewSet.as_view({'get': 'retrieve_by_cpf_cnpj'}), name='customer_by_cpf_cnpj'),
]
