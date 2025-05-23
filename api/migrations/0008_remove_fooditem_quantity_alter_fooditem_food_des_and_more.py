# Generated by Django 5.2 on 2025-05-15 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_fooditem_price_fooditem_quantity_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fooditem",
            name="quantity",
        ),
        migrations.AlterField(
            model_name="fooditem",
            name="food_des",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="fooditem",
            name="food_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="food",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="foods",
                to="api.fooditem",
            ),
        ),
    ]
