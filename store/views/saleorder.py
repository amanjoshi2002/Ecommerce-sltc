from django.shortcuts import render, redirect
from django.http import JsonResponse
from store.models.product import Product,RetailStore, SalesOrder, OrderItem
from django.forms import formset_factory
from .forms import SalesOrderForm, OrderItemForm, OrderItemFormSet
from django.db.models import Q
from django.views.decorators.http import require_POST
import pyperclip

def sales_order_form(request):
    retail_stores = RetailStore.objects.all()
    products = Product.objects.all()
    context = {
        'retail_stores': retail_stores,
        'products': products,
    }
    return render(request, 'sales_order_form.html', context)

def create_sales_order(request):
    form = SalesOrderForm(request.POST)
    formset = OrderItemFormSet(request.POST)

    if form.is_valid() and formset.is_valid():
        sales_order = form.save()
        order_items = formset.save(commit=False)

        for order_item in order_items:
            order_item.order = sales_order
            order_item.save()

        # Get retail and product names with quantities
        retail_name = sales_order.retail.name
        product_names_quantities = [
            f"{item.product.name} (Qty: {item.qty})"
            for item in order_items
        ]

        # Generate text to copy to clipboard
        text_to_copy = f"Retail: {retail_name}\n"
        text_to_copy += "\n".join(product_names_quantities)

        # Copy text to clipboard
        pyperclip.copy(text_to_copy)

        context = {
            'retail_name': retail_name,
            'product_names_quantities': product_names_quantities,
            'text_to_copy': text_to_copy,
        }

        return render(request, 'sales_order_success.html', context)

    return render(request, 'sales_order_form.html', {'form': form, 'formset': formset})



from django.http import JsonResponse
from django.db.models import Q

def search_product(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(name__icontains=query)
    data = [{'name': product.name} for product in results]
    return JsonResponse(data, safe=False)

def search_retail(request):
    query = request.GET.get('query', '')
    results = RetailStore.objects.filter(name__icontains=query)
    data = [{'name': retail.name} for retail in results]
    return JsonResponse(data, safe=False)




def sales_order_success(request):
    sales_order = SalesOrder.objects.latest('id')
    order_items = sales_order.order_items.all()
    context = {
        'sales_order': sales_order,
        'order_items': order_items,
    }
    return render(request, 'sales_order_success.html', context)