from django.contrib import admin

from store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'category', 'remains', 'price')
    list_filter = ('id', 'name', 'category', 'remains', 'price')
    search_fields = ('name', 'category', 'description', 'price')
    fields = ('name', 'description', 'image', 'category', 'remains', 'price')


admin.site.register(Product, ProductAdmin)
