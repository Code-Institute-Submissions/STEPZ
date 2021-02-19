from django.shortcuts import render
from .models import Wishlist, WishItems

# Create your views here.


def view_wishlist(request):

    return render(request, 'wishlist/wishlist.html')


