from django.contrib import admin
from .models import Product, Category, Price_list, Colours


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class Price_listAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
    )


class ColoursAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
    )


admin.site.register(Colours, ColoursAdmin)
admin.site.register(Price_list, Price_listAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


