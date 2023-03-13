from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from store.forms import ProductForm
from store.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_view.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add_view.html'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update_view.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_delete_view.html'
    context_object_name = 'product'
    model = Product
    success_url = reverse_lazy('products_list_view')
