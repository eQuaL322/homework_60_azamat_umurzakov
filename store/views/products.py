from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from store.forms import ProductForm
from store.models import Product


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }

    return render(request, 'product_view.html', context=context)


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_add_view.html', context={
            'form': form
        })

    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_add_view.html', context={
            'form': form
        })
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_view', pk=product.pk)


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'product_update_view.html', context=context)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.image = form.cleaned_data['image']
        product.category = form.cleaned_data['category']
        product.remains = form.cleaned_data['remains']
        product.price = form.cleaned_data['price']
        product.save()
        return redirect('product_view', pk=product.pk)

    form = ProductForm(instance=product)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'product_update_view.html', context=context)
