# traffic_generator_local.py
import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(123)

# Load your sales CSV
sales = pd.read_csv("raw_sales.csv", encoding="latin1")

# Extract distinct dates and countries
sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'], errors='coerce')
sales = sales.dropna(subset=['InvoiceDate', 'Country'])

dates_countries = sales[['InvoiceDate', 'Country']].drop_duplicates()

rows = []
for _, r in dates_countries.iterrows():
    date = r['InvoiceDate'].date()
    country = r['Country']

    pageviews = int(max(100, random.gauss(1500, 800)))
    unique_visitors = int(pageviews * random.uniform(0.4, 0.8))
    avg_session_duration = round(random.uniform(1.0, 4.5), 2)

    rows.append({
        "Date": date,
        "Country": country,
        "PageViews": pageviews,
        "UniqueVisitors": unique_visitors,
        "AvgSessionDuration": avg_session_duration
    })

traffic_df = pd.DataFrame(rows)
traffic_df.to_csv("website_traffic.csv", index=False)

print("✅ Website traffic data generated successfully! Saved as website_traffic.csv")
