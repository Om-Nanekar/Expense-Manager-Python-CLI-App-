# Expense Manager (Python CLI App)

This is a simple command-line based Expense Manager project made using Python. It allows you to record, view, and calculate your daily expenses. All data is saved in a JSON file.

---

# Features:

* Add new expenses with:
  Amount
  Category
  Note
  Date and Time (auto recorded)

* View all past expenses in table format

* Show total of all expenses

* Saves all data in "expenses\_history.json" permanently

---

# How to Run:

1. Clone or download this project folder

2. Install tabulate library
   Run this command in terminal:
   pip install tabulate

3. Run the program
   python main.py

---

# Project Files:

main.py – The main script to run the Expense Manager
expenses_history.json – Stores saved expenses
README.md – Info about the project

---

# Example Output:

-------- Welcome to Expense Maneger --------
1 for Add expense
2 for Show all expenses
3 for Show total expenses
4 for Exit

If you choose 2:

+--------+----------+---------+----------+--------+
| Amount | Category | Note    | Date     | Time   |
+--------+----------+---------+----------+--------+
| 120    | Food     | Lunch   | 25-06-25 | 14:22  |
| 200    | Travel   | Bus fare| 25-06-25 | 16:10  |
+--------+----------+---------+----------+--------+

---

# Built using:

Python 3
tabulate module
JSON for data saving

---

# Made by: [ Om-Nanekar ]

---
