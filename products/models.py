from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=254)
    website = models.URLField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1.00)])
    image = models.ImageField(null=True, blank=True)
    product_spec = models.OneToOneField('Specification', on_delete=models.CASCADE, null=True, blank=True, related_name='related_product')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    accessories = models.ManyToManyField('Accessory', blank=True, related_name='related_product')

    def __str__(self):
        return self.name
    

class Specification(models.Model):
    length = models.DecimalField("Min Length (mm)", max_digits=6, decimal_places=0, null=True, blank=True)
    weight = models.DecimalField("Weight (kg)", max_digits=6, decimal_places=2, null=True, blank=True)
    magazine_capacity = models.PositiveIntegerField("Magazine Capacity (rounds)", null=True, blank=True)
    muzzle_velocity = models.PositiveIntegerField("Muzzle Velocity (FPS)", null=True, blank=True)
    power_system = models.CharField("Powered By", max_length=50, choices=(('gas', 'Gas'), ('electric', 'Electric'), ('spring', 'Spring'), ('co2', 'CO2')), null=True, blank=True)
    ammunition_type = models.CharField("Ammunition Type", max_length=50, choices=(('bb', 'BB'), ('pellet', 'Pellet')), null=True, blank=True)

    def __str__(self):
        return f"Specifications for {self.related_product.name}"
    

class Accessory(models.Model):

    class Meta:
        verbose_name_plural = 'Accessories'

    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1.00)])
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
