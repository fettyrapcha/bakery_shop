from django.urls import path
from .views import (
    BakeryItemListCreateView,
    BakeryItemRetrieveUpdateDestroyView,
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('bakery_items/', BakeryItemListCreateView.as_view(), name='bakery_item_list_create'),
    path('bakery_items/<int:pk>/', BakeryItemRetrieveUpdateDestroyView.as_view(), name='bakery_item_retrieve_update_destroy'),
    path('customers/', CustomerListCreateView.as_view(), name='customer_list_create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer_retrieve_update_destroy'),
    path('orders/', OrderListCreateView.as_view(), name='order_list_create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order_retrieve_update_destroy'),
]
