# apps/inventory/forms.py
from django import forms

class UpdateStockForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    transaction_type = forms.ChoiceField(choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')])
