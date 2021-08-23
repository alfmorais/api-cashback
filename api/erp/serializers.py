# all packages necessary to work serializers
from rest_framework import serializers
from .models import PurchaseDetail


# Define serializers class from PurchaseDetail and Products
class PurchaseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseDetail
        fields = '__all__'
