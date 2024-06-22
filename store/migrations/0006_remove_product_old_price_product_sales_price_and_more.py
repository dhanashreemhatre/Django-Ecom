# Generated by Django 5.0.1 on 2024-06-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_cartitem_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="old_price",
        ),
        migrations.AddField(
            model_name="product",
            name="sales_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=99999999999999, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, default="this is good product", null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="specification",
            field=models.TextField(blank=True, default="Net Quantity:1", null=True),
        ),
    ]