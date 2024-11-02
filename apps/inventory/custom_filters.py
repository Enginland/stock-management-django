# apps/inventory/templatetags/custom_filters.py
from django import template
from django.utils.formats import number_format

register = template.Library()

@register.filter
def currency(value):
    """Format a number as currency."""
    return f"${number_format(value, 2)}"
