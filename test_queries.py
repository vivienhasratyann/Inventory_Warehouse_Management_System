# ============================================
# FILE: test_queries.py
# AUTHOR: Areli Baghdadian
# PURPOSE: Unit tests for inventory queries
# ============================================

import csv
from avl_tree import AVLTree
from queries import InventoryQueries

import os
print("Current working directory:", os.getcwd())
print("File exists?", os.path.exists("data/inventory.csv"))


def test_inorder_traversal():
    """Test that inorder traversal returns sorted products"""
    print("\n--- Test 1: In-order Traversal ---")
    tree = AVLTree()
    queries = InventoryQueries(tree)

    # Add test data
    tree.insert(100, "Wireless Mouse", "Electronics", 150, 29.99)
    tree.insert(50, "USB Cable", "Accessories", 500, 12.99)
    tree.insert(150, "Monitor", "Electronics", 42, 199.99)
    tree.insert(75, "Keyboard", "Electronics", 75, 89.99)
    tree.insert(25, "Mouse Pad", "Accessories", 200, 9.99)

    products = queries.inorder_traversal()
    ids = [p['id'] for p in products]

    if ids == [25, 50, 75, 100, 150]:
        print("✓ Correct sorted order")
        return True
    else:
        print(f"✗ Expected [25,50,75,100,150], got {ids}")
        return False


def test_range_query():
    """Test range query functionality"""
    print("\n--- Test 2: Range Query ---")
    tree = AVLTree()
    queries = InventoryQueries(tree)

    # Add numbers 10,20,30,...,100
    for i in range(10, 101, 10):
        tree.insert(i, f"Product{i}", "Test", 10, 9.99)

    results = queries.range_query(35, 65)
    ids = [p['id'] for p in results]

    expected = [40, 50, 60]
    if ids == expected:
        print(f"✓ Range query correct: {ids}")
        return True
    else:
        print(f"✗ Expected {expected}, got {ids}")
        return False


def test_low_stock():
    """Test low stock alert"""
    print("\n--- Test 3: Low Stock Alert ---")
    tree = AVLTree()
    queries = InventoryQueries(tree)

    tree.insert(1, "High", "Test", 100, 10)
    tree.insert(2, "Medium", "Test", 50, 10)
    tree.insert(3, "Low", "Test", 20, 10)
    tree.insert(4, "Critical", "Test", 5, 10)

    low = queries.low_stock(30)
    ids = [p['id'] for p in low]

    if ids == [3, 4]:  # IDs with quantity < 30
        print(f"✓ Low stock alert correct: {ids}")
        return True
    else:
        print(f"✗ Expected [3,4], got {ids}")
        return False


def test_statistics():
    """Test statistics calculation"""
    print("\n--- Test 4: Statistics ---")
    tree = AVLTree()
    queries = InventoryQueries(tree)

    tree.insert(10, "A", "Cat1", 10, 5.00)
    tree.insert(20, "B", "Cat2", 5, 10.00)
    tree.insert(30, "C", "Cat1", 2, 20.00)

    stats = queries.get_statistics()

    if (stats['total_products'] == 3 and
        stats['total_value'] == (10*5 + 5*10 + 2*20) and
        sorted(stats['categories']) == ['Cat1', 'Cat2']):
        print("✓ Statistics correct")
        return True
    else:
        print("✗ Statistics incorrect")
        return False


def test_with_real_csv():
    """Test with the actual inventory.csv file"""
    print("\n--- Test 5: Real CSV Data ---")
    try:
        tree = AVLTree()
        with open('data/inventory.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tree.insert(
                    int(row['product_id']),
                    row['name'],
                    row['category'],
                    int(row['quantity']),
                    float(row['price'])
                )

        queries = InventoryQueries(tree)
        products = queries.inorder_traversal()

        print(f"✓ Loaded {len(products)} products from CSV")
        print(f"  First ID: {products[0]['id']}, Last ID: {products[-1]['id']}")

        # Test range query
        results = queries.range_query(1010, 1015)
        print(f"  Range 1010-1015: {len(results)} products")

        # Test low stock (threshold 30)
        low = queries.low_stock(30)
        print(f"  Low stock (<30): {len(low)} products")

        return True
    except FileNotFoundError:
        print("✗ data/inventory.csv not found. Create it first.")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING INVENTORY QUERIES")
    print("=" * 60)

    # Run all tests
    test_inorder_traversal()
    test_range_query()
    test_low_stock()
    test_statistics()
    test_with_real_csv()

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETE")
    print("=" * 60)