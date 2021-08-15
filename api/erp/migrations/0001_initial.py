# Generated by Django 3.2.6 on 2021-08-15 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_at', models.DateTimeField(auto_now=True)),
                ('customer_document', models.CharField(max_length=11)),
                ('customer_name', models.CharField(max_length=50)),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(choices=[('A', 'discount_10%'), ('B', 'discount_30%'), ('C', 'discount_50%')], max_length=255)),
                ('product_value', models.FloatField()),
                ('product_quantity', models.PositiveIntegerField()),
                ('purchase_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='erp.purchasedetail')),
            ],
        ),
    ]
