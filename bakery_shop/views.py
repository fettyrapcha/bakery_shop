from rest_framework import generics
from .models import BakeryItem, Customer, Order, OrderItem
from .serializers import BakeryItemSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer

class BakeryItemListCreateView(generics.ListCreateAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class BakeryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
