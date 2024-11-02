from django.db import models
from django.utils import timezone

class Stock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def update_quantity(self, quantity, transaction_type):
        """Adjust stock quantity and create a transaction record."""
        if transaction_type == 'IN':
            self.quantity += quantity
        elif transaction_type == 'OUT':
            self.quantity -= quantity
        self.save()
        # Record transaction
        StockTransaction.objects.create(stock=self, transaction_type=transaction_type, quantity=quantity)

class StockTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out')
    ]
    
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type} - {self.stock.name} - {self.quantity}"
