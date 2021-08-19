from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .serializers import ProductsSerializer
from .models import PurchaseDetail, Products
from rest_framework import permissions
from .functions import (check_cpf_digits,
                        check_cpf_isvalid,
                        cachback_calculate,
                        calculate_check
                        )
from cashback.models import Cashback_API


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PurchaseDetail.objects.all()

    def post(self, request, format=None):
        """
        This function will provide double check for customers documents
        and return true in case of sucessuful validated. 
        """
        api_data = request.data
        customer_name = api_data["results"]["customer_name"]
        customer_document = api_data["results"]["customer_document"]
        first_validate = check_cpf_digits(customer_document)
        second_validate = check_cpf_isvalid(customer_document)
        if (first_validate and second_validate) == True:
            message = "Customers Document was sucessuful validated"
            database_updated = Cashback_API(customer_document_validated=message,
                                            customer_name=customer_name,
                                            customer_document=customer_document)
            database_updated.save()
        else:
            message = "Customers Document error validated"
            database_updated = Cashback_API(customer_document_validated=message,
                                            customer_name=customer_name,
                                            customer_document=customer_document)
            database_updated.save()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()

    def post(self, request, format=None):
        """
        This function will check products and cashback value.
        """
        api_data = request.data
        product_value = api_data['results']['product_value']
        quantity = api_data['results']['product_quantity']
        cashback = api_data['results']['discount']
        try:
            # Variables regarding a Cashback_API
            cashback_amount = cachback_calculate(cashback,
                                                 product_value,
                                                 quantity)
            message = 'The cashback was created'
            database_updated = Cashback_API(message=message,
                                            cashback_amount=cashback_amount)
            database_updated.save()
        except ValueError:
            message = 'Did not possible to calculate cashback amount'
            cashback_amount = 0.0
            database_updated = Cashback_API(message=message,
                                            cashback_amount=cashback_amount)
            database_updated.save()
