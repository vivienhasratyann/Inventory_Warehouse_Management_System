# ============================================
# FILE: avl_tree.py
# AUTHOR: Vivien Hasratyan
# PURPOSE: AVL Tree implementation for inventory management
# ============================================

class AVLNode:
    """Node in AVL tree - stores product data and tree metadata"""

    def __init__(self, product_id, name, category, quantity, price):
        # Product data
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

        # Tree pointers
        self.left = None
        self.right = None

        # AVL metadata
        self.height = 1


class AVLTree:
    """AVL Tree implementation with self-balancing properties"""

    def __init__(self):
        self.root = None
        self.node_count = 0

    # ============================================
    # Helper Methods
    # ============================================

    def get_height(self, node):
        """Return height of node (0 if node is None)"""
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        """Update height of node based on children heights"""
        if node is None:
            return
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def get_balance(self, node):
        """Calculate balance factor (left height - right height)"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ============================================
    # ROTATION METHODS (ADD HERE)
    # ============================================

    def _right_rotate(self, y):
        """
        Right rotation for Left-Left case

        Before:        y
                     /   \
                    x     T3
                   / \
                  T1  T2

        After:         x
                     /   \
                    T1    y
                         / \
                        T2  T3
        """
        x = y.left  # x becomes new root
        T2 = x.right  # Save T2 before reassigning

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights (y first, then x)
        self.update_height(y)
        self.update_height(x)

        return x  # New root of this subtree

    def _left_rotate(self, x):
        """
        Left rotation for Right-Right case

        Before:    x
                 /   \
                T1    y
                     / \
                    T2  T3

        After:         y
                     /   \
                    x     T3
                   / \
                  T1  T2
        """
        y = x.right  # y becomes new root
        T2 = y.left  # Save T2 before reassigning

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights (x first, then y)
        self.update_height(x)
        self.update_height(y)

        return y  # New root of this subtree

    def _left_right_rotate(self, node):
        """
        Left-Right rotation:
        1. Left rotate left child
        2. Right rotate node
        """
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_left_rotate(self, node):
        """
        Right-Left rotation:
        1. Right rotate right child
        2. Left rotate node
        """
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    # ============================================
    # Insert Methods
    # ============================================

    def insert(self, product_id, name, category, quantity, price):
        """Public method to insert a product"""
        try:
            self.root = self._insert_recursive(self.root, product_id, name,
                                               category, quantity, price)
            self.node_count += 1
        except ValueError as e:
            raise e

    def _insert_recursive(self, node, product_id, name, category, quantity, price):
        """Private recursive insert method with AVL balancing"""

        # Step 1: Standard BST insertion
        if node is None:
            return AVLNode(product_id, name, category, quantity, price)

        if product_id < node.product_id:
            node.left = self._insert_recursive(node.left, product_id, name,
                                               category, quantity, price)
        elif product_id > node.product_id:
            node.right = self._insert_recursive(node.right, product_id, name,
                                                category, quantity, price)
        else:
            raise ValueError(f"Product ID {product_id} already exists")

        # Step 2: Update height of current node
        self.update_height(node)

        # Step 3: Get balance factor
        balance = self.get_balance(node)

        # Step 4: Balance the tree (4 cases)

        # Case 1: Left-Left
        if balance > 1 and product_id < node.left.product_id:
            return self._right_rotate(node)

        # Case 2: Right-Right
        if balance < -1 and product_id > node.right.product_id:
            return self._left_rotate(node)

        # Case 3: Left-Right
        if balance > 1 and product_id > node.left.product_id:
            return self._left_right_rotate(node)

        # Case 4: Right-Left
        if balance < -1 and product_id < node.right.product_id:
            return self._right_left_rotate(node)

        return node

    # ============================================
    # Search Methods
    # ============================================

    def search(self, product_id):
        """Public method to search for a product by ID"""
        return self._search_recursive(self.root, product_id)

    def _search_recursive(self, node, product_id):
        """Private recursive search method"""
        # Base case: not found
        if node is None:
            return None

        # Found
        if product_id == node.product_id:
            return node

        # Search left or right
        if product_id < node.product_id:
            return self._search_recursive(node.left, product_id)
        else:
            return self._search_recursive(node.right, product_id)

    # ============================================
    # Delete Methods
    # ============================================

    def delete(self, product_id):
        """Public method to delete a product by ID"""
        try:
            self.root = self._delete_recursive(self.root, product_id)
            self.node_count -= 1
        except ValueError as e:
            raise e

    def _delete_recursive(self, node, product_id):
        """Private recursive delete method with AVL balancing"""

        # Step 1: Find the node to delete
        if node is None:
            raise ValueError(f"Product ID {product_id} not found")

        if product_id < node.product_id:
            node.left = self._delete_recursive(node.left, product_id)
        elif product_id > node.product_id:
            node.right = self._delete_recursive(node.right, product_id)
        else:
            # Found the node to delete

            # Case 1: No children or one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self._find_min(node.right)
            # Copy successor's data to current node
            node.product_id = successor.product_id
            node.name = successor.name
            node.category = successor.category
            node.quantity = successor.quantity
            node.price = successor.price
            # Delete the successor
            node.right = self._delete_recursive(node.right, successor.product_id)

        # If tree becomes empty after deletion
        if node is None:
            return None

        # Step 2: Update height
        self.update_height(node)

        # Step 3: Get balance factor
        balance = self.get_balance(node)

        # Step 4: Rebalance the tree (4 cases)

        # Case 1: Left-Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Case 2: Left-Right
        if balance > 1 and self.get_balance(node.left) < 0:
            return self._left_right_rotate(node)

        # Case 3: Right-Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Case 4: Right-Left
        if balance < -1 and self.get_balance(node.right) > 0:
            return self._right_left_rotate(node)

        return node

    def _find_min(self, node):
        """Find the node with minimum product_id in a subtree"""
        current = node
        while current.left:
            current = current.left
        return current


    # ============================================
    # Additional Methods for Testing
    # ============================================

    def get_node_count(self):
        """Return total number of nodes"""
        return self.node_count


