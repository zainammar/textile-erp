from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'sale_price',
        'current_stock',
        'status',
    )

    search_fields = ('sku', 'name')
    list_filter = ('category', 'status')