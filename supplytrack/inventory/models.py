from django.db import models
from suppliers.models import Supplier
import datetime  # Required for default date setting


# Product model
class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=False, default='P0000')  # Added default
    product_name = models.CharField(max_length=255, default='Unnamed Product')  # Added default
    product_type = models.CharField(max_length=100, default='GenericType')  # Added default
    unit_size = models.CharField(max_length=100, default='N/A')  # Added default
    brand = models.CharField(max_length=100, default='GenericBrand')  # Added default
    date_received = models.DateField(default=datetime.date(2017, 1, 1))  # Changed to DateField with default
    supplier = models.CharField(max_length=255, default='Unknown Supplier')  # Added default
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Added default
    batch_number = models.CharField(max_length=100, default='N/A')  # Added default
    expiration_date = models.DateField(default=datetime.date(2017, 1, 1))  # Changed to DateField with default

    def __str__(self):
        return f"{self.product_name} ({self.product_id})"


# Stock movement (inventory tracking)
class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_movements")
    quantity = models.IntegerField(default=0)  # Added default
    movement_type = models.CharField(
        max_length=50,
        choices=[('IN', 'In'), ('OUT', 'Out')],
        default='IN'  # Default movement type
    )
    date_moved = models.DateField(default=datetime.date(2020, 1, 1))  # Changed to DateField with default

    def __str__(self):
        return f"{self.movement_type} - {self.product.product_name} ({self.quantity})"

    class Meta:
        ordering = ['date_moved']


# Purchase orders
class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.date(2020, 1, 1))  # Changed to DateField with default
    expected_delivery = models.DateField(default=datetime.date(2021, 1, 1))  # Changed to DateField with default
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Canceled", "Canceled")],
        default="Pending"
    )

    def __str__(self):
        return f"Order {self.id} - {self.supplier.name}"
