import json

from cashback.models import Cashback_API, Customers
from cashback.serializers import Cashback_APISerializer, CustomersSerializer
from django.contrib.auth.models import User
from django.urls import reverse
from erp.models import PurchaseDetail
from erp.serializers import PurchaseDetailSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
