from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=False, related_name='wishlist')
    wishlist_products = models.ManyToManyField(Product, through='wishItems')

    def __str__(self):
        return f'Wishlist ({self.user},)'


class WishItems(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_items' )
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='product_wishlist')

    def __str__(self):
        return self.product.name



