from django.urls import path

from store.views.base import products_list_view
from store.views.products import product_view, product_add_view, product_update_view

urlpatterns = [
    path('', products_list_view, name='products_list_view'),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('product/add/', product_add_view, name='product_add_view'),
    path('product/edit/<int:pk>/', product_update_view, name='product_update_view'),
]
