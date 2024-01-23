# Generated by Django 3.2.23 on 2024-01-23 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240123_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='related_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_spec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_product', to='products.specification'),
        ),
    ]