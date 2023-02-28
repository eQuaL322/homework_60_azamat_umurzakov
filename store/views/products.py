from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from store.models import Product


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }

    return render(request, 'product_view.html', context=context)
