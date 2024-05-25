# forms.py
from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['realtor', 'title', 'address', 'city', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'squaremeters', 'lot_size', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published']
