from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .serializers import ProductsSerializer
from .models import PurchaseDetail, Products


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    queryset = PurchaseDetail.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
