# Projeto API Cashback

## Introdução

O projeto de desenvolvimento da API (Application Programming Interface) tem como objetivo, receber dados de um sistema ERP varejista e calcular o valor de cashback para o cliente de acordo com a regra de negócio. Para mais detalhes do projeto, consulte a [proposta técnica](files/readme.md).

## Stacks Utilizadas:

<p>Frameworks utilizado no desenvolvimento do projeto:</p>

1. Django
2. Django Rest Framework
3. SQLite3

## Preparação do Ambiente: 

<p>O módulo <b>venv</b> fornece soluções para criar ambientes virtuais isolado do diretória do sistema. A principal vantagem é isolar o <b>venv</b> do Sistema Operacional, para evitar conflitos de pacotes e bibliotecas.</p>

### Criar um Ambiente Virtual

Os seguintes passos descreve como criar um ambiente virtual no sistema operacional Windowns. Para informações de MacOS e Unix, porfavor consulte a documentação para [Criação de Ambientes Virtuais](https://docs.python.org/pt-br/3/library/venv.html).

~~~cmd
mkdir API-CASHBACK

cd API-CASHBACK

python -m venv api-cashback
~~~

### Ativando o Ambiente Virtual

~~~cmd
api-cashback/Scripts/Activate
~~~

<p>Deve aparecer a palavra (api-cashback) na cor verde, indicando que o ambiente virtual está ativado.</p>

![Text Alt](files/venv.png)

## Instalação dos Pacotes e Bibliotecas:

## Iniciando o projeto:

1. Iniciando o projeto Django. 

~~~cmd
django-admin startproject api
~~~

2. Iniciando as aplicações.

~~~cmd
django-admin startapp cashback
django-admin startapp erp
~~~

## Configurando o projeto:

## Definindo o banco de dados no models.py

Definindo o banco de dados no arquivo models.py da primeira API ERP.

~~~python
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
~~~ 

Definindo o banco de dados no arquivo models.py da segunda API Cashback

~~~python
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
~~~

## Definindo o serialiazers.py

Definição de Serializer: 
[Serialização é o processo de transformar dados em um formato que pode ser armazenado ou transmitido e, então, reconstruído. Ele é usado em todas as partes do desenvolvimento de aplicações, ou quando estamos armazenando dados numa base de dados, na memória ou convertendo-os em arquivos.](https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/)

Codificando o serializer da aplicação API ERP.

~~~python
# all packages necessary to work serializers
from rest_framework import serializers
from .models import PurchaseDetail


# Define serializers class from PurchaseDetail and Products
class PurchaseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseDetail
        fields = '__all__'
~~~

Codificando o serializer da aplicação API Cashback

~~~python
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
~~~

## Definindo o viewsets.py

No arquivo viewsets.py será responsável por toda a lógica da API ERP e CASHBACK. No caso a lógica será definida sobrescrevendo o metódo CREATE. 

Definindo a lógica da primeira API ERP.

~~~python
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PurchaseDetailSerializer
from .models import PurchaseDetail
from rest_framework import permissions
from .functions import (check_cpf_digits,
                        check_cpf_isvalid,
                        cashback_calculate,
                        calculate_check
                        )
from cashback.models import Cashback_API
from django.utils import timezone


# define viewsets for classes created on serializers.py
class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PurchaseDetail.objects.all()

    def create(self, request, *args, **kwargs):
        """
        This function will provide double check for customers documents
        and return true in case of sucessuful validated. 
        """

        # Request data from POST API
        data = request.data

        # Organize all variables to start the process to validate all data
        customer_document = data["customer_document"]
        customer_name = data["customer_name"]
        product_description = data["product_description"]
        product_value = data["product_value"]
        product_quantity = data["product_quantity"]
        total = data["total"]
        discount = data["discount"]

        # cashback time
        cashback_data = timezone.now()

        # create the database
        PurchaseDetail.objects.create(
            customer_document=customer_document,
            customer_name=customer_name,
            product_description=product_description,
            product_value=product_value,
            product_quantity=product_quantity,
            total=total,
            discount=discount,
        )

        # validate customers document
        validate_customers_document = check_cpf_digits(customer_document)
        validate_total = calculate_check(product_quantity,
                                         product_value,
                                         total)

        # Conditional of the program to save data in Cashback_API
        if (validate_customers_document and validate_total) == True:
            message = "Customers Document was sucessuful validated"
            cashback_message = "Cashback was sucessuful calculated"
            cashback_amount = cashback_calculate(
                discount,
                product_value,
                product_quantity)
            Cashback_API.objects.create(
                cashback_date=cashback_data,
                customer_name=customer_name,
                customer_document=customer_document,
                customer_document_validated=message,
                cashback_message=cashback_message,
                cashback_amount=cashback_amount
            )
            return Response('The data was received and save in our database')
        else:
            message = "Customers Document error validated"
            cashback_message = "It wasn't possible to calculate cashback amount"
            Cashback_API.objects.create(
                cashback_date=cashback_data,
                customer_name=customer_name,
                customer_document=customer_document,
                customer_document_validated=message,
                cashback_message=cashback_message,
                cashback_amount=0.0
            )
            return Response('The data was received and save in our database')
~~~

Definindo a lógica da segunda API Cashback

~~~python
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomersSerializer
from .models import Customers, Cashback_API
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum


# define viewsets for classes created on serializers.py
class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customers.objects.all()

    def create(self, request, format=None):
        """
        This method CREATE function will responsable for
        show all cashback value by customers
        """

        # Request data from POST API
        data = request.data

        # request value from POST method
        customer_document = data["customer_document"]

        # save data in database
        Customers.objects.create(
            customer_document=customer_document
        )

        # getting database only
        database = Cashback_API.objects.filter(
            customer_document=customer_document
        )

        # getting variables regarding to cashback API response
        customer_name = database.values("customer_name").latest("id")
        customer_document = database.values("customer_document").latest("id")
        cashback_per_purchase_detail = database.values_list(
            "cashback_amount").order_by("id")
        cashback_total = database.aggregate(Sum("cashback_amount"))

        # that response will be in charge of the reply some consult
        # for checking how much cashback some customer have in our
        # database. The answer will provide a full information
        # to accomplish targets from API 2
        return Response({
            "customer_name": customer_name,
            "customer_document": customer_document,
            "cashback_per_purchase_detail": cashback_per_purchase_detail,
            "cashback_total": cashback_total,
        })
~~~

## Trabalhando com Routers na urls.py

A função Routers do Django Rest Framework facilita a protipagem de URL dinâmica de acordo com as classes configurada no projeto. Essa função é utilizada no arquivo urls.py do diretório principal da aplicação.

~~~python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from erp import (viewsets, serializers, views)
from cashback.viewsets import CustomersViewSet


# to define routes for ERP API
route = routers.DefaultRouter()


# defined routes to ERP API models Purchase Detail
# Purchase Detail
route.register(r'purchase', viewsets.PurchaseDetailViewSet,
               basename="PurchaseDetail")


# Customers
route.register(r'customers', CustomersViewSet,
               basename="Customers")


# The urlpatterns list show the all possibilities to access the API url
urlpatterns = [
    path('admin/', admin.site.urls),
    # url standard from Django Rest Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url from ERP | Cashback API
    path('', include(route.urls)),
]
~~~

## Lógica da API

O fluxograma abaixo demonstra o funcionamento da API. 

![Text Alt](files/flowchart.png)

## Cálculo de Cashback

## Verificando o CPF do Cliente

## Como usar a API

## Verificando o banco de dados

## Testes

## Agradecimentos

## Referências Bibliográficas

1. [Documentação do Django](https://docs.djangoproject.com/en/3.2/)
2. [Documentação do Django Rest Framework](https://www.django-rest-framework.org/)
3. [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/)
4. [Guia Básico de Markdown](https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown#open)
5. [Criação de Ambientes Virtuais](https://docs.python.org/pt-br/3/library/venv.html)
