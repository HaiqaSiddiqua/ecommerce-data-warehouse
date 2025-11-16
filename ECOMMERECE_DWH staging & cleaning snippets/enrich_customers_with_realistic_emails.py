import pandas as pd
import random
import re

# Load the existing enriched CSV
df = pd.read_csv("raw_customers_enriched.csv")

# Function to safely extract first name from CustomerName
def extract_first_name(full_name):
    # Split on space and remove non-alphabetic characters
    parts = re.split(r'\s+', str(full_name).strip())
    if len(parts) > 0:
        return re.sub(r'[^a-zA-Z]', '', parts[0]).lower()
    return "user"

# Function to create realistic email
def create_realistic_email(name):
    first_name = extract_first_name(name)
    num = random.randint(100, 999)
    domain = random.choice(["example.com", "example.net", "example.org"])
    return f"{first_name}{num}@{domain}"

# Apply email generation
df['Email'] = [create_realistic_email(name) for name in df['CustomerName']]

# Optional: make sure there are no duplicates
df['Email'] = df['Email'].str.lower()
df.drop_duplicates(subset=['Email'], inplace=True)

# Save updated CSV
df.to_csv("raw_customers_enriched.csv", index=False)

print("✅ Customer emails updated to realistic format and saved successfully!")
