from django.urls import path

from store.views.base import products_list_view
from store.views.products import product_view

urlpatterns = [
    path('', products_list_view, name='products_list_view'),
    path('product/<int:pk>/', product_view, name='product_view'),
]
