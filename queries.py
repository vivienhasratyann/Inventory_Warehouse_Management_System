# ============================================
# FILE: queries.py
# AUTHOR: Areli Baghdadian
# PURPOSE: Query operations for inventory management system
# ============================================

from avl_tree import AVLTree


class InventoryQueries:
    """Wrapper class for inventory query operations"""
    
    def __init__(self, tree):
        """Initialize with an AVL tree"""
        self.tree = tree
    
    
    def inorder_traversal(self):
        """Return all products in sorted order by ID"""
        result = []
        self._inorder_recursive(self.tree.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for recursive in-order traversal"""
        if node is None:
            return
        
        # Traverse left subtree
        self._inorder_recursive(node.left, result)
        
        # Add current node
        result.append({
            'id': node.product_id,
            'name': node.name,
            'category': node.category,
            'quantity': node.quantity,
            'price': node.price
        })
        
        # Traverse right subtree
        self._inorder_recursive(node.right, result)
    
    
    def range_query(self, low, high):
        """Return all products with IDs between low and high"""
        result = []
        self._range_recursive(self.tree.root, low, high, result)
        return result

    def _range_recursive(self, node, low, high, result):
        """Helper method for recursive range query"""
        if node is None:
            return
        
        # If current node is greater than low, check left subtree
        if node.product_id > low:
            self._range_recursive(node.left, low, high, result)
        
        # If current node is within range, add it
        if low <= node.product_id <= high:
            result.append({
                'id': node.product_id,
                'name': node.name,
                'category': node.category,
                'quantity': node.quantity,
                'price': node.price
            })
        
        # If current node is less than high, check right subtree
        if node.product_id < high:
            self._range_recursive(node.right, low, high, result)
    
    
    def low_stock(self, threshold):
        """Return all products with quantity below threshold"""
        result = []
        self._low_stock_recursive(self.tree.root, threshold, result)
        return result

    def _low_stock_recursive(self, node, threshold, result):
        """Helper method for low stock search"""
        if node is None:
            return
        
        # Check left subtree
        self._low_stock_recursive(node.left, threshold, result)
        
        # Check current node
        if node.quantity < threshold:
            result.append({
                'id': node.product_id,
                'name': node.name,
                'quantity': node.quantity
            })
        
        # Check right subtree
        self._low_stock_recursive(node.right, threshold, result)
        
        
    def get_statistics(self):
        """Return inventory statistics"""
        stats = {
            'total_products': self.tree.get_node_count(),
            'total_value': 0,
            'categories': set(),
            'tree_height': self.tree.get_height(self.tree.root)
        }
        
        # Collect statistics during traversal
        self._stats_recursive(self.tree.root, stats)
        
        # Convert set to list for JSON serialization
        stats['categories'] = list(stats['categories'])
        
        return stats

    def _stats_recursive(self, node, stats):
        """Helper method to collect statistics"""
        if node is None:
            return
        
        self._stats_recursive(node.left, stats)
        
        # Add to total value
        stats['total_value'] += node.quantity * node.price
        
        # Add category
        stats['categories'].add(node.category)
        
        self._stats_recursive(node.right, stats)
    
    
    def search_by_category(self, category):
        """Return all products in a specific category"""
        result = []
        self._category_recursive(self.tree.root, category, result)
        return result

    def _category_recursive(self, node, category, result):
        if node is None:
            return
        
        self._category_recursive(node.left, category, result)
        
        if node.category.lower() == category.lower():
            result.append({
                'id': node.product_id,
                'name': node.name,
                'category': node.category,
                'quantity': node.quantity,
                'price': node.price
            })
        
        self._category_recursive(node.right, category, result)
    
    def search_by_name(self, keyword):
        """Return all products with name containing keyword"""
        result = []
        self._name_recursive(self.tree.root, keyword.lower(), result)
        return result

    def _name_recursive(self, node, keyword, result):
        if node is None:
            return
        
        self._name_recursive(node.left, keyword, result)
        
        if keyword in node.name.lower():
            result.append({
                'id': node.product_id,
                'name': node.name,
                'category': node.category,
                'quantity': node.quantity,
                'price': node.price
            })
        
        self._name_recursive(node.right, keyword, result)
        