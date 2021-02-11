from django.contrib import admin
from .models import Product, Category, Colours


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

class ColoursAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
    )


admin.site.register(Colours, ColoursAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


