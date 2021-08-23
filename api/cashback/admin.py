from django.contrib import admin
from .models import Customers, Cashback_API


# Register your models here.
@admin.register(Cashback_API)
class Cashback_APIAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Cashback_API.
    """
    list_display = ('cashback_date',
                    'customer_name',
                    'customer_document',
                    'customer_document_validated',
                    'cashback_message',
                    'cashback_amount')


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Customers.
    """
    list_display = ('customer_document',)
