from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomersSerializer
from .models import Customers
from rest_framework.response import Response


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

        # getting database regarding cashback

        return Response("OK")
