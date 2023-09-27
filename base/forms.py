from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    description = forms.TextInput()

    class Meta:
        model = Order
        fields = ['description']
        labels = {'description': 'توضیحات'}
