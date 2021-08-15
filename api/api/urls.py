from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from erp import viewsets
from erp import serializers


# to define routes for ERP API
route = routers.DefaultRouter()


# defined routes to ERP API models Purchase Detail
# Purchase Detail
route.register(r'purchase', viewsets.PurchaseDetailViewSet,
               basename="PurchaseDetail")

# Products
route.register(r'products', viewsets.ProductsViewSet,
               basename="Products")

# The urlpatterns list show the all possibilities to access the API url
urlpatterns = [
    path('admin/', admin.site.urls),
    # url standard from Django Rest Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url from ERP API
    path('', include()),
]
