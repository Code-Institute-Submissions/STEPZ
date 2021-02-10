from django.db import models

# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here


class Category (models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Price_list (models.Model):

    class Meta:
        verbose_name_plural = 'PriceList'

    name = models.CharField(max_length=254, default='1')

    def __str__(self):
        return '{}'.format(self.name)


class Colours (models.Model):

    class Meta:
        verbose_name_plural = 'colours'

    colour_choices = (
        ('Brown','Brown'),
        ('Black','Black'),
        ('White','White'),
        ('Red','Red'),
        ('Blue','Blue'),
        ('Pink','brown'),
        ('Yellow','Yellow'),
        ('Orange','Orange'),
        ('Purple','Purple'),
         ('Green','Green'),
    )

    name = MultiSelectField(choices=colour_choices, null=True)
    product_id = models.ForeignKey('Product', null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}, {}'.format(self.name, self.product_id)


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price_list = models.ForeignKey('Price_list', null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
         return '{}, {}'.format(self.name, self.price_list)
