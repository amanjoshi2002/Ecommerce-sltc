from django import forms
from store.models.retailstore import RetailStore
from store.models.product import Product,SalesOrder,OrderItem
from django.forms import formset_factory


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'qty']


OrderItemFormSet = formset_factory(OrderItemForm, extra=1)
