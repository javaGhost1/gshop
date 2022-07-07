from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    laptops = Product.objects.filter(category=1)
    speakers = Product.objects.filter(category=2)
    context = {'products':products, 'categories':categories, 'laptops':laptops, 'speakers':speakers}
    return render(request, 'product/index.html', context)