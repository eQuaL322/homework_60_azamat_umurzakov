from django.contrib import admin

from store.models import Product
from store.models.order import Order
from store.models.order_amount import OrderAmount


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'category', 'remains', 'price')
    list_filter = ('id', 'name', 'category', 'remains', 'price')
    search_fields = ('name', 'category', 'description', 'price')
    fields = ('name', 'description', 'image', 'category', 'remains', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('id', 'name', 'phone', 'address', 'created_at')
    search_fields = ('name', 'phone', 'address')
    fields = ('id', 'name', 'phone', 'address', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
