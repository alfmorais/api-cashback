# all packages necessary to work serializers
from rest_framework import serializers
from .models import Customers


# Define serializers class from Customers
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
