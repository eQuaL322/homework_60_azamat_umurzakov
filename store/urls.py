from django.urls import path

from store.views.base import products_list_view
from store.views.products import product_view, product_add_view, product_update_view, product_delete_view, \
    product_confirm_delete_view

urlpatterns = [
    path('', products_list_view, name='products_list_view'),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('product/add/', product_add_view, name='product_add_view'),
    path('product/<int:pk>/edit/', product_update_view, name='product_update_view'),
    path('product/<int:pk>/delete/', product_delete_view, name='product_delete_view'),
    path('product/<int:pk>/confirm_delete/', product_confirm_delete_view, name='product_confirm_delete_view'),

]
