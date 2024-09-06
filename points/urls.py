from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PointsViewSet, StoreViewSet

router = DefaultRouter()
router.register(r'points', PointsViewSet)
router.register(r'stores', StoreViewSet)  # Rota para lojas

urlpatterns = [
    path('', include(router.urls)),
]
