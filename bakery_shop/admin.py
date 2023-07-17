from django.contrib import admin
from .models import BakeryItem, Customer, Order, OrderItem

class BakeryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

admin.site.register(BakeryItem, BakeryItemAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
