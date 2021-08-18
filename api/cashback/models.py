from django.db import models


# Create your models here.
class Cashback_API(models.Model):
    """
    This is model to renderize the Cashback_API
    """
    customer_name = models.CharField(max_length=50)
    customer_document = models.CharField(max_length=11)
    message = models.CharField(max_length=255)
    cashback_amount = models.FloatField(default=0)


class Customers(models.Model):
    """
    This is model to check customers document (CPF)
    """
    customer_document = models.CharField(max_length=11)
