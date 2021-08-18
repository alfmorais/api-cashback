from django.contrib import admin
from .models import Customers, Cashback_API


# Register your models here.
class Cashback_APIAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Cashback_API.
    """
    list_display = ('customer_name', 'customer_document',
                    'message', 'cashback_amount')
