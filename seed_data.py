import os
import django

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from chat.models import Order, Invoice

def seed_db():
    print("🌱 Seeding database...")

    # Clear existing data to avoid duplicates
    Order.objects.all().delete()
    Invoice.objects.all().delete()

    # 2. Create Mock Orders
    orders = [
        {'order_id': 'ORD101', 'item': 'MacBook Pro M3', 'status': 'Shipped'},
        {'order_id': 'ORD102', 'item': 'Sony WH-1000XM5', 'status': 'Processing'},
        {'order_id': 'ORD103', 'item': 'Keychron K2 Keyboard', 'status': 'Delivered'},
        {'order_id': 'ORD104', 'item': 'Logitech MX Master 3S', 'status': 'In Transit'},
    ]

    for o in orders:
        Order.objects.create(**o)
        print(f"✅ Created Order: {o['order_id']}")

    # 3. Create Mock Invoices
    invoices = [
        {'invoice_id': 'INV-5001', 'amount': 2499.00, 'is_paid': True},
        {'invoice_id': 'INV-5002', 'amount': 350.50, 'is_paid': False},
        {'invoice_id': 'INV-5003', 'amount': 99.00, 'is_paid': True},
    ]

    for i in invoices:
        Invoice.objects.create(**i)
        print(f"✅ Created Invoice: {i['invoice_id']}")

    print("\n✨ Database seeding complete! Your agents now have data to find.")

if __name__ == "__main__":
    seed_db()