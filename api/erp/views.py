from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .models import PurchaseDetail
from .functions import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cashback_views(request):
    """
    This function will return all data necessary to 
    calculate cashback amount.
    """
    products = Products.objects.all()
    output = [{
        "Discount": products.discount,
        "Product Value": products.product_value,
        "Quantity": products.product_quantity,
    } for product in products]

    return Response(output)
