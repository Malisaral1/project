# orders/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """Форма оформления заказа"""
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postal_code']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'checkout-input',
                'placeholder': 'Иван'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'checkout-input',
                'placeholder': 'Иванов'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'checkout-input',
                'placeholder': 'example@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'checkout-input',
                'placeholder': '+7 (999) 000-00-00'
            }),
            'address': forms.Textarea(attrs={
                'class': 'checkout-input',
                'placeholder': 'Улица, дом, квартира',
                'rows': 3
            }),
            'city': forms.TextInput(attrs={
                'class': 'checkout-input',
                'placeholder': 'Москва'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'checkout-input',
                'placeholder': '101000'
            }),
        }