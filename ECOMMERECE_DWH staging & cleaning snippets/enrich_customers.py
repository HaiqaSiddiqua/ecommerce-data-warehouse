# enrich_customers.py
import pandas as pd
from faker import Faker
import random

fake = Faker()
random.seed(42)

# 1. Load your downloaded customers CSV
df = pd.read_csv("raw_customers.csv")

# 2. Enrich with realistic data
def random_loyalty():
    return random.choices(['Gold', 'Silver', 'Bronze'], weights=[0.1, 0.3, 0.6])[0]

n = len(df)
df['CustomerName'] = [fake.name() for _ in range(n)]
df['Email'] = [fake.email() for _ in range(n)]
df['Gender'] = [random.choice(['M', 'F']) for _ in range(n)]
df['LoyaltyLevel'] = [random_loyalty() for _ in range(n)]
df['SignupDate'] = [fake.date_between(start_date='-5y', end_date='today') for _ in range(n)]
df['City'] = [fake.city() for _ in range(n)]

# 3. Save enriched version
df.to_csv("raw_customers_enriched.csv", index=False)

print("✅ Enriched customer data saved as raw_customers_enriched.csv")
