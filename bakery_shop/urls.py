from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BakeryItemViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'bakery_items', BakeryItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]