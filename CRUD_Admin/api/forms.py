# forms.py
from django import forms
from api.models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_image', 'food_name', 'food_des', 'price']
