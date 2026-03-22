# ============================================
# FILE: test_avl.py
# AUTHOR: Vivien Hasratyan
# PURPOSE: Unit tests for AVL Tree implementation
# ============================================

from avl_tree import AVLTree

def check_avl_balance(tree, node):
    """Recursively check AVL balance property"""
    if node is None:
        return True
    balance = tree.get_balance(node)
    if abs(balance) > 1:
        print(f"  ✗ Unbalanced at node {node.product_id}: balance={balance}")
        return False
    left_ok = check_avl_balance(tree, node.left)
    right_ok = check_avl_balance(tree, node.right)
    return left_ok and right_ok


if __name__ == "__main__":
    print("=" * 50)
    print("TESTING AVL TREE IMPLEMENTATION")
    print("=" * 50)

    # Test 1: Create tree
    print("\nTest 1: Create AVL Tree")
    tree = AVLTree()
    print("✓ AVLTree created successfully")

    # Test 2: Insert product
    print("\nTest 2: Insert Product")
    tree.insert(100, "Test Product", "Test", 10, 9.99)
    print("✓ Inserted product with ID 100")
    print(f"  Node count: {tree.get_node_count()}")

    # Test 3: Search for product
    print("\nTest 3: Search Product")
    result = tree.search(100)
    if result:
        print(f"✓ Found product: {result.name}")
        print(f"  ID: {result.product_id}")
        print(f"  Category: {result.category}")
        print(f"  Quantity: {result.quantity}")
        print(f"  Price: ${result.price}")
    else:
        print("✗ Search failed - product not found")

    # Test 4: Duplicate handling
    print("\nTest 4: Duplicate ID Handling")
    try:
        tree.insert(100, "Duplicate", "Test", 5, 5.99)
        print("✗ Duplicate should have been rejected")
    except ValueError as e:
        print(f"✓ Duplicate correctly rejected: {e}")

    # Test 5: Search for non-existent product
    print("\nTest 5: Search Non-Existent Product")
    result = tree.search(999)
    if result is None:
        print("✓ Non-existent product returns None")
    else:
        print("✗ Search should return None for missing product")

    # Test 6: Insert multiple products
    print("\nTest 6: Insert Multiple Products")
    test_ids = [50, 150, 75, 125, 25]
    for pid in test_ids:
        tree.insert(pid, f"Product{pid}", "Test", 10, 9.99)
        print(f"  ✓ Inserted ID: {pid}")

    print(f"\n  Final node count: {tree.get_node_count()}")
    print(f"  Expected: {1 + len(test_ids)}")

    # Test 7: Search all inserted products
    print("\nTest 7: Search All Products")
    all_ids = [100] + test_ids
    all_found = True
    for pid in all_ids:
        result = tree.search(pid)
        if result:
            print(f"  ✓ Found ID: {pid}")
        else:
            print(f"  ✗ Missing ID: {pid}")
            all_found = False

    if all_found:
        print("✓ All products found successfully")

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETE")
    print("=" * 50)

    # ============================================
    # ADDITIONAL AVL BALANCE TESTS
    # ============================================

    print("\n" + "=" * 50)
    print("TESTING AVL BALANCE PROPERTIES")
    print("=" * 50)

    # Test 8: Test rotations with sorted input (worst case)
    print("\nTest 8: Inserting Sorted IDs (Should Trigger Rotations)")
    tree2 = AVLTree()
    sorted_ids = [10, 20, 30, 40, 50, 60, 70]

    for pid in sorted_ids:
        tree2.insert(pid, f"Product{pid}", "Test", 10, 9.99)
        print(f"  Inserted {pid}: root={tree2.root.product_id}, height={tree2.get_height(tree2.root)}")

    if check_avl_balance(tree2, tree2.root):
        print("✓ AVL property maintained (|balance| ≤ 1 for all nodes)")
    else:
        print("✗ AVL property violated")

    # Expected height for 7 nodes in AVL: log₂(7) ≈ 3
    expected_max_height = 4
    actual_height = tree2.get_height(tree2.root)
    print(f"  Tree height: {actual_height} (expected ≤ {expected_max_height})")
    if actual_height <= expected_max_height:
        print("✓ Tree height is O(log n)")
    else:
        print("✗ Tree is too tall - balancing may not work")

    # Test 9: Delete functionality
    print("\nTest 9: Delete Functionality")
    tree3 = AVLTree()
    for pid in [50, 30, 70, 20, 40, 60, 80]:
        tree3.insert(pid, f"Product{pid}", "Test", 10, 9.99)

    print(f"Initial node count: {tree3.get_node_count()}")

    # Delete leaf
    tree3.delete(20)
    print(f"  After deleting leaf (20): count={tree3.get_node_count()}")

    # Delete node with one child
    tree3.delete(30)
    print(f"  After deleting node with one child (30): count={tree3.get_node_count()}")

    # Delete node with two children (root)
    tree3.delete(50)
    print(f"  After deleting root with two children (50): count={tree3.get_node_count()}")

    # Verify deleted nodes are gone
    if tree3.search(20) is None and tree3.search(30) is None and tree3.search(50) is None:
        print("✓ All deleted nodes properly removed")
    else:
        print("✗ Some deleted nodes still exist")

    # Check balance after deletions
    if check_avl_balance(tree3, tree3.root):
        print("✓ Tree remains balanced after deletions")
    else:
        print("✗ Tree unbalanced after deletions")

    # Test 10: Test invalid delete
    print("\nTest 10: Delete Non-Existent Product")
    try:
        tree3.delete(999)
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly handled: {e}")

    print("\n" + "=" * 50)
    print("ALL AVL TESTS COMPLETE")
    print("=" * 50)