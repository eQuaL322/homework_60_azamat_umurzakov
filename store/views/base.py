from django.views.generic import ListView

from store.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(remains__gte=1).order_by('category', 'name')
