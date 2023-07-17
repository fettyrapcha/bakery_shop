from rest_framework import serializers
from .models import BakeryItem, Customer, Order, OrderItem

class BakeryItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = BakeryItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'