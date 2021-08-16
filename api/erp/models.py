from django.db import models


# Create your models here.
# Models applied in ERP API
class PurchaseDetail(models.Model):
    """
    This class are applied Purchase Detail
    """
    sold_at = models.DateTimeField(auto_now=True)
    customer_document = models.CharField(max_length=11)
    customer_name = models.CharField(max_length=50)
    total = models.FloatField()

    def __str__(self):
        return self.customer_name


class Products(models.Model):
    """
    This class are applied in Products 
    """
    DISCOUNT_CHOICES = [
        ('A', 'discount_10%'),
        ('B', 'discount_30%'),
        ('C', 'discount_50%'),
    ]
    purchase_detail = models.ForeignKey(to=PurchaseDetail,
                                        null=True,
                                        blank=True,
                                        on_delete=models.PROTECT)
    discount = models.CharField(choices=DISCOUNT_CHOICES,
                                max_length=255)
    product_value = models.FloatField()
    product_quantity = models.PositiveIntegerField()
