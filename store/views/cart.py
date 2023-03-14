from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from store.models import CartItem, Product


class AddToCartView(View):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        cart_item = CartItem.objects.filter(product=product).first()
        if cart_item is None:
            if product.remains > 0:
                cart_item = CartItem(product=product)
            else:
                return redirect('products_list_view')
        else:
            if cart_item.qty >= product.remains:
                return redirect('products_list_view')
            cart_item.qty += 1
        cart_item.save()
        product.remains -= 1
        product.save()
        return redirect('products_list_view')

    def get(self, request):
        cart_items = CartItem.objects.all()
        return render(request, 'cart/cart_view.html', {'cart_items': cart_items})


class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart_view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_cost = sum([product.product.price * product.qty for product in context['object_list']])
        context['total_cost'] = total_cost
        return context


class CartProductDeleteView(DeleteView):
    template_name = 'cart/cart_product_delete.html'
    model = CartItem
    context_object_name = 'product'
    success_url = reverse_lazy('card')
