import pandas as pd
from pathlib import Path
from datetime import datetime

from app.db.database import SessionLocal
from app.models.product import Product

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "datasets" / "products.csv"

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(csv_file)

print(f"Total Records Found : {len(df)}")

print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)
print(df.columns.tolist())

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("FIRST ROW AS DICTIONARY")
print("=" * 60)
print(df.iloc[0].to_dict())

print("\n" + "=" * 60)
print("CSV FILE PATH")
print("=" * 60)
print(csv_file)

db = SessionLocal()

success = 0
failed = 0

for index, row in df.iterrows():

    try:

        product = Product(
            product_id=str(row["product_id"]),
            title=str(row["title"]),
            description=str(row["description"]),
            brand=str(row["brand"]),
            category=str(row["category"]),
            price=float(row["price"]),
            rating=float(row["rating"]),
            stock=int(row["stock"]),
            image_url=str(row["image_url"]),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        db.add(product)

        success += 1

        if success % 500 == 0:
            db.commit()
            print(f"Imported {success} products...")

    except Exception as e:

        failed += 1

        print(f"\n❌ Row {index} failed")
        print("Row Data:")
        print(row.to_dict())
        print("Error:")
        print(e)

db.commit()
db.close()

print("=" * 60)
print("IMPORT COMPLETED")
print("=" * 60)
print(f"Success : {success}")
print(f"Failed  : {failed}")
print("=" * 60)