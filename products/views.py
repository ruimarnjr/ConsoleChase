from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    "A view designed to display a comprehensive list of products, featuring functionality for sorting and handling search queries."

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)