# Generated by Django 3.2.23 on 2024-01-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240123_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='accessories',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_product', to='products.Accessory'),
        ),
    ]
