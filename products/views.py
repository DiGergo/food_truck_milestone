from django.shortcuts import render

from .models import User, Products, Order, Order_Products
# Create your views here.


def products_list(request):
    context = {
        'products' : Products.objects.all()
    }
    return render (request, 'products_list.html', context)