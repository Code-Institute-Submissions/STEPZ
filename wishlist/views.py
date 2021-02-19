from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Wishlist, WishItems
from profiles.models import UserProfile

# Create your views here.


def view_wishlist(request):
    """ Added a views to show the Wishlist """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(Wishlist, user=user)
    wishlist_items = get_list_or_404(WishItems, wishlist=wishlist)
    print(wishlist_items)

    context = {
        'user': user,
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)

