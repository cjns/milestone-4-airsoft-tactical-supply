# Generated by Django 3.2.23 on 2024-01-23 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
        migrations.AddField(
            model_name='product',
            name='product_spec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.specification'),
        ),
        migrations.AddField(
            model_name='specification',
            name='related_product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]