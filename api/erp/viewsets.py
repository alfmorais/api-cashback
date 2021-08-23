from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .models import PurchaseDetail
from rest_framework import permissions
from .functions import (check_cpf_digits,
                        check_cpf_isvalid,
                        cashback_calculate,
                        calculate_check
                        )
from cashback.models import Cashback_API
from django.utils import timezone


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PurchaseDetail.objects.all()

    def create(self, request, *args, **kwargs):
        """
        This function will provide double check for customers documents
        and return true in case of sucessuful validated. 
        """

        # Request data from POST API
        data = request.data

        # Organize all variables to start the process to validate all data
        customer_document = data["customer_document"]
        customer_name = data["customer_name"]
        product_description = data["product_description"]
        product_value = data["product_value"]
        product_quantity = data["product_quantity"]
        total = data["total"]
        discount = data["discount"]

        # cashback time
        cashback_data = timezone.now()

        # create the database
        PurchaseDetail.objects.create(
            customer_document=customer_document,
            customer_name=customer_name,
            product_description=product_description,
            product_value=product_value,
            product_quantity=product_quantity,
            total=total,
            discount=discount,
        )

        # validate customers document
        validate_customers_document = check_cpf_digits(customer_document)
        validate_total = calculate_check(product_quantity,
                                         product_value,
                                         total)

        # Conditional of the program to save data in Cashback_API
        if (validate_customers_document and validate_total) == True:
            message = "Customers Document was sucessuful validated"
            cashback_message = "Cashback was sucessuful calculated"
            cashback_amount = cashback_calculate(
                discount,
                product_value,
                product_quantity)
            Cashback_API.objects.create(
                cashback_date=cashback_data,
                customer_name=customer_name,
                customer_document=customer_document,
                customer_document_validated=message,
                cashback_message=cashback_message,
                cashback_amount=cashback_amount
            )
            return Response('The data was received and save in our database')
        else:
            message = "Customers Document error validated"
            cashback_message = "It wasn't possible to calculate cashback amount"
            Cashback_API.objects.create(
                cashback_date=cashback_data,
                customer_name=customer_name,
                customer_document=customer_document,
                customer_document_validated=message,
                cashback_message=cashback_message,
                cashback_amount=0.0
            )
            return Response('The data was received and save in our database')
