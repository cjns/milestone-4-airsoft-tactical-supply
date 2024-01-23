from django.contrib import admin
from .models import Product, Category, Specification, Manufacturer, Accessory


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'manufacturer',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SpecificationAdmin(admin.ModelAdmin):
    list_display = (
        'length',
        'weight',
        'magazine_capacity',
        'muzzle_velocity',
        'power_system',
        'ammunition_type',
    )


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )


class AccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Accessory, AccessoryAdmin)
