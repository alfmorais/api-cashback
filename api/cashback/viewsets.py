from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomersSerializer
from .models import Customers


# define viewsets for classes created on serializers.py
class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customers.objects.all()

    def post(self, request, format=None):
        pass
