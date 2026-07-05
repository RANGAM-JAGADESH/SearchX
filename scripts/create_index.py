from app.search.index import create_products_index

print("=" * 50)
print("Creating Elasticsearch Index...")
print("=" * 50)

create_products_index()

print("=" * 50)
print("Products Index Created!")
print("=" * 50)