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



