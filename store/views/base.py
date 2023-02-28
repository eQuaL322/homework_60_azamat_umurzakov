from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from store.models import Product


def products_list_view(request: WSGIRequest):
    products = Product.objects.filter(remains__gt=0).order_by('category', 'name')
    context = {
        'products': products
    }

    return render(request, 'index.html', context=context)
