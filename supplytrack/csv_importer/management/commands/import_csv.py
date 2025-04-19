import csv
from django.core.management.base import BaseCommand
from inventory.models import Product
import datetime  # Required for date conversion

class Command(BaseCommand):
    help = 'Import products from CSV'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\JOMARIE\Desktop\CAPSTONE-101-SupplyTrack-progress0%\hospital_inventory_sample_2017_2024.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                # Update this line to match your actual CSV header column
                try:
                    date_received = datetime.datetime.strptime(row["date_received"], "%Y-%m-%d").date()  # Change "Date" to the correct header
                    expiration_date = datetime.datetime.strptime(row["expiration_date"], "%Y-%m-%d").date()
                except ValueError as e:
                    self.stdout.write(self.style.WARNING(f"Skipping row {row['product_id']} due to date parsing error: {e}"))
                    continue  # Skip this row if there's a date parsing error
                
                # Create Product entry
                Product.objects.create(
                    product_id=row["product_id"],
                    product_name=row["product_name"],
                    product_type=row["product_type"],
                    unit_size=row["unit_size"],
                    brand=row["brand"],
                    date_received=date_received,  # Use the converted date
                    supplier=row["supplier"],
                    price=row["price"],
                    batch_number=row["batch_number"],
                    expiration_date=expiration_date  # Use the converted date
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} products."))
