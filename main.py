import json
from datetime import datetime

class Product:
    def __init__(self, product_id, product_name,cost_price, price, quantity, category):
        self.product_id = product_id
        self.product_name = product_name
        self.cost_price= cost_price
        self.price = price
        self.quantity = quantity
        self.category = category

    def display(self):
        print("\t\t----------------------")
        print("ID = ", self.product_id)
        print("Name = ", self.product_name)
        print("Cost Price = ",f"{self.cost_price:.2f}")
        print("Price = ", f"{self.price:.2f}")
        print("Quantity = ", self.quantity)
        print("Category = ", self.category)
        print("\t\t----------------------\n")

    def update_stock(self,amount):
        self.quantity= self.quantity+ amount

    def calculate_profit(self, quantity):
        profit = (self.price - self.cost_price) * quantity
        return profit

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        else:
            return False

    def is_low_stock(self):
        if self.quantity <= 5: 
            return True 
        else: 
            return False


p1 = Product(13, "Chocolate",40.00, 55.00, 1, "milk")
p2 = Product(14, "Wafer",35.00, 55.00, 1, "biscuit")
p3 = Product(25, "Zeera",20.00, 35.00, 1, "biscuit")

products = []
products.append(p1)
products.append(p2)
products.append(p3)

# ---------------- SAVE PRODUCTS ----------------
def save_products():
    
    product_data=[]
    for product in products:
        pro_dic = {
            "Product_ID": product.product_id,
            "Product_Name": product.product_name,
            "Cost_price": product.cost_price,
            "Product_Price": product.price,
            "Quantity": product.quantity,
            "Product_Category":product.category
        }
        product_data.append(pro_dic)

    with open("products.json", "w") as file:
        json.dump(product_data,file,indent=4)


# ---------------- LOAD PRODUCTS ----------------
def load_products():
    try:
        with open("products.json","r") as file:
            data= json.load(file)
        products.clear()
        for item in data:
            product = Product(
                item["Product_ID"],
                item["Product_Name"],
                item["Cost_price"],
                item["Product_Price"],
                item["Quantity"],
                item["Product_Category"]
            )

            products.append(product)
    except FileNotFoundError: 
        print("Products file not found. Starting with empty product list.")
    except json.JSONDecodeError:
        print("Products file contains invalid JSON data.")

# ---------------- VIEW PRODUCTS ----------------

def view_product():
    if not products:
        print("No products available!")
        return
    for product in products:
        product.display()


# ---------------- ADD PRODUCT ----------------

def add_product():

    try:
        p_id = int(input("Enter The Product ID: "))
        if p_id <= 0:
            print("Product ID must be greater than 0!")
            return

        for product in products:
            if product.product_id == p_id:
                print("Product ID already exists!")
                return
                
        p_name = input("Enter the Product Name: ").strip()
        if p_name == "":
            print("Product Name cannot be empty!")
            return

        cost_price = float(input("Enter the Product Cost Price: "))
        if cost_price <= 0:
            print("Cost Price must be greater than 0!")
            return

        p_price = float(input("Enter the Product selling Price: "))
        if p_price <= 0:
            print("Price must be greater than 0!")
            return

        if p_price < cost_price:
            print("Selling Price cannot be less than Cost Price!")
            return
        
        p_quantity = int(input("Enter the Product Quantity: "))
        if p_quantity < 0:
            print("Quantity must be 0 or greater!")
            return
        
        p_category = input("Enter the Product Category: ").strip()
        if p_category == "":
            print("Product Category cannot be empty!")
            return

        p4 = Product(p_id, p_name,cost_price, p_price, p_quantity, p_category)
        products.append(p4)

        save_products()

        print("Product Added Successfully")

    except ValueError:
        print("Invalid Input! Please enter numbers where required.")


# ---------------- SEARCH PRODUCT ----------------

def search_product():
    try:
        print(""" 
        ------------------------------ SEARCH PRODUCT ------------------------------ 
        1. Search by ID 
        2. Search by Name 
        3. Search by Category
         """)

        choice = input("Enter your choice: ")
        found = False

        # Search By ID
        if choice == "1": 
            user_id = int(input("Enter Product ID: ")) 
            for product in products: 
                if product.product_id == user_id: 
                    product.display() 
                    found = True 
                    break

        # Search by Name 
        elif choice == "2": 
            user_name = input("Enter Product Name: ").strip().lower()
            if user_name == "":
                print("Product Name cannot be empty!")
                return 
            for product in products: 
                if product.product_name.lower() == user_name: 
                    product.display() 
                    found = True

        # Search by Category 
        elif choice == "3": 
            user_category = input("Enter Product Category: ").strip().lower()
            if user_category == "":
                print("Product Category cannot be empty!")
                return 
            for product in products: 
                if product.category.lower() == user_category: 
                    product.display() 
                    found = True

        else: 
            print("Invalid Search Choice!") 
            return

        if not found:
            print("Product Not Found")
    except ValueError:
        print("Invalid Input! Please enter numbers where required.")

