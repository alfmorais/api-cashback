from django.contrib import admin
from .models import PurchaseDetail, Products


# Register your models here.
@admin.register(PurchaseDetail)
class PurchaseDetailAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database PurchaseDetail.
    """
    list_display = ('customer_name', 'customer_document',
                    'total', 'sold_at')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference 
    from database Products 
    """
    list_display = ('product_description', 'product_quantity',
                    'product_value', 'discount')
