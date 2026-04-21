# 📦 Inventory Management System

> An AVL Tree-powered inventory engine with O(log n) operations

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
4. Range query (IDs between X and Y)
5. List all products
6. Low stock alert
7. Statistics
8. Save & Exit

---

## 📁 File Structure

┌────────────────────────────────────────────────────────────┐
│  INVENTORY MANAGEMENT SYSTEM                               │
├────────────────────────────────────────────────────────────┤
│  📄 main.py           Entry point                          │
│  🌲 avl_tree.py       AVL Tree                    │
│  🔍 queries.py        Queries                       │
│  🖥️ ui.py             User interface               │
│  💾 file_manager.py   CSV operations               │
│  🔧 create_inventory.py  Sample data generator             │
│  ✅ test_avl.py       AVL tests                            │
│  ✅ test_queries.py   Query tests                          │
│  📁 data/                                                 │
│      └── inventory.csv  Product database                   │
└────────────────────────────────────────────────────────────┘
