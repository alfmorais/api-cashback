# all packages necessary to work serializers
from rest_framework import serializers
from .models import Customers, Cashback_API


# Define serializers class from Customers
class CustomersSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Customers
        fields = '__all__'


class Cashback_APISerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cashback_API
        fields = '__all__'
