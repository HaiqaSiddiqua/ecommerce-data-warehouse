# enrich_dim_product_brands.py
import pandas as pd
import random
import os

# 1️⃣ Define the exact filename (update this if needed)
file_path = "dim_product.csv"

# 2️⃣ Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found: {file_path}. Please check your folder name and file path.")

# 3️⃣ Load the dim_product table
df = pd.read_csv(file_path)
print(f"✅ Loaded {len(df)} rows from {file_path}")

# 4️⃣ Show a quick sample before change
print("\n🔍 Before update (first 5 brands):")
print(df['Brand'].head(5).tolist())

# 5️⃣ Define realistic brand names
real_brands = [
    "IKEA", "Nike", "Adidas", "Apple", "Samsung", "Sony", "Dell", "HP",
    "Canon", "Lenovo", "Microsoft", "Philips", "LG", "Panasonic",
    "Puma", "Reebok", "H&M", "Zara", "Unilever", "Nestle",
    "Levi’s", "AmazonBasics", "ASUS", "Beats", "Bose",
    "JBL", "Crocs", "KitchenAid", "Whirlpool", "Vans"
]

# 6️⃣ Assign random realistic brand to each product
random.seed(42)
df['Brand'] = [random.choice(real_brands) for _ in range(len(df))]

# 7️⃣ Save back to same file (overwrite)
df.to_csv(file_path, index=False)

# 8️⃣ Confirm update
print("\n✅ Brand column updated successfully in dim_product.csv!")
print("🔍 After update (first 5 brands):")
print(df['Brand'].head(5).tolist())
