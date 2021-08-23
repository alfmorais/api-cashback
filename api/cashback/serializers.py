# all packages necessary to work serializers
from rest_framework import serializers
from .models import Customers, Cashback_API


# Define serializers class from Customers
class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = '__all__'


class Cashback_APISerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashback_API
        fields = '__all__'
