from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='wishlist'),
    path('add/<product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<product_id>/', views.delete_wishlist, name='delete_wishlist'),
]
