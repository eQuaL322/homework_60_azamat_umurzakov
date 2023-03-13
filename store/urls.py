from django.urls import path

from store.views.base import IndexView
from store.views.products import ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='products_list_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='product_confirm_delete_view'),

]
