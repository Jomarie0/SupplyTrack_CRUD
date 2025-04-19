import csv
from django.core.management.base import BaseCommand
from inventory.models import Product

class Command(BaseCommand):
    help = 'Import products from CSV'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\JOMARIE\Desktop\CAPSTONE-101-SupplyTrack-progress0%\hospital_inventory_sample_2017_2024.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                Product.objects.create(
                    product_id=row["Product ID"],
                    product_name=row["Product Name"],
                    product_type=row["Product Type"],
                    unit_size=row["Unit Size"],
                    brand=row["Brand"],
                    date_received=row["Date"],
                    supplier=row["Supplier"],
                    price=row["Price"],
                    batch_number=row["Batch Number"],
                    expiration_date=row["Expiration Date"]
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} products."))
