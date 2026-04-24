# ============================================
# FILE: main.py
# AUTHOR: Emilya Karapetyan
# PURPOSE: Main entry point for inventory system
# ============================================

from avl_tree import AVLTree
from file_manager import load_inventory
from ui import (
    display_menu, get_user_choice,
    add_product_interactive, delete_product_interactive,
    search_product_interactive, list_all_products_interactive,
    range_query_interactive, low_stock_interactive,
    statistics_interactive, search_by_category_interactive, search_by_name_interactive, save_and_exit_interactive
)

INVENTORY_FILE = "data/inventory.csv"


def main():
    """Main program loop."""
    print("\n" + "=" * 60)
    print("  WELCOME TO INVENTORY MANAGEMENT SYSTEM")
    print("  Powered by AVL Tree")
    print("=" * 60)

    # Create AVL tree instance
    tree = AVLTree()

    # Load existing inventory
    load_inventory(INVENTORY_FILE, tree)

    # Main menu loop
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_product_interactive(tree)
        elif choice == 2:
            delete_product_interactive(tree)
        elif choice == 3:
            search_product_interactive(tree)
        elif choice == 4:
            range_query_interactive(tree)
        elif choice == 5:
            list_all_products_interactive(tree)
        elif choice == 6:
            low_stock_interactive(tree)
        elif choice == 7:
            statistics_interactive(tree)
        elif choice == 8:
            search_by_category_interactive(tree)
        elif choice == 9:
            search_by_name_interactive(tree)
        elif choice == 10:
            if save_and_exit_interactive(tree, INVENTORY_FILE):
                break


if __name__ == "__main__":
    main()