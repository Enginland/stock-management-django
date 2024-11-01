from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'phone_number', 'email', 'address', 'website', 'supplier_code', 'tax_id', 'payment_terms', 'notes']
        widgets = {
            'website': forms.URLInput(attrs={'placeholder': 'Optional'}),  # Use URLInput instead of WebsiteInput
        }