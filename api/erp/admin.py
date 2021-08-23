from django.contrib import admin
from .models import PurchaseDetail


# Register your models here.
@admin.register(PurchaseDetail)
class PurchaseDetailAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database PurchaseDetail.
    """
    list_display = ('customer_document',
                    'customer_name',
                    'product_description',
                    'product_value',
                    'product_quantity',
                    'total',
                    'discount',
                    'sold_at')
