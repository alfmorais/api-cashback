from json import dumps

from cashback.models import Cashback_API, Customers
from cashback.serializers import Cashback_APISerializer, CustomersSerializer
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.test.client import RequestFactory, encode_multipart
from django.urls import reverse
from erp.models import PurchaseDetail
from erp.serializers import PurchaseDetailSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import (APIRequestFactory, APITestCase,
                                 force_authenticate)


class PurchaseDetailTestCase(APITestCase):
    """
    This class will provide test for Purchase Detail
    """

    def test_purchase_detail_get(self):
        url = "http://127.0.0.1:8000/purchase/1/"
        factory = APIRequestFactory()
        request = factory.get(url)

    def test_purchase_detail_post(self):
        data = dumps({
            "customer_document": "20211020210",
            "customer_name": "Joaquim Morais Neto",
            "product_description": "Boneco do Batman",
            "product_value": 150.0,
            "product_quantity": 2,
            "total": 300.0,
            "discount": "A",
        })
        url = "http://127.0.0.1:8000/purchase/"
        factory = APIRequestFactory()
        request = factory.post(url, data)

    def test_purchase_detail_put(self):
        factory = RequestFactory()
        data = dumps({
            "customer_document": "20211020210",
            "customer_name": "Joaquim Morais Neto",
            "product_description": "Boneco do Batman",
            "product_value": 150.0,
            "product_quantity": 2,
            "total": 300.0,
            "discount": "A",
        })
        url = "http://127.0.0.1:8000/purchase/1/"
        request = factory.put(url, data)

    def test_purchase_detail_delete(self):
        url = "http://127.0.0.1:8000/purchase/1/"
        factory = APIRequestFactory()
        request = factory.delete(url)


class CustomersTestCase(APITestCase):
    """
    This classes will provide unit test to customers
    """

    def test_customers_get(self):
        url = "http://127.0.0.1:8000/customers/48/"
        factory = APIRequestFactory()
        request = factory.get(url)

    def test_customers_detail_post(self):
        data = dumps({
            "customer_document": "31748861809",
        })
        url = "http://127.0.0.1:8000/customers/"
        factory = APIRequestFactory()
        request = factory.post(url, data)

    def test_customers_detail_put(self):
        factory = RequestFactory()
        data = dumps({
            "customer_document": "20211020210",
        })
        url = "http://127.0.0.1:8000/customers/48/"
        request = factory.put(url, data)

    def test_customers_detail_delete(self):
        url = "http://127.0.0.1:8000/customers/48/"
        factory = APIRequestFactory()
        request = factory.delete(url)
