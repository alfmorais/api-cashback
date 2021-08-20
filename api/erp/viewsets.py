from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .serializers import ProductsSerializer
from .models import PurchaseDetail, Products
from rest_framework import permissions
from .functions import (check_cpf_digits,
                        check_cpf_isvalid,
                        cashback_calculate,
                        calculate_check
                        )
from cashback.models import Cashback_API


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PurchaseDetail.objects.all()

    def create(self, request, *args, **kwargs):
        """
        This function will provide double check for customers documents
        and return true in case of sucessuful validated. 
        """
        data = request.data
        customer_name = data["customer_name"]
        customer_document = data["customer_document"]
        total = data["total"]

        PurchaseDetail.objects.create(
            customer_name=data["customer_name"],
            customer_document=data["customer_document"],
            total=data["total"],
        )

        # validate customers document
        validate = check_cpf_digits(customer_document)

        if validate == True:
            message = "Customers Document was sucessuful validated"
            Cashback_API.objects.create(
                customer_document_validated=message,
                customer_name=customer_name,
                customer_document=customer_document)
            return Response('OK')
        else:
            message = "Customers Document error validated"
            Cashback_API.objects.create(
                customer_document_validated=message,
                customer_name=customer_name,
                customer_document=customer_document)
            return Response('OK')


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()

    def create(self, request):
        """
        This function will check products and cashback value.
        """
        data = request.data
        print(data)
        product_value = data['product_value']
        quantity = data['product_quantity']
        cashback = data['discount']

        Products.objects.create(
            product_value=data['product_value'],
            product_quantity=data['product_quantity'],
            discount=data['discount'],
            product_description=data['product_description'],
        )
        cashback_amount = cashback_calculate(cashback,
                                             product_value,
                                             quantity)
        message = 'The cashback was created'
        Cashback_API.objects.create(
            message=message,
            cashback_amount=cashback_amount)
        return Response('OK')
