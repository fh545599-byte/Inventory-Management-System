# Inventory Management System

A Python-based **Inventory Management System** designed to manage products, stock, sales, expenses, and business reports through a simple console-based interface.

## 📌 Project Overview

The Inventory Management System helps small businesses manage their daily inventory operations efficiently.

The application allows users to:

* Add and manage products
* Search products
* Update stock
* Sell products
* Track sales
* Record expenses
* Monitor low-stock products
* Calculate profit and profit margin
* Generate business reports
* Store data using JSON files

## ✨ Features

### 📦 Product Management

* Add new products
* View all products
* Search products by:

  * Product ID
  * Product name
  * Category
* Update product stock
* Delete products
* Display product information

### 🛒 Sales Management

* Sell products
* Check available stock before selling
* Automatically update inventory after a sale
* Store sales history
* Record date and time of sales

### 💰 Expense Management

* Add business expenses
* View expense records
* Track total expenses

### 📊 Business Reports

The system generates useful business information including:

* Total sales
* Total expenses
* Total profit
* Net profit
* Profit margin
* Inventory value
* Best-selling product

### ⚠️ Low Stock Alert

The system identifies products with low inventory levels and displays them for restocking.

### 💾 Data Persistence

Product, sales, and expense data are stored in **JSON files**, allowing information to remain available after the program is closed.

### 🛡️ Input Validation

The application uses validation and exception handling to reduce invalid user input and runtime errors.

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Exception Handling
* Functions
* Lists
* Dictionaries
* Classes & Objects

## 📂 Project Structure

```text
Inventory-Management-System/
│
├── main.py
├── .gitignore
└── README.md
```

> JSON data files are generated locally by the application and are excluded from Git using `.gitignore`.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/fh545599-byte/Inventory-Management-System.git
```

### 2. Open the project folder

```bash
cd Inventory-Management-System
```

### 3. Run the application

```bash
python main.py
```

## 📋 Main Menu

The application provides the following options:

```text
1. Add Product
2. View Products
3. Search Product
4. Update Stock
5. Delete Product
6. Sell Product
7. Add Expense
8. View Expenses
9. View Sales
10. Low Stock Alert
11. Reports
12. Exit
```

## 🎯 Learning Objectives

This project was developed to practice and demonstrate:

* Python programming fundamentals
* Object-Oriented Programming
* Classes and objects
* Functions and modular programming
* Lists and dictionaries
* File handling
* JSON data storage
* Exception handling
* CRUD operations
* Basic business logic
* Git and GitHub

## 🔮 Future Improvements

Possible future improvements include:

* SQLite/MySQL database integration
* Graphical User Interface (GUI)
* Web-based interface
* User authentication
* Admin and employee roles
* Barcode scanning
* PDF report generation
* Advanced sales analytics
* REST API integration

## 👨‍💻 Author

**Farhan Habib**

BS Computer Science Student
Interested in **Artificial Intelligence, Machine Learning, and Software Development**.

## 📄 License

This project is created for **educational and internship practice purposes**.
