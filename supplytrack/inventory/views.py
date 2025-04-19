from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product
from .forms import ProductForm, StockMovementForm

def inventory_list(request):
    query = request.GET.get('q', '')
    product_list = Product.objects.all()

    if query:
        product_list = product_list.filter(
            Q(product_id__icontains=query) |
            Q(product_name__icontains=query) |
            Q(product_type__icontains=query) |
            Q(unit_size__icontains=query) |
            Q(brand__icontains=query) |
            Q(batch_number__icontains=query) |
            Q(expiration_date__icontains=query) |
            Q(date_received__icontains=query)
        )

    product_list = product_list.order_by('-id')  # Optional: newest first

    paginator = Paginator(product_list, 20)  # Show 20 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    form = ProductForm()
    movement_form = StockMovementForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory_list')

    context = {
        'products': products,
        'form': form,
        'movement_form': movement_form,
        'query': query,
    }
    return render(request, 'inventory/inventory_list.html', context)


# def inventory_list(request):
#     products = Product.objects.all()
#     form = ProductForm()
#     movement_form = StockMovementForm()

#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inventory:inventory_list')

#     context = {
#         'products': products,
#         'form': form,
#         'movement_form': movement_form,
#     }
#     return render(request, 'inventory/inventory_list.html', context)


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'inventory/product_edit.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory:inventory_list')
    
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

