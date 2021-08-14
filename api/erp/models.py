from django.db import models


# Create your models here.
# Models applied in erp api
class PurchaseDetail(models.Model):
    """
    This class are applied Purchase Detail
    """
    sold_at = models.DateTimeField(auto_now=True)
    customer_document = models.CharField(max_length=11)
    customer_name = models.CharField(max_length=50)
    total = models.FloatField()


class Products(models.Model):
    """
    This class are applied in Products 
    """
    DISCOUNT_CHOICES = [
        ('A'),
        ('B'),
        ('C'),
    ]
    purchase_detail = models.ForeignKey(to=PurchaseDetail,
                                        null=True,
                                        blank=True,
                                        on_delete=models.PROTECT)
    discount = models.CharField(choices=DISCOUNT_CHOICES)
    product_value = models.FloatField()
    product_quantity = models.PositiveIntegerField()
