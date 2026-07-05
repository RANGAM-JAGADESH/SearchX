from app.search.sync import sync_products

print("=" * 60)
print("Syncing Products to Elasticsearch...")
print("=" * 60)

sync_products()

print("=" * 60)