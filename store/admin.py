from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.retailstore import RetailStore
from django.shortcuts import redirect


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price']


# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ['__str__', 'email']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(RetailStore)
class RetailStoreAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']



 