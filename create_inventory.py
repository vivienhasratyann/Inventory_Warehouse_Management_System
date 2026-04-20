import csv
import os

# Make sure the data folder exists
os.makedirs("data", exist_ok=True)

# Sample inventory data
inventory_data = [
    {"product_id": 1001, "name": "Wireless Mouse", "category": "Electronics", "quantity": 45, "price": 29.99},
    {"product_id": 1002, "name": "Mechanical Keyboard", "category": "Electronics", "quantity": 23, "price": 89.99},
    {"product_id": 1003, "name": "USB-C Cable", "category": "Accessories", "quantity": 120, "price": 12.99},
    {"product_id": 1004, "name": "27-inch Monitor", "category": "Electronics", "quantity": 8, "price": 249.99},
    {"product_id": 1005, "name": "Laptop Stand", "category": "Furniture", "quantity": 32, "price": 45.99},
    {"product_id": 1006, "name": "Screen Protector", "category": "Accessories", "quantity": 67, "price": 9.99},
    {"product_id": 1007, "name": "External Hard Drive", "category": "Electronics", "quantity": 15, "price": 79.99},
    {"product_id": 1008, "name": "Desk Lamp", "category": "Furniture", "quantity": 19, "price": 34.99},
    {"product_id": 1009, "name": "Webcam", "category": "Electronics", "quantity": 11, "price": 59.99},
    {"product_id": 1010, "name": "Phone Charger", "category": "Accessories", "quantity": 88, "price": 19.99},
    {"product_id": 1011, "name": "Notebook", "category": "Supplies", "quantity": 150, "price": 4.99},
    {"product_id": 1012, "name": "Pen Set", "category": "Supplies", "quantity": 200, "price": 7.99},
    {"product_id": 1013, "name": "Stapler", "category": "Supplies", "quantity": 42, "price": 12.99},
    {"product_id": 1014, "name": "Desk Organizer", "category": "Furniture", "quantity": 28, "price": 24.99},
    {"product_id": 1015, "name": "USB Hub", "category": "Accessories", "quantity": 34, "price": 27.99},
    {"product_id": 1016, "name": "HDMI Cable", "category": "Accessories", "quantity": 95, "price": 8.99},
    {"product_id": 1017, "name": "Wireless Headphones", "category": "Electronics", "quantity": 17, "price": 79.99},
    {"product_id": 1018, "name": "Mouse Pad", "category": "Accessories", "quantity": 73, "price": 14.99},
    {"product_id": 1019, "name": "Laptop Backpack", "category": "Accessories", "quantity": 21, "price": 49.99},
    {"product_id": 1020, "name": "Power Bank", "category": "Electronics", "quantity": 38, "price": 39.99},
    {"product_id": 1021, "name": "Document Holder", "category": "Furniture", "quantity": 14, "price": 18.99},
    {"product_id": 1022, "name": "Desk Mat", "category": "Furniture", "quantity": 26, "price": 29.99},
    {"product_id": 1023, "name": "Cable Ties", "category": "Accessories", "quantity": 250, "price": 5.99},
    {"product_id": 1024, "name": "Laptop Sleeve", "category": "Accessories", "quantity": 31, "price": 24.99},
    {"product_id": 1025, "name": "USB Flash Drive", "category": "Electronics", "quantity": 112, "price": 15.99},
]

# Write to CSV file
filename = "data/inventory.csv"

with open(filename, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['product_id', 'name', 'category', 'quantity', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(inventory_data)

print(f"✓ Successfully created {filename}")
print(f"✓ Added {len(inventory_data)} products")
print("\nFirst 5 products:")
for i, product in enumerate(inventory_data[:5]):
    print(f"  {i+1}. ID: {product['product_id']} - {product['name']}")