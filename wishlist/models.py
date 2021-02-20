from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserWishlist(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_owner')
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.name





