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

    price_choices = (
        ('over_50','over_50'),
        ('over_100','over_100'),
        ('over_150','over_150'),
        ('over_200','over_200'),
        ('over_250','over_250'),
        ('over_300','over_300'),
    )

    product_id = models.ForeignKey('Product', null=True,blank=True, on_delete=models.SET_NULL)
    name =MultiSelectField(choices=price_choices, null=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.product_id)


class Colours (models.Model):

    class Meta:
        verbose_name_plural = 'colours'

    colour_choices = (
        ('Brown','Brown'),
        ('Black','Black'),
        ('White','White'),
        ('Red','Red'),
        ('Blue','Blue'),
        ('Yellow','Yellow'),
        ('Orange','Orange'),
        ('Purple','Purple'),
        ('Green','Green'),
        ('Pink','Pink'),
        ('Gray','Gray'),
    )

    name = MultiSelectField(choices=colour_choices, null=True)
    product_id = models.ForeignKey('Product', null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}, {}'.format(self.name, self.product_id)


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