# ---------------- LOW STOCK ALERT ---------------- 
def low_stock_alert(): 
    found = False 
    print(""" 
    ------------------------------
            LOW STOCK ALERT 
    ------------------------------
    """) 
    for product in products: 
        if product.is_low_stock(): 
            print("Product Name =", product.product_name) 
            print("Quantity =", product.quantity) 
            print("Category =", product.category) 
            print("------------------------------") 
            found = True 
    if not found: 
        print("No low stock products!")

# ---------------- UPDATE STOCK ----------------

def update_stock():
    try:
        user_id = int(input("Enter Product ID to update the Product: \n"))

        found = False

        for product in products:
            if product.product_id == user_id:
                print("Current Quantity = ", product.quantity)

                new_stock = int(input("Enter the new stock quantity to add: "))

                     # Value Validation
                if new_stock < 0:
                    print("New Stock must be 0 or greater!")
                    return


                product.update_stock(new_stock)

                save_products()

                print("Stock Updated Successfully")

                found = True
                break

        if not found:
            print("Product Not Found")
    except ValueError:
        print("Invalid Input! Please enter numbers where required.")


# ---------------- DELETE PRODUCT ----------------

def delete_product():
    try:
        user_id = int(input("Enter Product ID to Delete the Product: \n"))

        found = False

        for product in products:
            if product.product_id == user_id:
                products.remove(product)
                save_products()

                print("Product Deleted Successfully")

                found = True
                break

        if not found:
            print("Product Not Found")
    except ValueError:
        print("Invalid Input! Please enter numbers where required.")

# ---------------- SALES ----------------

sales = []

def load_sales():
    try:
        with open("sales.json","r") as file:
            data= json.load(file)
        sales.clear()
        for item in data:
            sales.append(item)
    except FileNotFoundError: 
        print("Sales file not found. Starting with empty Sales list.")
    except json.JSONDecodeError:
        print("Sales file contains invalid JSON data.")

def save_sales():
    with open("sales.json", "w") as file:
        json.dump(sales, file, indent=4)

