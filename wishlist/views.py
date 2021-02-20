from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Wishlist, WishItems, UserWishlist
from profiles.models import UserProfile

from products.models import Product

# Create your views here.


def view_wishlist(request):
    """ Added a views to show the Wishlist """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(UserWishlist, user=user)
    wishlist_items = wishlist.products.all()
    print(wishlist_items)

    context = {
        'user': user,
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):

    product = Product.objects.get(pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist, created = UserWishlist.objects.get_or_create(user=user)
    user_wishlist.products.add(product)
    user_wishlist.save()

    context = {
        'user': user,
        'wishlist': user_wishlist,
        'wishlist_items': user_wishlist.products.all(),
    }

    return render(request, 'wishlist/wishlist.html', context)




