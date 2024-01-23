from django.contrib import admin
from .models import Product, Category, Specification, Manufacturer, Accessory


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Specification)
admin.site.register(Manufacturer)
admin.site.register(Accessory)