def sell_product():
    try:
        user_id = int(input("Enter Product ID to Sell the Product: \n"))

        found = False

        for product in products:
            if product.product_id == user_id:

                print("Name = ", product.product_name)
                print("Price = ", product.price)
                print("Quantity = ", product.quantity)

                selling_unit = int(input("How many units you want to sell? "))
                         # Value Validation
                if selling_unit <= 0:
                    print("Selling Unit must be greater than 0!")
                    return

                if product.sell(selling_unit):
                    save_products()

                    total = selling_unit * product.price

                    sale = {
                        "Product_ID": product.product_id,
                        "Product_Name": product.product_name,
                        "Quantity_Sold": selling_unit,
                        "Cost_price": product.cost_price,
                        "Product_Price": product.price,
                        "Total_sale": total,
                        "Date_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    sales.append(sale)
                    save_sales()

                    print("Sale Successfully")

                else:
                    print("Insufficient Stock")

                found = True
                break

        if not found:
            print("Product Not Found")
    except ValueError:
        print("Invalid Input! Please enter numbers where required.")


# ---------------- VIEW SALES ----------------

def view_sales():
    if not sales:
        print("No Sales available!")
        return
    for s in sales:
        print("\t\t----------------------")
        print("Product Name = ", s["Product_Name"])
        print("Quantity Sold = ", s["Quantity_Sold"])
        print("Cost Price = ", f"{s['Cost_price']:.2f}")
        print("Product Price = ", f"{s['Product_Price']:.2f}")
        print("Total Sale = ", f"{s['Total_sale']:.2f}")
        print("Date & Time = ", s.get("Date_Time", "Not Available"))
        print("\t\t----------------------")


# ---------------- EXPENSE ----------------

class Expense:
    def __init__(self, expense_name, expense_amount):
        self.expense_name = expense_name
        self.expense_amount = expense_amount

    def display(self):
        print("\t\t----------------------")
        print("Name = ", self.expense_name)
        print("Amount = ", f"{self.expense_amount:.2f}")
        print("\t\t----------------------\n")
        



expenses = []

def load_expenses():
    try:
        with open("expenses.json","r") as file:
            data= json.load(file)
        expenses.clear()
        for item in data:
            expense = Expense(
                item["Expense_Name"],
                item["Expense_Amount"],
            )

            expenses.append(expense)
    except FileNotFoundError: 
        print("Expense file not found. Starting with empty Expense list.")
    except json.JSONDecodeError:
        print("Expense file contains invalid JSON data.")

def save_expenses():
    expense_data = []

    for expense in expenses:
        exp_dic = {
            "Expense_Name": expense.expense_name,
            "Expense_Amount": expense.expense_amount
        }

        expense_data.append(exp_dic)

    with open("expenses.json", "w") as file:
        json.dump(expense_data, file, indent=4)


def add_expense():
    try:
        expense_name = input("Enter the Expense Name: ").strip()
        if expense_name == "":
            print("Expense Name cannot be empty!")
            return
        expense_amount = float(input("Enter the Expense Amount: "))
                 # Value Validation
        if expense_amount <= 0:
            print("Expense Amount must be greater than 0!")
            return

        e1 = Expense(expense_name, expense_amount)

        expenses.append(e1)
        save_expenses()

        print("Expense Added Successfully")
    except ValueError:
        print("Invalid Input! Please enter numbers where required.")

# ---------------- VIEW EXPENSES ----------------

def view_expense():
    if not expenses:
        print("No Expenses available!")
        return
    for expen in expenses:
        expen.display()
        


# ---------------- REPORTS ----------------

def reports():
    total_profit= 0
    total_sales = 0
    total_expenses = 0
    total_stock = 0
    total_units_sold = 0
    total_inventory_value = 0
    total_products=len(products)

    #Total Stock + Inventory Value
    for product in products:
        total_stock=total_stock+product.quantity
        total_inventory_value = total_inventory_value + (product.price * product.quantity)

    # Total Sales + Total Profit 
    for sale in sales:
        total_sales = total_sales + sale["Total_sale"]

        total_units_sold = total_units_sold + sale["Quantity_Sold"]

        profit = (sale["Product_Price"] - sale["Cost_price"]) * sale["Quantity_Sold"]
        total_profit = total_profit + profit

    # Total Expenses
    for exp in expenses:
        total_expenses = total_expenses + exp.expense_amount

    # Average Sale
    if len(sales) > 0:
        average_sale = total_sales / len(sales)
    else:
        average_sale = 0

    # Best Selling Product
    product_sales = {}

    for sale in sales:
        product_name = sale["Product_Name"]
        quantity_sold = sale["Quantity_Sold"]

        if product_name in product_sales:
            product_sales[product_name] = product_sales[product_name] + quantity_sold
        else:
            product_sales[product_name] = quantity_sold

    best_product = None
    best_quantity = 0

    for product_name in product_sales:
        if product_sales[product_name] > best_quantity:
            best_quantity = product_sales[product_name]
            best_product = product_name

    
    # Profit Margin
    if total_sales > 0:
        profit_margin = (total_profit / total_sales) * 100
    else:
        profit_margin = 0

    # Net Profit
    net_amount = total_profit - total_expenses

    print("""
    --------------------------------
          BUSINESS REPORT
    --------------------------------""")
    print("Total Products = ", total_products)
    print("Total Stock Units = ", total_stock)
    print("Total Inventory Value = ", f"{total_inventory_value:.2f}")
    print("Total Units Sold = ", total_units_sold)
    print("Total Sales = ", f"{total_sales:.2f}")
    print("Average Sale = ", f"{average_sale:.2f}")
    print("Total Profit = ", f"{total_profit:.2f}")
    print("Profit Margin = ", f"{profit_margin:.2f}%")
    print("Total Expenses = ", f"{total_expenses:.2f}")

    if best_product:
        print("Best Selling Product = ", best_product)
        print("Units Sold = ", best_quantity)
    else:
        print("Best Selling Product = No Sales Yet")

    print("Net Profit = ", f"{net_amount:.2f}")
    print("--------------------------------")



def main_menu():

    while True:

        print("""
================================
   INVENTORY MANAGEMENT SYSTEM
================================

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
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            sell_product()

        elif choice == "7":
            add_expense()

        elif choice == "8":
            view_expense()

        elif choice == "9":
            view_sales()

        elif choice == "10":
            low_stock_alert()

        elif choice == "11":
            reports()

        elif choice == "12":
            print("Thank you for using Inventory Management System!")
            break

        else:
            print("Invalid Choice! Please try again.")

def main():
    load_products()
    load_sales()
    load_expenses()
    main_menu()


if __name__ == "__main__":
    main()