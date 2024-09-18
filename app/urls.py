from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.http import HttpResponse

# View simples para a página inicial de /dashpoints/
def dashpoints_home(request):
    return HttpResponse("<h1>Bem-vindo ao Dashpoints</h1>")

# Configurações do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Dash Points",
        default_version='v1',
        description="Gerenciamento de pontos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@dashpoints.io"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('dashpoints/admin/', admin.site.urls),
    path('dashpoints/', dashpoints_home, name='dashpoints_home'),  # Adicionada esta linha
    path('dashpoints/api/', include('users.urls')), 
    path('dashpoints/api/', include('points.urls')), 
    path('dashpoints/api/', include('customers.urls')),

    # URLs de autenticação JWT
    path('dashpoints/api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dashpoints/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashpoints/api/validate-token/', TokenVerifyView.as_view(), name='token_verify'),

    # Documentação Swagger
    path('dashpoints/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('dashpoints/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
