from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomersSerializer
from .models import Customers, Cashback_API
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum


# define viewsets for classes created on serializers.py
class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customers.objects.all()

    def create(self, request, format=None):
        """
        This method CREATE function will responsable for
        show all cashback value by customers
        """

        # Request data from POST API
        data = request.data

        # request value from POST method
        customer_document = data["customer_document"]

        # save data in database
        Customers.objects.create(
            customer_document=customer_document
        )

        # getting database only
        database = Cashback_API.objects.filter(
            customer_document=customer_document
        )

        # getting variables regarding to cashback API response
        customer_name = database.values("customer_name").latest("id")
        customer_document = database.values("customer_document").latest("id")
        cashback_per_purchase_detail = database.values_list(
            "cashback_amount").order_by("id")
        cashback_total = database.aggregate(Sum("cashback_amount"))

        # that response will be in charge of the reply some consult
        # for checking how much cashback some customer have in our
        # database. The answer will provide a full information
        # to accomplish targets from API 2
        return Response({
            "customer_name": customer_name,
            "customer_document": customer_document,
            "cashback_per_purchase_detail": cashback_per_purchase_detail,
            "cashback_total": cashback_total,
        })
