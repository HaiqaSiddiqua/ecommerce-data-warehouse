# shipping_generator_local.py
import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Initialize Faker and random
fake = Faker()
random.seed(42)

# Load your sales CSV (adjust filename if different)
sales = pd.read_csv("raw_sales.csv", encoding="latin1")

# Select only InvoiceNo and InvoiceDate
sales = sales[['InvoiceNo', 'InvoiceDate']].dropna().drop_duplicates()

# Convert InvoiceDate to datetime
sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'], errors='coerce')
sales = sales.dropna(subset=['InvoiceDate'])

# Limit to smaller sample if needed
sales = sales.head(5000)  # adjust this number as you like

couriers = ["Royal Mail", "DHL", "FedEx", "UPS", "Hermes"]
statuses = ["Delivered", "In Transit", "Returned", "Cancelled"]

rows = []

for _, r in sales.iterrows():
    invoice = r['InvoiceNo']
    ship_date = r['InvoiceDate'] + pd.to_timedelta(random.randint(0, 2), unit='D')
    delivery_offset = random.choice([1, 2, 3, 4, 5, 6, 7])
    delivery = ship_date + pd.to_timedelta(delivery_offset, unit='D')
    courier = random.choice(couriers)
    cost = round(max(0.0, random.gauss(5.0, 2.0)), 2)
    status = "Delivered" if delivery <= pd.Timestamp.today() else random.choice(statuses)

    rows.append({
        "InvoiceNo": invoice,
        "ShipmentDate": ship_date.date(),
        "DeliveryDate": delivery.date(),
        "Courier": courier,
        "ShippingCost": cost,
        "Status": status
    })

# Create DataFrame and save
shipping_df = pd.DataFrame(rows)
shipping_df.to_csv("shipping_data.csv", index=False)

print("✅ Shipping data generated successfully! Saved as shipping_data.csv")
