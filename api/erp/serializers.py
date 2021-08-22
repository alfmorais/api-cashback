# all packages necessary to work serializers
from rest_framework import serializers
from .models import PurchaseDetail, Products


# Define serializers class from PurchaseDetail and Products
class PurchaseDetailSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PurchaseDetail
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
