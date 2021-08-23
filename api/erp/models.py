from django.db import models


# Create your models here.
# Models applied in ERP API
class PurchaseDetail(models.Model):
    """
    This class are applied Purchase Detail
    """
    DISCOUNT_CHOICES = [
        ('A', 'discount_10%'),
        ('B', 'discount_30%'),
        ('C', 'discount_50%'),
    ]
    sold_at = models.DateTimeField(auto_now=True)
    customer_document = models.CharField(max_length=11)
    customer_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100, default='')
    product_value = models.FloatField()
    product_quantity = models.PositiveIntegerField()
    total = models.FloatField()
    discount = models.CharField(choices=DISCOUNT_CHOICES,
                                max_length=255)
