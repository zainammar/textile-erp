from django.db import models
from decimal import Decimal
from categories.models import Category


class Product(models.Model):

    PRICE_OPTION = (
        ('same', 'Same Price'),
        ('30', 'Add 30%'),
        ('expense', 'Calculate From Expenses'),
    )

    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Dates
    purchase_date = models.DateField(null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)

    # Price Calculation Option
    price_option = models.CharField(
        max_length=20,
        choices=PRICE_OPTION,
        default='same'
    )

    # Expenses
    expense1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense4 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense5 = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    opening_stock = models.PositiveIntegerField(default=0)
    current_stock = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True, null=True)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):

        if self.price_option == "same":
            self.sale_price = self.purchase_price

        elif self.price_option == "30":
            self.sale_price = self.purchase_price * Decimal("1.30")

        elif self.price_option == "expense":
            total_expense = (
                self.expense1 +
                self.expense2 +
                self.expense3 +
                self.expense4 +
                self.expense5
            )

            self.sale_price = self.purchase_price + total_expense

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name