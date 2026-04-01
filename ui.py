# ============================================
# FILE: ui.py
# AUTHOR: Emilya Karapetyan
# PURPOSE: Command-line user interface for inventory system
# ============================================

# ============================================
# Input Validation Helpers
# ============================================

def get_int_input(prompt, min_val=None, max_val=None):
    """Get integer input with optional bounds."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("  Input cannot be empty.")
                continue
            value = int(user_input)
            if min_val is not None and value < min_val:
                print(f"  Value must be >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Value must be <= {max_val}.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def get_float_input(prompt, min_val=None, max_val=None):
    """Get float input with optional bounds."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("  Input cannot be empty.")
                continue
            value = float(user_input)
            if min_val is not None and value < min_val:
                print(f"  Value must be >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Value must be <= {max_val}.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_string_input(prompt, min_length=1, max_length=None):
    """Get non-empty string input with optional max length."""
    while True:
        user_input = input(prompt).strip()
        if not user_input and min_length > 0:
            print("  Input cannot be empty.")
            continue
        if max_length and len(user_input) > max_length:
            print(f"  Input too long (max {max_length} characters).")
            continue
        return user_input


def get_confirmation(prompt):
    """Ask yes/no question, return True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("  Please answer 'y' or 'n'.")


# ============================================
# Menu Display
# ============================================

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("        INVENTORY MANAGEMENT SYSTEM")
    print("=" * 60)
    print("  1. Add product")
    print("  2. Delete product")
    print("  3. Search by ID")
    print("  4. Range query (IDs between X and Y)")
    print("  5. List all products")
    print("  6. Low stock alert")
    print("  7. Statistics")
    print("  8. Save & Exit")
    print("=" * 60)


def get_user_choice():
    """Get and validate menu choice."""
    while True:
        choice = input("\nEnter choice (1-8): ").strip()
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
            return int(choice)
        print("  Invalid choice. Please enter 1-8.")


# ============================================
# Interactive Action Functions
# ============================================

def add_product_interactive(tree):
    """Add a new product."""
    print("\n--- ADD NEW PRODUCT ---")

    product_id = get_int_input("Product ID: ", min_val=1)

    # Check if ID already exists
    if tree.search(product_id):
        print(f"✗ Product ID {product_id} already exists!")
        return

    name = get_string_input("Product name: ", min_length=1, max_length=100)
    category = get_string_input("Category: ", min_length=1, max_length=50)
    quantity = get_int_input("Quantity: ", min_val=0)
    price = get_float_input("Price: $", min_val=0)

    try:
        tree.insert(product_id, name, category, quantity, price)
        print(f"✓ Product '{name}' (ID: {product_id}) added successfully!")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def delete_product_interactive(tree):
    """Delete a product by ID."""
    print("\n--- DELETE PRODUCT ---")

    product_id = get_int_input("Product ID to delete: ", min_val=1)

    product = tree.search(product_id)
    if not product:
        print(f"✗ Product ID {product_id} not found!")
        return

    print("\nProduct found:")
    print(f"  Name: {product.name}")
    print(f"  Category: {product.category}")
    print(f"  Quantity: {product.quantity}")
    print(f"  Price: ${product.price:.2f}")

    if not get_confirmation("\nConfirm delete? (y/n): "):
        print("Deletion cancelled.")
        return

    try:
        tree.delete(product_id)
        print(f"✓ Product ID {product_id} deleted successfully!")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def search_product_interactive(tree):
    """Search and display product by ID."""
    print("\n--- SEARCH PRODUCT ---")

    product_id = get_int_input("Product ID: ", min_val=1)

    product = tree.search(product_id)
    if not product:
        print(f"✗ Product ID {product_id} not found!")
        return

    print("\n" + "=" * 50)
    print("PRODUCT DETAILS")
    print("=" * 50)
    print(f"ID:         {product.product_id}")
    print(f"Name:       {product.name}")
    print(f"Category:   {product.category}")
    print(f"Quantity:   {product.quantity}")
    print(f"Price:      ${product.price:.2f}")
    print("=" * 50)


def list_all_products_interactive(tree):
    """List all products in sorted order."""
    print("\n--- FULL INVENTORY (Sorted by ID) ---")

    try:
        products = tree.inorder_traversal()
    except AttributeError:
        products = []

        def collect(node):
            if node:
                collect(node.left)
                products.append({
                    'id': node.product_id,
                    'name': node.name,
                    'category': node.category,
                    'quantity': node.quantity,
                    'price': node.price
                })
                collect(node.right)

        collect(tree.root)

    if not products:
        print("Inventory is empty.")
        return

    # Print table
    print("\n" + "-" * 80)
    print(f"{'ID':<8} {'Name':<25} {'Category':<15} {'Qty':<8} {'Price':<10}")
    print("-" * 80)

    for p in products:
        print(f"{p['id']:<8} {p['name']:<25} {p['category']:<15} "
              f"{p['quantity']:<8} ${p['price']:<10.2f}")

    print("-" * 80)
    print(f"Total products: {len(products)}")


def range_query_interactive(tree):
    """Query products with IDs between low and high."""
    print("\n--- RANGE QUERY ---")

    low = get_int_input("Lower bound ID: ", min_val=1)
    high = get_int_input("Upper bound ID: ", min_val=1)

    if low > high:
        print("✗ Lower bound must be less than or equal to upper bound.")
        return

    try:
        results = tree.range_query(low, high)
    except AttributeError:
        all_products = []

        def collect(node):
            if node:
                collect(node.left)
                all_products.append({
                    'id': node.product_id,
                    'name': node.name,
                    'category': node.category,
                    'quantity': node.quantity,
                    'price': node.price
                })
                collect(node.right)

        collect(tree.root)
        results = [p for p in all_products if low <= p['id'] <= high]

    if not results:
        print(f"No products found with IDs between {low} and {high}")
        return

    print(f"\nFound {len(results)} products:")
    print("-" * 80)
    print(f"{'ID':<8} {'Name':<25} {'Category':<15} {'Qty':<8} {'Price':<10}")
    print("-" * 80)

    for p in results:
        print(f"{p['id']:<8} {p['name']:<25} {p['category']:<15} "
              f"{p['quantity']:<8} ${p['price']:<10.2f}")

    print("-" * 80)


def low_stock_interactive(tree):
    """Show products with quantity below threshold."""
    print("\n--- LOW STOCK ALERT ---")

    threshold = get_int_input("Quantity threshold: ", min_val=0)

    try:
        results = tree.low_stock(threshold)
    except AttributeError:
        results = []

        def collect(node):
            if node:
                collect(node.left)
                if node.quantity < threshold:
                    results.append({
                        'id': node.product_id,
                        'name': node.name,
                        'quantity': node.quantity
                    })
                collect(node.right)

        collect(tree.root)

    if not results:
        print(f"No products with quantity below {threshold}")
        return

    print(f"\nProducts with quantity below {threshold}:")
    print("-" * 60)
    print(f"{'ID':<8} {'Name':<25} {'Quantity':<10} {'Status':<15}")
    print("-" * 60)

    for p in results:
        status = "⚠ CRITICAL" if p['quantity'] < 5 else "⚠ Low"
        print(f"{p['id']:<8} {p['name']:<25} {p['quantity']:<10} {status:<15}")

    print("-" * 60)


def statistics_interactive(tree):
    """Display tree statistics."""
    print("\n--- INVENTORY STATISTICS ---")

    node_count = tree.get_node_count()
    height = tree.get_height(tree.root)
    balance = tree.get_balance(tree.root)

    print(f"Total products: {node_count}")
    print(f"Tree height: {height}")
    print(f"Root balance factor: {balance:+d}")

    if abs(balance) <= 1:
        print("Tree status: ✓ Balanced")
    else:
        print("Tree status: ✗ Unbalanced (should not happen with AVL)")


def save_and_exit_interactive(tree, filename):
    """Save inventory and return flag to exit."""
    from file_manager import save_inventory
    print("\n--- SAVING AND EXITING ---")
    save_inventory(filename, tree)
    print("Goodbye!")
    return True