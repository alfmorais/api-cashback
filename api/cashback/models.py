from django.db import models


# Create your models here.
class Cashback_API(models.Model):
    """
    This is model to renderize the Cashback_API
    """
    cashback_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=50)
    customer_document = models.CharField(max_length=11)
    customer_document_validated = models.CharField(
        max_length=255)
    cashback_message = models.CharField(max_length=255)
    cashback_amount = models.FloatField()


class Customers(models.Model):
    """
    This is model to check customers document (CPF)
    """
    customer_document = models.CharField(max_length=11)
