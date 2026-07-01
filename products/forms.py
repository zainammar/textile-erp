from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'sku',
            'name',
            'category',
            'purchase_price',
            'sale_price',
            'opening_stock',
            'current_stock',
            'minimum_stock',
            'description',
            'status',
        ]

        widgets = {
            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Code'
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'purchase_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'sale_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'opening_stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'current_stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'minimum_stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }