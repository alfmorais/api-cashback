# Generated by Django 3.2.6 on 2021-08-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_description',
            field=models.CharField(default='product', max_length=100),
        ),
    ]