from django.db import models


class Customer(models.Model):
    """A model representing a customer."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# from django.db import models

# class Supplier(models.Model):
#     name = models.CharField(max_length=255)
#     contact_name = models.CharField(max_length=255, null=True, blank=True)
#     phone_number = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     website = models.URLField(null=True, blank=True)
#     supplier_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
#     tax_id = models.CharField(max_length=50, null=True, blank=True)
#     payment_terms = models.CharField(max_length=100, null=True, blank=True)
#     notes = models.TextField(null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
