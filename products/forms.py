from django import forms
from .models import Product,Price_list


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product


class Price_list(forms.ModelForm):
    class Meta:
        model = Price_list
