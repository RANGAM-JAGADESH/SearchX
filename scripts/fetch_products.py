import requests
import pandas as pd
import os

from app.services.normalizer import (
    normalize_dummyjson,
    normalize_fakestore
)

print("=" * 60)
print("Fetching Products...")
print("=" * 60)

rows = []

# ==========================================================
# DummyJSON
# ==========================================================

print("\nFetching Products from DummyJSON...")

dummy_url = "https://dummyjson.com/products?limit=200"

response = requests.get(dummy_url)

if response.status_code == 200:

    dummy_products = response.json()["products"]

    print(f"Fetched {len(dummy_products)} products")

    for product in dummy_products:
        rows.append(normalize_dummyjson(product))

else:
    print("DummyJSON API Failed")


# ==========================================================
# FakeStore
# ==========================================================

print("\nFetching Products from FakeStore...")

fake_url = "https://fakestoreapi.com/products"

response = requests.get(fake_url)

if response.status_code == 200:

    fake_products = response.json()

    print(f"Fetched {len(fake_products)} products")

    for product in fake_products:
        rows.append(normalize_fakestore(product))

else:
    print("FakeStore API Failed")


# ==========================================================
# Save CSV
# ==========================================================

df = pd.DataFrame(rows)

os.makedirs("datasets", exist_ok=True)

output_file = "datasets/products.csv"

df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("CSV Saved Successfully")
print(output_file)
print(f"Total Products : {len(rows)}")
print("=" * 60)