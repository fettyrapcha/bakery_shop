# from django.shortcuts import render
from rest_framework import viewsets
from .models import BakeryItem, Customer, Order, OrderItem
from .serializers import BakeryItemSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer

class BakeryItemViewSet(viewsets.ModelViewSet):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
