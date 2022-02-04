from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.


def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'Products/product_detail.html', context)
