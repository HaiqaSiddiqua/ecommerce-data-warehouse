# enrich_products.py
import pandas as pd
from faker import Faker
import random
import re

fake = Faker()
random.seed(123)

# 1. Load your downloaded products CSV
df = pd.read_csv("raw_products.csv")

# 2. Define category mapping
def assign_category(desc):
    d = (str(desc) or "").upper()
    if re.search(r'MUG|CUP|TEA|COFFEE', d):
        return 'Kitchen'
    if re.search(r'LAMP|LANTERN|LIGHT|BULB', d):
        return 'Lighting'
    if re.search(r'HEART|COAT|HANGER|CUSHION|HOME', d):
        return 'Home Decor'
    if re.search(r'SOCK|SCARF|HAT|GLOVE', d):
        return 'Apparel'
    if re.search(r'BATTERY|USB|CHARGER|ELECTR', d):
        return 'Electronics'
    return 'Misc'

# 3. Enrich
df['Category'] = df['Description'].apply(assign_category)
df['Supplier'] = [fake.company() for _ in range(len(df))]
df['Brand'] = [fake.word().title() for _ in range(len(df))]
df['LaunchDate'] = [fake.date_between(start_date='-3y', end_date='today') for _ in range(len(df))]
df['ReorderLevel'] = [random.randint(10, 200) for _ in range(len(df))]

# 4. Save enriched version
df.to_csv("raw_products_enriched.csv", index=False)

print("✅ Enriched product data saved as raw_products_enriched.csv")
