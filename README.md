# 📦 Inventory Management System

> Inventory Management System is a command-line application that helps businesses track products, manage stock levels, and perform fast inventory queries. The system is built around an AVL Tree (self-balancing binary search tree) implemented from scratch, ensuring all operations run in O(log n) time.
The program loads product data from a CSV file and allows users to add, delete, search by ID, query ID ranges, list all products in sorted order, check low stock items, and view inventory statistics. After each operation, the tree automatically rebalances itself using rotations (left, right, left-right, right-left) to maintain logarithmic height.

---

## 👥 Team Members

| Member | Role |
|--------|------|
| **Vivien Hasratyan** | AVL Tree (`avl_tree.py`, `test_avl.py`) |
| **Areli Baghdadian** | Queries (`queries.py`, `test_queries.py`) |
| **Emilya Karapetyan** | UI & File Management (`ui.py`, `file_manager.py`, `main.py`) |

---

## ✨ Features

| Feature | Status |
|---------|--------|
| AVL Tree (insert/delete/search) | ✅ |
| Range query (ID between X and Y) | ✅ |
| In-order traversal (sorted listing) | ✅ |
| Load/Save from CSV | ✅ |
| Low stock alert | ✅ |
| Statistics dashboard | ✅ |

---

## 🌲 Why AVL Tree?

| Structure | Search | Insert | Delete | Sorted |
|-----------|--------|--------|--------|--------|
| Sorted Array | O(log n) | O(n) | O(n) | ✅ |
| Hash Table | O(1) | O(1) | O(1) | ❌ |
| Regular BST | O(n) | O(n) | O(n) | ✅ |
| **AVL Tree** | **O(log n)** | **O(log n)** | **O(log n)** | ✅ |

---

## 🎮 Menu Options

1. Add product
2. Delete product
3. Search by ID
4. Range query
5. List all products
6. Low stock alert
7. Statistics
8. Search by Category
9. Search by Name
10. Save & Exit

---
