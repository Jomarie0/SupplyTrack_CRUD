from django.shortcuts import render
from inventory.models import Product
import json

# def home(request):
#     return render(request, 'dashboard/home.html')

def home(request):
    products = Product.objects.all()
    labels = [product.product_name for product in products]
    values = [product.stock_movements.last().quantity if product.stock_movements.exists() else 0 for product in products]

    context = {
        'labels': json.dumps(labels),
        'values': json.dumps(values),
    }
    return render(request, 'dashboard/home.html', context)
