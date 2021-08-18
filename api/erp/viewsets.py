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
        customers_document = api_data["results"]["customer_document"]
        first_validate = check_cpf_digits(customers_document)
        second_validate = check_cpf_isvalid(customers_document)
        if (first_validate and second_validate) == True:
            message = "Customers Document was sucessuful validated"
            return message
        else:
            message = "Customers Document error validated"
            return message


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()
