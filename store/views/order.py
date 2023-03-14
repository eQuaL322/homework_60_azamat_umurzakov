from django.urls import reverse
from django.views.generic import CreateView

from store.forms import OrderForm
from store.models import CartItem
from store.models.order import Order
from store.models.order_amount import OrderAmount


class OrderAddView(CreateView):
    template_name = 'partial/add_order.html'
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        cart_products = CartItem.objects.all()
        order = form.save()
        for cart_product in cart_products:
            form.instance.products.add(cart_product.product)
            qty = OrderAmount.objects.create(order_id=order.pk,
                                             product=cart_product.product,
                                             order_amount=cart_product.qty)
        cart_products.delete()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products_list_view')
