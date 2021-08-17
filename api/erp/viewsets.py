from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .serializers import ProductsSerializer
from .models import PurchaseDetail, Products
from rest_framework import permissions


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PurchaseDetail.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()
