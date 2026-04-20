# ============================================
# FILE: file_manager.py
# AUTHOR: Emilya Karapetyan
# PURPOSE: CSV file operations for inventory system
# ============================================

import csv
import os


def load_inventory(filename, avl_tree):
    """
    Load products from CSV file into AVL tree.
    Returns number of products loaded.
    """
    if not os.path.exists(filename):
        print(f"⚠ File not found: {filename}")
        print("  Starting with empty inventory.")
        return 0

    loaded_count = 0
    error_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Verify required columns exist
            required = {'product_id', 'name', 'category', 'quantity', 'price'}
            if not required.issubset(reader.fieldnames):
                missing = required - set(reader.fieldnames)
                print(f"✗ CSV missing columns: {missing}")
                return 0

            for row_num, row in enumerate(reader, start=2):
                try:
                    product_id = int(row['product_id'].strip())
                    name = row['name'].strip()
                    category = row['category'].strip()
                    quantity = int(row['quantity'].strip())
                    price = float(row['price'].strip())

                    avl_tree.insert(product_id, name, category, quantity, price)
                    loaded_count += 1

                except ValueError as e:
                    error_count += 1
                    print(f"✗ Row {row_num} skipped: {e}")
                except Exception as e:
                    error_count += 1
                    print(f"✗ Row {row_num} unexpected error: {e}")

    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
        return 0
    except PermissionError:
        print(f"✗ Permission denied: {filename}")
        return 0
    except Exception as e:
        print(f"✗ Failed to open file: {e}")
        return 0

    print(f"✓ Loaded {loaded_count} products from {filename}")
    if error_count > 0:
        print(f"  ({error_count} rows skipped due to errors)")
    return loaded_count


def save_inventory(filename, avl_tree):
    """
    Save all products from AVL tree to CSV file.
    Returns number of products saved.
    """
    products = []  # ← DEFINE HERE FIRST (FIX)

    try:
        products = avl_tree.inorder_traversal()
    except AttributeError:
        # Fallback: collect manually
        def collect(node):
            if node:
                collect(node.left)
                products.append({
                    'product_id': node.product_id,
                    'name': node.name,
                    'category': node.category,
                    'quantity': node.quantity,
                    'price': node.price
                })
                collect(node.right)

        collect(avl_tree.root)

    if not products:
        print(" No products to save.")
        return 0

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['product_id', 'name', 'category', 'quantity', 'price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for p in products:
                writer.writerow({
                    'product_id': p['product_id'],
                    'name': p['name'],
                    'category': p['category'],
                    'quantity': p['quantity'],
                    'price': p['price']
                })

        print(f"✓ Saved {len(products)} products to {filename}")
        return len(products)

    except PermissionError:
        print(f" Permission denied: cannot write to {filename}")
        return 0
    except Exception as e:
        print(f"✗ Failed to save: {e}")
        return 0