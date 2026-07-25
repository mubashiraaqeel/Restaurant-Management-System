import json
from datetime import datetime
# ==========================
# Classes
# ==========================

class MenuItem:
    
    def __init__(self,food_id,food_name,category,price,availability):
        
        self.food_id = food_id
        self.food_name = food_name
        self.category = category
        self.price = price
        self.availability = availability
        
    def display(self):
        
        print("------------------------------------------")
        print("Food ID      :" , self.food_id)
        print("Food Name    :" , self.food_name)
        print("Category     :" , self.category)
        print("Price        :" , self.price)
        print("Availability :" , self.availability)
        print("------------------------------------------")
        
    def to_dict(self):
        
        return{
            "food_id": self.food_id,
            "food_name": self.food_name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability
        }
        
    
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["food_id"],
            data["food_name"],
            data["category"],
            data["price"],
            data["availability"]
        )

        


class Customer:
    
    def __init__(self, customer_id, customer_name, phone_number, email, gender, visit_type):
        
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
        self.visit_type = visit_type
        
    def display(self):
            
        print("------------------------------------------")
        print("Customer ID   :", self.customer_id)
        print("Customer Name :", self.customer_name)
        print("Phone Number  :", self.phone_number)
        print("Email         :", self.email)
        print("Gender        :", self.gender)
        print("Visit Type    :", self.visit_type)
        print("------------------------------------------")
        
    def to_dict(self):
        
        return{ 
            "customer_id"   : self.customer_id,
            "customer_name" : self.customer_name,
            "phone_number"  : self.phone_number,
            "email"         : self.email,
            "gender"        : self.gender,
            "visit_type"    : self.visit_type
        }
        
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["customer_id"],
            data["customer_name"],
            data["phone_number"],
            data["email"],
            data["gender"],
            data["visit_type"]
        )


            

class Employee:
    
    def __init__(self, employee_id, employee_name, phone_number, position, email, salary, shift):
        
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.phone_number = phone_number
        self.position = position
        self.email = email
        self.salary = salary
        self.shift = shift
        
    def display(self):
        
        print("------------------------------------------")
        print("Employee ID   :", self.employee_id)
        print("Employee Name :", self.employee_name)
        print("Phone Number  :", self.phone_number)
        print("Position      :", self.position)
        print("Email         :", self.email)
        print("Salary        :", self.salary)
        print("Shift         :", self.shift)
        print("------------------------------------------")
        
    def to_dict(self):
        
        return{
            "employee_id"   : self.employee_id,
            "employee_name" : self.employee_name,
            "phone_number"  : self.phone_number,
            "position"      : self.position,
            "email"         : self.email,
            "salary"        : self.salary,
            "shift"         : self.shift
        }
        
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["employee_id"],
            data["employee_name"],
            data["phone_number"],
            data["position"],
            data["email"],
            data["salary"],
            data["shift"]
        )
        
    
                


class Table:
    
    def __init__(self, table_number, capacity, status, location):
        
        self.table_number = table_number
        self.capacity = capacity
        self.status = status
        self.location = location
        
    def display(self):
            
        print("------------------------------------------")
        print("Table Number  :", self.table_number)
        print("Capacity    :", self.capacity)
        print("Status      :", self.status)
        print("Location    :", self.location)
        print("------------------------------------------")
        
    def to_dict(self):
        
        return{
            "table_number" : self.table_number,
            "capacity"     :   self.capacity,
            "status"       : self.status,
            "location"     : self.location
        }
        
    @classmethod
    
    def from_dict(cls,data):
        
        return cls(
            data["table_number"],
            data["capacity"],
            data["status"],
            data["location"]
        )
            
    
class Order:
    
    def __init__(self, order_id, customer_id, table_number, items, total_amount, order_status, order_time):
        
        self.order_id = order_id
        self.customer_id = customer_id
        self.table_number = table_number
        self.items = items
        self.total_amount = total_amount
        self.order_status = order_status
        self.order_time = order_time
        
    def display(self):
        
        print("------------------------------------------")
        print("Order ID      :", self.order_id)
        print("Customer ID   :", self.customer_id)
        print("Table Number  :", self.table_number)
        print("Items         :", self.items)
        print("Total Amount  : Rs.", self.total_amount)
        print("Order Status  :", self.order_status)
        print("Order Time    :", self.order_time)      
        print("------------------------------------------")
        
        
    def to_dict(self):
        
        return{
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "table_number": self.table_number,
            "items": self.items,
            "total_amount": self.total_amount,
            "order_status": self.order_status,
            "order_time": self.order_time
        }
        
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["order_id"],
            data["customer_id"],
            data["table_number"],
            data["items"],
            data["total_amount"],
            data["order_status"],
            data["order_time"]
        )


class Invoice:
    
    def __init__(self, invoice_id, order_id, subtotal, discount, tax, invoice_date):
        
        self.invoice_id = invoice_id
        self.order_id = order_id      
        self.subtotal = subtotal
        self.discount = discount
        self.tax = tax
        self.grand_total = subtotal - discount + tax
        self.invoice_date = invoice_date
        
    def display(self):
        
        print("------------------------------------------") 
        print("Invoice ID    :", self.invoice_id)
        print("Order ID      :", self.order_id)
        print("Subtotal      : Rs.", self.subtotal)
        print("Discount      : Rs.", self.discount)
        print("Tax           : Rs.", self.tax)
        print("Grand Total   : Rs.", self.grand_total)
        print("Invoice Date  :", self.invoice_date)      
        print("------------------------------------------")
        
        
    def to_dict(self):
        
        return{
            "invoice_id": self.invoice_id,
            "order_id": self.order_id,
            "subtotal": self.subtotal,
            "discount": self.discount,
            "tax": self.tax,
            "grand_total": self.grand_total,
            "invoice_date": self.invoice_date
        }
        
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["invoice_id"],
            data["order_id"],
            data["subtotal"],
            data["discount"],
            data["tax"],
            data["invoice_date"]
        )



class Payment:
    
    def __init__(self, payment_id, invoice_id, payment_method, amount_paid, payment_status, payment_date, transaction_id):
        
        self.payment_id = payment_id
        self.invoice_id = invoice_id 
        self.payment_method = payment_method     
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.payment_date = payment_date
        self.transaction_id = transaction_id
        
    def display(self):
        
        print("------------------------------------------") 
        print("Payment ID       :", self.payment_id)
        print("Invoice ID       :", self.invoice_id)
        print("Payment Method   :", self.payment_method)
        print("Amount Paid      : Rs.", self.amount_paid)
        print("Payment Status   :", self.payment_status)
        print("Payment Date     :", self.payment_date)
        print("Transaction ID   :", self.transaction_id)      
        print("------------------------------------------")
  
    def to_dict(self):
        
        return{
            "payment_id": self.payment_id,
            "invoice_id": self.invoice_id,
            "payment_method": self.payment_method,
            "amount_paid": self.amount_paid,
            "payment_status": self.payment_status,
            "payment_date": self.payment_date,
            "transaction_id": self.transaction_id
        }
        
    @classmethod
    
    def from_dict(cls, data):
        
        return cls(
            data["payment_id"],
            data["invoice_id"],
            data["payment_method"],
            data["amount_paid"],
            data["payment_status"],
            data["payment_date"],
            data["transaction_id"]
        )


def load_data():

    global menu, customers, employees, tables, orders, invoices, payments

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        menu = [MenuItem.from_dict(item) for item in data.get("menu", [])]
        customers = [Customer.from_dict(item) for item in data.get("customers", [])]
        employees = [Employee.from_dict(item) for item in data.get("employees", [])]
        tables = [Table.from_dict(item) for item in data.get("tables", [])]
        orders = [Order.from_dict(item) for item in data.get("orders", [])]
        invoices = [Invoice.from_dict(item) for item in data.get("invoices", [])]
        payments = [Payment.from_dict(item) for item in data.get("payments", [])]

    except FileNotFoundError:
        menu = []
        customers = []
        employees = []
        tables = []
        orders = []
        invoices = []
        payments = []


def save_data():

    data = {
        "menu": [item.to_dict() for item in menu],
        "customers": [item.to_dict() for item in customers],
        "employees": [item.to_dict() for item in employees],
        "tables": [item.to_dict() for item in tables],
        "orders": [item.to_dict() for item in orders],
        "invoices": [item.to_dict() for item in invoices],
        "payments": [item.to_dict() for item in payments]
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# ==========================
# Menu Management
# ==========================

menu = []

def menu_management():
    
    while True:
    
        print("=================================================")
        print("                 MENU MANAGEMENT                 ")
        print("=================================================")
        print()
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Search Menu Item")
        print("4. Update Menu Item")
        print("5. Delete Menu Item")
        print("6. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-6): "))
            
            if choice == 1:
                add_menu_item()
                print()
            elif choice == 2:
                view_menu()
                print()
            elif choice == 3:
                search_menu_item()
                print()
            elif choice == 4:
                update_menu_item()
                print()
            elif choice == 5:
                delete_menu_item()
                print()
            elif choice == 6:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 6.")
                
        except ValueError:
            print("Please enter a number between 1 - 6.")    
            


def add_menu_item():
    
    while True:
    
        print("=================================================")
        print("                  ADD MENU ITEM                  ")
        print("=================================================")
        print()
        
        try:
            food_id = int(input("Enter Food ID: "))
            if food_id <= 0 :
                print("Invalid Food ID!")
                continue
                
            found = False
            
            for item in menu:
                if item.food_id == food_id:
                    
                    found = True
                    
                    print("Food ID already exists!")
                    break 
                
            if not found:
                
                food_name = input("Enter Food Name: ").strip().title()
                
                if food_name == "":
                    print("Food Name cannot be empty!")
                    continue
                    
                category = input("Enter Category: ").strip().title()
                
                if category == "":
                    print("Category cannot be empty!")
                    continue
                    
                price = float(input("Enter Price:"))
                
                if price <= 0:
                    print("Price cannot be lesser than zero!")
                    continue
                
                while True:
                
                    availability = input("Is the food available? (Yes/No): ").strip().lower()
    
                    if availability == "yes":
                        availability = True
                        break
    
                    elif availability == "no":
                        availability = False
                        break

                    else:
                        print("Please enter Yes or No.")
                    
                new_item = MenuItem(
                                food_id,
                                food_name,
                                category,
                                price,
                                availability
                            )

                menu.append(new_item)
                save_data()
                print("=================================================")
                print("          Menu item added successfully!          ")
                print("=================================================")
                break  
                
        except ValueError:
            print("Invalid Input!")
                        


def view_menu():
    
    print("=================================================")
    print("                    VIEW MENU                    ")
    print("=================================================")
    print()
    
    if len(menu) == 0:
        print("No menu items available!")
        return
        
    else:
        for item in menu:
            item.display()



def search_menu_item():
    
    while True:
    
        print("================================================")
        print("                SEARCH MENU ITEM                ")
        print("================================================")
        print()
        
        if len(menu) == 0:
            print("No menu items available!")
            return
            
        try:
            search = int(input("Search menu items by Food ID: "))
            
            found = False
            for item in menu:
                if search == item.food_id:
                    found = True
                    item.display()
                    break
                
            if not found:
                print("Food ID does not exist!")
                
            break
                        
        except ValueError:
            print("Invalid Food ID!")


def update_menu_item():
 
    while True:

        print("================================================")
        print("                UPDATE MENU ITEM                ")
        print("================================================")
        print()

        if len(menu) == 0:
            print("No menu items available!")
            return

        try:
            search = int(input("Enter Food ID to update: "))

            found = False

            for item in menu:
                
                if search == item.food_id:

                    found = True

                    print("Current Menu Item Details:")
                    item.display()

                    food_name = input("Enter New Food Name: ").strip().title()

                    if food_name == "":
                        print("Food Name cannot be empty!")
                        break

                    category = input("Enter New Category: ").strip().title()

                    if category == "":
                        print("Category cannot be empty!")
                        break

                    price = float(input("Enter New Price: "))

                    if price <= 0:
                        print("Price must be greater than zero!")
                        break

                    while True:

                        availability = input("Is the food available? (Yes/No): ").strip().lower()

                        if availability == "yes":
                            availability = True
                            break

                        elif availability == "no":
                            availability = False
                            break

                        else:
                            print("Please enter Yes or No.")

                    item.food_name = food_name
                    item.category = category
                    item.price = price
                    item.availability = availability

                    save_data()
                    
                    print("=================================================")
                    print("         Menu item updated successfully!         ")
                    print("=================================================")
                    break

            if not found:
                print("Food ID does not exist!")

            break

        except ValueError:
            print("Invalid Input!")


def delete_menu_item():
    print("=================================================")
    print("                   DELETE MENU                   ")
    print("=================================================")
    print()
    
    if len(menu) == 0:
        print("No menu items available!")
        return
    try:
        delete = int(input("Enter Food ID for Deletion: "))
        
        found = False
        for item in menu:
            
            if delete == item.food_id:
                found = True
                
                while True:
                    confirm = input("Are you sure you want to delete this item? (Yes/No): ").strip().lower()

                    if confirm == "yes":
                        menu.remove(item)
                        save_data()

                        print("=================================================")
                        print("         Menu item deleted successfully!         ")
                        print("=================================================")
                        break

                    elif confirm == "no":
                        print("Deletion cancelled!")
                        break

                    else:
                        print("Please enter Yes or No.")
                        
                        
                break
                
        if not found:
            print("Food ID does not exist!")

    except ValueError:
        print("Invalid Input!")

# ==========================
# Customer Management
# ==========================

customers = []

def customer_management():
    
    while True:
    
        print("=================================================")
        print("               CUSTOMER MANAGEMENT               ")
        print("=================================================")
        print()
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-6): "))
            
            if choice == 1:
                add_customer()
                print()
            elif choice == 2:
                view_customers()
                print()
            elif choice == 3:
                search_customer()
                print()
            elif choice == 4:
                update_customer()
                print()
            elif choice == 5:
                delete_customer()
                print()
            elif choice == 6:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 6.")
                
        except ValueError:
            print("Please enter a number between 1 - 6.") 


def add_customer():
    
    while True:    
    
        print("=================================================")
        print("                 ADD CUSTOMER                    ")
        print("=================================================")
        print()
        
        try:
            customer_id = int(input("Enter Customer ID: "))
            
            if customer_id <= 0:
                print("Invalid Customer ID!")
                continue
            
            found = False
            
            for item in customers:
                
                if customer_id == item.customer_id:
                
                    found = True
                    print("Customer ID already exists!")
                    break
                
            if not found:
                
                customer_name = input("Enter Customer Name: ").strip().title()
                    
                if customer_name  == "":
                    print("Customer name cannot be empty!")
                    continue
                    
                phone_number = input("Enter Phone Number: ").strip()
                
                if phone_number == "":
                    print("Phone Number cannot be empty!")
                    continue
                    
                if len(phone_number) != 11 or not phone_number.isdigit():
                    print("Invalid Phone Number!")
                    continue
            
                email = input("Enter Email: ").strip().lower()
                
                if email == "":
                    print("Email cannot be empty!")
                    continue
                        
                if "@" not in email or "." not in email :
                    print("Invalid Email!")
                    continue
                    
                while True:
                 
                    gender = input("Enter Gender (Male/Female/Other): ").strip().title()
                    
                    if gender == "":
                        print("Gender cannot be empty!")
                        continue
                       
                    if gender == "Male":
                        gender = "Male"
                        break
                            
                    elif gender == "Female":
                        gender = "Female"
                        break
                            
                    elif gender == "Other":
                        gender = "Other"
                        break
                            
                    else:
                        print("Please enter the gender correct (Male, Female, Other)!")
                    
                while True:
                    
                    visit_type = input("Enter Visit Type (Dine In/Take Away/Delivery): ").strip().title()
                            
                    if visit_type == "":
                        print("Visit Type cannot be empty!")
                        continue
                            
                    if visit_type == "Dine In":
                        visit_type = "Dine In"
                        break
                            
                    elif visit_type == "Take Away":
                        visit_type = "Take Away"
                        break
                            
                    elif visit_type == "Delivery":
                        visit_type = "Delivery"
                        break
                            
                    else:
                        print("Please Enter the Visit Type (Dine In, Take Away, Delivery)!")                     
                    
                customer = Customer(
                            customer_id,
                            customer_name,
                            phone_number,
                            email,
                            gender,
                            visit_type
                        )
                    
                customers.append(customer)
                save_data()
                    
                print("==================================================")
                print("           Customer added successfully!           ")
                print("==================================================")
                break   
                    
        except ValueError:
            print("Invalid Input!")


                

def view_customers():
    
    print("================================================")
    print("                 VIEW CUSTOMERS                 ")
    print("================================================")
    print()
    
    if len(customers) == 0:
        print("No customers available!")
        return
    
    for item in customers:
        item.display()


def search_customer():
    
    while True:    
    
        print("==================================================")
        print("                SEARCH CUSTOMER                   ")
        print("==================================================")
        print()
        
        if len(customers) == 0:
            print("No customers available!")
            return
        
        try:
            customer_id = int(input("Search Customers by Customer ID: "))
            
            found = False
            
            for item in customers:
                
                if customer_id == item.customer_id:
                    found = True
                    item.display()
                    break
                
            if not found:
                print("Customer ID does not exist!")
                continue
            
            break
            
        except ValueError:
            print("Invalid Customer ID!")
            
                                    
def update_customer():

    while True:

        print("==================================================")
        print("                UPDATE CUSTOMER                   ")
        print("==================================================")
        print()

        if len(customers) == 0:
            print("No customers available!")
            return

        try:
            customer_id = int(input("Enter Customer ID to update: "))

            found = False

            for item in customers:

                if customer_id == item.customer_id:

                    found = True

                    print("\nCurrent Customer Details:")
                    item.display()

                    customer_name = input("Enter New Customer Name: ").strip().title()

                    if customer_name == "":
                        print("Customer Name cannot be empty!")
                        break

                    phone_number = input("Enter New Phone Number: ").strip()

                    if phone_number == "":
                        print("Phone Number cannot be empty!")
                        break

                    if len(phone_number) != 11 or not phone_number.isdigit():
                        print("Invalid Phone Number!")
                        break

                    email = input("Enter New Email: ").strip().lower()

                    if email == "":
                        print("Email cannot be empty!")
                        break

                    if "@" not in email or "." not in email:
                        print("Invalid Email!")
                        break

                    while True:

                        gender = input("Enter Gender (Male/Female/Other): ").strip().title()

                        if gender == "":
                            print("Gender cannot be empty!")
                            continue

                        if gender == "Male":
                            gender = "Male"
                            break

                        elif gender == "Female":
                            gender = "Female"
                            break

                        elif gender == "Other":
                            gender = "Other"
                            break

                        else:
                            print("Please enter Male, Female or Other!")

                    while True:

                        visit_type = input("Enter Visit Type (Dine In/Take Away/Delivery): ").strip().title()

                        if visit_type == "":
                            print("Visit Type cannot be empty!")
                            continue

                        if visit_type == "Dine In":
                            visit_type = "Dine In"
                            break
                            
                        elif visit_type == "Take Away":
                            visit_type = "Take Away"
                            break
                            
                        elif visit_type == "Delivery":
                            visit_type = "Delivery"
                            break

                        else:
                            print("Please enter Dine In, Take Away or Delivery!")

                    item.customer_name = customer_name
                    item.phone_number = phone_number
                    item.email = email
                    item.gender = gender
                    item.visit_type = visit_type

                    save_data()

                    print("==================================================")
                    print("        Customer updated successfully!           ")
                    print("==================================================")

                    break

            if not found:
                print("Customer ID does not exist!")

            break

        except ValueError:
            print("Invalid Customer ID!")


def delete_customer():
    
    print("=================================================")
    print("                 DELETE CUSTOMER                 ")
    print("=================================================")
    print()
    
    if len(customers) == 0:
        print("No customers available!")
        return
    try:
        delete = int(input("Enter Customer ID for Deletion: "))
        
        found = False
        for item in customers:
            
            if delete == item.customer_id:
                found = True
                
                while True:
                    confirm = input("Are you sure you want to delete this customer? (Yes/No): ").strip().lower()

                    if confirm == "yes":
                        customers.remove(item)
                        save_data()

                        print("================================================")
                        print("         Customer deleted successfully!         ")
                        print("================================================")
                        break

                    elif confirm == "no":
                        print("Deletion cancelled!")
                        break

                    else:
                        print("Please enter Yes or No.")
                        
                break
                
        if not found:
            print("Customer ID does not exist!")

    except ValueError:
        print("Invalid Input!")


# ==========================
# Employee Management
# ==========================

employees = []

def employee_management():
    
    while True:
    
        print("=================================================")
        print("               EMPLOYEE MANAGEMENT               ")
        print("=================================================")
        print()
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-6): "))
            
            if choice == 1:
                add_employee()
                print()
            elif choice == 2:
                view_employees()
                print()
            elif choice == 3:
                search_employee()
                print()
            elif choice == 4:
                update_employee()
                print()
            elif choice == 5:
                delete_employee()
                print()
            elif choice == 6:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 6.")
                
        except ValueError:
            print("Please enter a number between 1 - 6.") 
    


def add_employee():
    
    while True:    
    
        print("=================================================")
        print("                 ADD EMPLOYEE                    ")
        print("=================================================")
        print()
        
        try:
            employee_id = int(input("Enter Employee ID: "))
            
            if employee_id <= 0:
                print("Invalid Employee ID!")
                continue
            
            found = False
            
            for item in employees:
                
                if employee_id == item.employee_id:
                
                    found = True
                    print("Employee ID already exists!")
                    break
                
            if not found:
                
                employee_name = input("Enter Employee Name: ").strip().title()
                    
                if employee_name  == "":
                    print("Employee name cannot be empty!")
                    continue
                    
                phone_number = input("Enter Phone Number: ").strip()
                
                if phone_number == "":
                    print("Phone Number cannot be empty!")
                    continue
                    
                if len(phone_number) != 11 or not phone_number.isdigit():
                    print("Invalid Phone Number!")
                    continue
                
                while True:
                
                    position = input("Enter position: ").strip().title()
                
                    if position == "":
                        print("Position cannot be empty!")
                        continue
                        
                    if position == "Chef":
                        position = "Chef"
                        break
                    elif position == "Manager":
                        position = "Manager"
                        break
                    elif position == "Cashier":
                        position = "Cashier"
                        break
                    elif position == "Cleaner":
                        position = "Cleaner"
                        break
                    elif position == "Waiter":
                        position = "Waiter"
                        break
                    else:
                        print("Please enter a correct position!")
                   
            
                email = input("Enter Email: ").strip().lower()
                
                if email == "":
                    print("Email cannot be empty!")
                    continue
                        
                if "@" not in email or "." not in email :
                    print("Invalid Email!")
                    continue
                    
                salary = float(input("Enter salary: "))
                
                if salary <= 0:
                    print("Salary cannot be lesser than zero!")
                    continue
                 
                while True:
                       
                    shift = input("Enter shift: ").strip().title()
                    
                    if shift == "":
                        print("Shift cannot be empty!")
                        continue
               
                    if shift == "Morning":
                        shift = "Morning"
                        break
                    elif shift == "Evening":
                        shift = "Evening"
                        break
                    elif shift == "Night":
                        shift = "Night"
                        break
                    
                    else:
                        print("Enter correct shift (Morning, Evening, Night)")                    
                    
                employee = Employee(
                            employee_id,
                            employee_name,
                            phone_number,
                            position,
                            email,
                            salary,
                            shift
                        )
                    
                employees.append(employee)
                save_data()
                    
                print("==================================================")
                print("           Employee added successfully!           ")
                print("==================================================")
                break   
                    
        except ValueError:
            print("Invalid Input!")
    


def view_employees():
    
    print("===================================================")
    print("                 VIEW EMPLOYEES                    ")
    print("===================================================")
    print()
        
    if len(employees) == 0:
        print("No employees available!")
        return
    
    for item in employees:
        item.display()
            


def search_employee():
    
    while True:    
    
        print("==================================================")
        print("                SEARCH EMPLOYEE                   ")
        print("==================================================")
        print()
        
        if len(employees) == 0:
            print("No employees available!")
            return
        
        try:
            employee_id = int(input("Search Employees by Employee ID: "))
            
            found = False
            
            for item in employees:
                
                if employee_id == item.employee_id:
                    found = True
                    item.display()
                    break
                
            if not found:
                print("Employee ID does not exist!")
                continue
            
            break
            
        except ValueError:
            print("Invalid Employee ID!")


def update_employee():

    while True:

        print("==================================================")
        print("                UPDATE EMPLOYEE                   ")
        print("==================================================")
        print()

        if len(employees) == 0:
            print("No employees available!")
            return

        try:
            employee_id = int(input("Enter Employee ID to update: "))

            found = False

            for item in employees:

                if employee_id == item.employee_id:

                    found = True

                    print("Current Employee Details:")
                    item.display()

                    employee_name = input("Enter New Employee Name: ").strip().title()

                    if employee_name == "":
                        print("Employee name cannot be empty!")
                        continue

                    phone_number = input("Enter New Phone Number: ").strip()

                    if phone_number == "":
                        print("Phone Number cannot be empty!")
                        continue

                    if len(phone_number) != 11 or not phone_number.isdigit():
                        print("Invalid Phone Number!")
                        continue

                    while True:

                        position = input("Enter New Position: ").strip().title()

                        if position == "":
                            print("Position cannot be empty!")
                            continue

                        if position == "Chef":
                            break

                        elif position == "Manager":
                            break

                        elif position == "Cashier":
                            break

                        elif position == "Cleaner":
                            break

                        elif position == "Waiter":
                            break

                        else:
                            print("Please enter a correct position!")

                    email = input("Enter New Email: ").strip().lower()

                    if email == "":
                        print("Email cannot be empty!")
                        continue

                    if "@" not in email or "." not in email:
                        print("Invalid Email!")
                        continue

                    salary = float(input("Enter New Salary: "))

                    if salary <= 0:
                        print("Salary cannot be less than zero!")
                        continue

                    while True:

                        shift = input("Enter New Shift: ").strip().title()

                        if shift == "":
                            print("Shift cannot be empty!")
                            continue

                        if shift == "Morning":
                            break

                        elif shift == "Evening":
                            break

                        elif shift == "Night":
                            break

                        else:
                            print("Please enter Morning, Evening or Night!")

                    item.employee_name = employee_name
                    item.phone_number = phone_number
                    item.position = position
                    item.email = email
                    item.salary = salary
                    item.shift = shift

                    save_data()

                    print("==================================================")
                    print("        Employee updated successfully!           ")
                    print("==================================================")

                    break

            if not found:
                print("Employee ID does not exist!")

            break

        except ValueError:
            print("Invalid Employee ID!")


def delete_employee():
    
    print("===================================================")
    print("                 DELETE EMPLOYEE                   ")
    print("===================================================")
    print()
        
    if len(employees) == 0:
        print("No employees available!")
        return
    
    try:
        delete = int(input("Enter Employee ID for deletion: "))
        
        found = False
        
        for item in employees:
            if delete == item.employee_id:
                found = True
                
                while True:
                    confirm = input("Are you sure you want to delete this employee?(Yes/No): ").lower().strip()
                
                    if confirm == "yes":
                        employees.remove(item)
                        save_data()
                    
                        print("========================================================")
                        print("             Employee deleted successfully!             ")
                        print("========================================================")
                        break
                    
                    elif confirm == "no":
                        print("Deletion cancelled!")
                        break
                    
                    else:
                        print("Please enter Yes or No!")
                break
                    
        if not found:
            print("Employee ID does not exist!")
                    
    except ValueError:
        print("Invalid Input!")
    
    
# ==========================
# Table Management
# ==========================

tables = []

def table_management():
    
    while True:
    
        print("==================================================")
        print("                 TABLE MANAGEMENT                 ")
        print("==================================================")
        print()
        print("1. View Tables")
        print("2. Reserve Table")
        print("3. Release Table")
        print("4. Search Table")
        print("5. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-5): "))
            
            if choice == 1:
                view_tables()
                print()
            elif choice == 2:
                reserve_table()
                print()
            elif choice == 3:
                release_table()
                print()
            elif choice == 4:
                search_table()
                print()
            elif choice == 5:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Please enter a number between 1 - 5.") 


def view_tables():
    
    print("===================================================")
    print("                    VIEW TABLES                    ")
    print("===================================================")
    print()
    
    if len(tables) == 0:
        print("No tables available!")
        return
        
    for item in tables:
        item.display()


def reserve_table():

    while True:

        print("===================================================")
        print("                  RESERVE TABLE                    ")
        print("===================================================")
        print()

        if len(tables) == 0:
            print("No tables available!")
            return

        try:
            table_number = int(input("Enter Table Number for reservation: "))
            
            found = False
            
            for item in tables:
                if table_number == item.table_number:
                    found = True
                    
                    if item.status == "Reserved":
                        print("Table already reserved!")
                        break
                        
                    elif item.status == "Available":
                        item.status = "Reserved"
                        save_data()
                        
                        print("====================================================")
                        print("            Table reserved successfully!            ")
                        print("====================================================")
                        return      
                    
            if not found:
                print("Table Number does not exist!")
                
            break
        
        except ValueError:
            print("Invalid Input!")
            
                        
def release_table():
    
    while True:

        print("===================================================")
        print("                  RELEASE TABLE                    ")
        print("===================================================")
        print()

        if len(tables) == 0:
            print("No tables available!")
            return

        try:
            table_number = int(input("Enter Table Number for release: "))
            
            found = False
            
            for item in tables:
                if table_number == item.table_number:
                    found = True
                    
                    if item.status == "Available":
                        print("Table already available!")
                        break
                        
                    elif item.status == "Reserved":
                        item.status = "Available"
                        save_data()
                        
                        print("====================================================")
                        print("            Table released successfully!            ")
                        print("====================================================")
                        return      
                    
            if not found:
                print("Table Number does not exist!")
                
            break
        
        except ValueError:
            print("Invalid Input!")


def search_table():
    
    while True:

        print("==================================================")
        print("                  SEARCH TABLE                    ")
        print("==================================================")
        print()

        if len(tables) == 0:
            print("No tables available!")
            return

        try:
            table_number = int(input("Enter Table Number to search: "))
            
            found = False
            
            for item in tables:
                if table_number == item.table_number:
                    found = True
                    item.display()
                    break
                          
            if not found:
                print("Table Number does not exist!")
                continue
                
            break
        
        except ValueError:
            print("Invalid Input!")


# ==========================
# Order Management
# ==========================

orders = []

def order_management():
    
    while True:
    
        print("==================================================")
        print("                 ORDER MANAGEMENT                 ")
        print("==================================================")
        print()
        print("1. Place Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Update Order")
        print("5. Complete Order")
        print("6. Cancel Order")
        print("7. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-7): "))
            
            if choice == 1:
                place_order()
                print()
            elif choice == 2:
                view_orders()
                print()
            elif choice == 3:
                search_order()
                print()
            elif choice == 4:
                update_order()
                print()
            elif choice == 5:
                complete_order()
                print()   
            elif choice == 6:
                cancel_order()
                print()
            elif choice == 7:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 7.")
                
        except ValueError:
            print("Please enter a number between 1 - 7.") 
    


def place_order():

    while True:

        print("===================================================")
        print("                  PLACE ORDER                      ")
        print("===================================================")
        print()

        if len(customers) == 0:
            print("No customers available!")
            return

        if len(menu) == 0:
            print("No menu items available!")
            return

        try:

            order_id = int(input("Enter Order ID: "))

            if order_id <= 0:
                print("Order ID cannot be less than or equal to zero!")
                continue

            found = False

            for item in orders:
                if order_id == item.order_id:
                    found = True
                    print("Order ID already exists!")
                    break

            if found:
                continue

            customer_id = int(input("Enter Customer ID: "))

            if customer_id <= 0:
                print("Customer ID cannot be less than or equal to zero!")
                continue

            found_customer = False
            table_number = 0
            

            for customer in customers:

                if customer.customer_id == customer_id:

                    found_customer = True

                    if customer.visit_type == "Dine In":

                        table_number = int(input("Enter Table Number: "))

                        found_table = False
                        table_available = False

                        for table in tables:

                            if table.table_number == table_number:

                                found_table = True

                                if table.status == "Reserved":
                                    print("Table already reserved! Please choose another table.")
                                    break

                                elif table.status == "Available":
                                    table.status = "Reserved"
                                    table_available = True
                                    break

                        if not found_table:
                            print("Table Number does not exist!")
                            continue
                        
                        if not table_available:
                            continue
                        
                        
                    elif customer.visit_type == "Take Away":

                        table_number = 0
                        print("Take Away Order Selected.")

                    elif customer.visit_type == "Delivery":

                        table_number = 0
                        print("Delivery Order Selected.")


                    break

            if not found_customer:
                print("Customer ID does not exist!")
                continue

            items = []
            total_amount = 0
            
            while True:

                print()
                print("================ MENU ================")
                view_menu()

                food_id = int(input("Enter Food ID: "))

                found_food = False
                food_added = False

                for item in menu:

                    if item.food_id == food_id:

                        found_food = True

                        if not item.availability:
                            print("Selected food item is currently unavailable.")
                            break

                        quantity = int(input("Enter Quantity: "))

                        if quantity <= 0:
                            print("Quantity must be greater than zero!")
                            break

                        subtotal = item.price * quantity

                        items.append({
                            "food_id": item.food_id,
                            "food_name": item.food_name,
                            "price": item.price,
                            "quantity": quantity,
                            "subtotal": subtotal
                        })

                        total_amount += subtotal
                        food_added = True

                        print(f"'{item.food_name}' added successfully! (x{quantity})")
                        break

                if not found_food:
                    print("Food ID does not exist!")
                    continue
                
                if not food_added:
                    continue

                while True:

                    another = input("Add another food item? (Yes/No): ").strip().lower()

                    if another == "yes":
                        break

                    elif another == "no":

                        order_status = "Pending"
                        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        print()
                        print("===================================================")
                        print("                  ORDER SUMMARY                    ")
                        print("===================================================")
                        print("Order ID      :",order_id)
                        print("Customer ID   :",customer_id)
                        
                        for customer in customers:
                            if customer.customer_id == customer_id:
                                print("Visit Type    :", customer.visit_type)
                                break

                        if table_number != 0:
                            print("Table Number  :", table_number)
                            
                        print("Order Status  :",order_status)
                        print("Order Time    :",order_time)

                        print()

                        print("-" * 55)
                        print(f"{'Food':20}{'Qty':>8}{'Price':>12}{'Subtotal':>15}")
                        print("-" * 55)

                        for item in items:

                            print(
                                f"{item['food_name'][:20]:20}"
                                f"{item['quantity']:>8}"
                                f"{item['price']:>12.2f}"
                                f"{item['subtotal']:>15.2f}"
                            )

                        print("-" * 55)
                        print(f"{'TOTAL AMOUNT':>40} : Rs. {total_amount:.2f}")
                        print("=" * 55)

                        while True:

                            confirm = input("Confirm Order? (Yes/No): ").strip().lower()

                            if confirm == "yes":

                                order = Order(
                                    order_id,
                                    customer_id,
                                    table_number,
                                    items,
                                    total_amount,
                                    order_status,
                                    order_time
                                )

                                orders.append(order)
                                save_data()

                                print("===================================================")
                                print("          Order placed successfully!               ")
                                print("===================================================")

                                return

                            elif confirm == "no":

                                if table_number != 0:

                                    for table in tables:
                                        if table.table_number == table_number:
                                            table.status = "Available"
                                            break

                                    save_data()

                                print("Order cancelled!")
                                return
                            
                            else:
                                print("Please enter Yes or No.")
                    
                    else:
                        print("Please enter Yes or No.")
    
        except ValueError:
            print("Invalid Input!")
            continue
             
                
                


def view_orders():

    print("===================================================")
    print("                  VIEW ORDERS                      ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders found!")
        return

    for food in orders:

        print("===================================================")
        print("Order ID      :", food.order_id)
        print("Customer ID   :", food.customer_id)

        # Show Visit Type
        for customer in customers:
            if customer.customer_id == food.customer_id:
                print("Visit Type    :", customer.visit_type)
                break

        # Show Table Number only for Dine In
        if food.table_number != 0:
            print("Table Number  :", food.table_number)

        print("Order Status  :", food.order_status)
        print("Order Time    :", food.order_time)
        print()

        print("-" * 55)
        print(f"{'Food':20}{'Qty':>8}{'Price':>12}{'Subtotal':>15}")
        print("-" * 55)

        for item in food.items:

            print(
                f"{item['food_name'][:20]:20}"
                f"{item['quantity']:>8}"
                f"{item['price']:>12.2f}"
                f"{item['subtotal']:>15.2f}"
            )

        print("-" * 55)
        print(f"{'TOTAL AMOUNT':>40} : Rs. {food.total_amount:.2f}")
        print("=" * 55)
        print()


def search_order():

    print("===================================================")
    print("                 SEARCH ORDER                      ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders available!")
        return

    try:

        order_id = int(input("Enter Order ID: "))

        if order_id <= 0:
            print("Order ID must be greater than zero!")
            return

        found = False

        for order in orders:

            if order.order_id == order_id:

                found = True

                print()
                print("===================================================")
                print("                ORDER DETAILS                      ")
                print("===================================================")
                print("Order ID      :", order.order_id)
                print("Customer ID   :", order.customer_id)

                for customer in customers:
                    if customer.customer_id == order.customer_id:
                        print("Visit Type    :", customer.visit_type)
                        break

                if item.table_number != 0:
                    print("Table Number  :", order.table_number)

                print("Order Status  :", order.order_status)
                print("Order Time    :", order.order_time)
                print()

                print("-" * 55)
                print(f"{'Food':20}{'Qty':>8}{'Price':>12}{'Subtotal':>15}")
                print("-" * 55)

                for item in order.items:

                    print(
                        f"{item['food_name'][:20]:20}"
                        f"{item['quantity']:>8}"
                        f"{item['price']:>12.2f}"
                        f"{item['subtotal']:>15.2f}"
                    )

                print("-" * 55)
                print(f"{'TOTAL AMOUNT':>40} : Rs. {order.total_amount:.2f}")
                print("=" * 55)

                break

        if not found:
            print("Order ID does not exist!")

    except ValueError:
        print("Invalid Input!")


def update_order():

    print("===================================================")
    print("                 UPDATE ORDER                      ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders available!")
        return

    try:

        order_id = int(input("Enter Order ID: "))

        if order_id <= 0:
            print("Order ID must be greater than zero!")
            return

        found = False

        for item in orders:

            if item.order_id == order_id:

                found = True

                print()
                print("Current Order Status :", item.order_status)
                print()
                print("1. Pending")
                print("2. Preparing")
                print("3. Ready")
                print("4. Completed")
                print("5. Cancelled")
                print()

                choice = int(input("Select New Status (1-5): "))

                if choice == "1":
                    item.order_status = "Pending"

                elif choice == "2":
                    item.order_status = "Preparing"

                elif choice == "3":
                    item.order_status = "Ready"

                elif choice == "4":
                    item.order_status = "Completed"

                elif choice == "5":
                    item.order_status = "Cancelled"

                else:
                    print("Invalid choice!")
                    return

                save_data()

                print()
                print("===================================================")
                print("     Order status updated successfully!           ")
                print("===================================================")

                return

        if not found:
            print("Order ID does not exist!")

    except ValueError:
        print("Invalid Input!")


def complete_order():
    
    print("===================================================")
    print("                COMPLETE ORDER                     ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders available!")
        return

    try:

        order_id = int(input("Enter Order ID: "))

        if order_id <= 0:
            print("Order ID must be greater than zero!")
            return

        found = False

        for item in orders:

            if item.order_id == order_id:

                found = True

                if item.order_status == "Completed":
                    print("Order is already completed!")
                    return

                if item.order_status == "Cancelled":
                    print("Cancelled orders cannot be completed!")
                    return

                item.order_status = "Completed"

                if item.table_number != 0:

                    for table in tables:

                        if table.table_number == item.table_number:
                            table.status = "Available"
                            break

                save_data()

                print()
                print("===================================================")
                print("        Order completed successfully!             ")
                print("===================================================")

                return

        if not found:
            print("Order ID does not exist!")

    except ValueError:
        print("Invalid Input!")



def cancel_order():

    print("===================================================")
    print("                 CANCEL ORDER                      ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders available!")
        return

    try:

        order_id = int(input("Enter Order ID: "))

        if order_id <= 0:
            print("Order ID must be greater than zero!")
            return

        found = False

        for order in orders:

            if order.order_id == order_id:

                found = True

                if order.order_status == "Cancelled":
                    print("Order is already cancelled!")
                    return

                if order.order_status == "Completed":
                    print("Completed orders cannot be cancelled!")
                    return

                confirm = input("Are you sure you want to cancel this order? (Yes/No): ").strip().lower()

                if confirm == "yes":

                    order.order_status = "Cancelled"

                    if order.table_number != 0:

                        for table in tables:

                            if table.table_number == order.table_number:
                                table.status = "Available"
                                break

                    save_data()

                    print()
                    print("===================================================")
                    print("         Order cancelled successfully!            ")
                    print("===================================================")

                elif confirm == "no":
                    print("Order cancellation cancelled.")

                else:
                    print("Please enter Yes or No.")

                return

        if not found:
            print("Order ID does not exist!")

    except ValueError:
        print("Invalid Input!")


# ==========================
# Billing & Invoice
# ==========================

invoices = []

def billing_management():
    
    while True:
    
        print("====================================================")
        print("                 BILLING MANAGEMENT                 ")
        print("====================================================")
        print()
        print("1. Generate Invoice")
        print("2. View Invoice")
        print("3. Apply Discount")
        print("4. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-4): "))
            
            if choice == 1:
                generate_invoice()
                print()
            elif choice == 2:
                view_invoices()
                print()
            elif choice == 3:
                apply_discount()
                print()
            elif choice == 4:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 4.")
                
        except ValueError:
            print("Please enter a number between 1 - 4.") 


def generate_invoice():

    print("===================================================")
    print("                 GENERATE INVOICE                  ")
    print("===================================================")
    print()

    if len(orders) == 0:
        print("No orders available!")
        return

    try:

        order_id = int(input("Enter Order ID: "))

        if order_id <= 0:
            print("Order ID must be greater than zero!")
            return

        found_order = False

        for item in orders:

            if item.order_id == order_id:

                found_order = True

                if item.order_status != "Completed":
                    print("Invoice can only be generated for completed orders!")
                    return

                for invoice in invoices:
                    if invoice.order_id == order_id:
                        print("Invoice already exists for this order!")
                        return

                invoice_id = int(input("Enter Invoice ID: "))

                if invoice_id <= 0:
                    print("Invoice ID must be greater than zero!")
                    return

                duplicate = False

                for invoice in invoices:
                    if invoice.invoice_id == invoice_id:
                        duplicate = True
                        print("Invoice ID already exists!")
                        break

                if duplicate:
                    return

                subtotal = item.total_amount

                discount_percent = float(input("Enter Discount (%): "))

                if discount_percent < 0:
                    print("Discount cannot be negative!")
                    return

                tax_percent = float(input("Enter Tax (%): "))

                if tax_percent < 0:
                    print("Tax cannot be negative!")
                    return

                discount = subtotal * discount_percent / 100
                tax = (subtotal - discount) * tax_percent / 100
                grand_total = subtotal - discount + tax

                invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                invoice = Invoice(
                    invoice_id,
                    order_id,
                    subtotal,
                    discount,
                    tax,
                    invoice_date
                )

                invoices.append(invoice)
                save_data()

                print()
                print("===================================================")
                print("                    INVOICE                        ")
                print("===================================================")
                print(f"Invoice ID     : {invoice_id}")
                print(f"Order ID       : {order_id}")
                print(f"Subtotal       : Rs. {subtotal:.2f}")
                print(f"Discount       : Rs. {discount:.2f}")
                print(f"Tax            : Rs. {tax:.2f}")
                print(f"Grand Total    : Rs. {invoice.grand_total:.2f}")
                print(f"Invoice Date   : {invoice_date}")
                print("===================================================")
                print("Invoice generated successfully!")
                print("===================================================")

                return

        if not found_order:
            print("Order ID does not exist!")

    except ValueError:
        print("Invalid Input!")


def view_invoices():

    print("==============================================================")
    print("                        VIEW INVOICES                         ")
    print("==============================================================")
    print()

    if len(invoices) == 0:
        print("No invoices available!")
        return

    print("-" * 95)
    print(f"{'ID':<8}{'Order ID':<12}{'Subtotal':<15}{'Discount':<15}{'Tax':<12}{'Grand Total':<15}")
    print("-" * 95)

    for item in invoices:

        print(
            f"{item.invoice_id:<8}"
            f"{item.order_id:<12}"
            f"Rs.{item.subtotal:<12.2f}"
            f"Rs.{item.discount:<12.2f}"
            f"Rs.{item.tax:<9.2f}"
            f"Rs.{item.grand_total:<12.2f}"
        )

    print("-" * 95)

    print()
    print("==============================================================")
    print("                  INVOICE DETAILS                             ")
    print("==============================================================")

    for item in invoices:

        print(f"Invoice ID   : {item.invoice_id}")
        print(f"Order ID     : {item.order_id}")
        print(f"Subtotal     : Rs. {item.subtotal:.2f}")
        print(f"Discount     : Rs. {item.discount:.2f}")
        print(f"Tax          : Rs. {item.tax:.2f}")
        print(f"Grand Total  : Rs. {item.grand_total:.2f}")
        print(f"Invoice Date : {item.invoice_date}")
        print("-" * 50)


def apply_discount():

    print("===================================================")
    print("                 APPLY DISCOUNT                    ")
    print("===================================================")
    print()

    try:

        subtotal = float(input("Enter Subtotal Amount: Rs. "))

        if subtotal <= 0:
            print("Subtotal must be greater than zero!")
            return

        discount_percent = float(input("Enter Discount Percentage (%): "))

        if discount_percent < 0 or discount_percent > 100:
            print("Discount percentage must be between 0 and 100!")
            return

        discount = subtotal * discount_percent / 100
        final_amount = subtotal - discount

        print()
        print("===================================================")
        print("              DISCOUNT DETAILS                     ")
        print("===================================================")
        print(f"Subtotal           : Rs. {subtotal:.2f}")
        print(f"Discount ({discount_percent:.0f}%) : Rs. {discount:.2f}")
        print(f"Amount After Discount : Rs. {final_amount:.2f}")
        print("===================================================")

    except ValueError:
        print("Invalid Input!")


# ==========================
# Payment Management
# ==========================

payments = []

def payment_management():
    
    while True:
    
        print("====================================================")
        print("                 PAYMENT MANAGEMENT                 ")
        print("====================================================")
        print()
        print("1. Make Payment")
        print("2. Payment History")
        print("3. Search Payment")
        print("4. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-4): "))
            
            if choice == 1:
                make_payment()
                print()
            elif choice == 2:
                payment_history()
                print()
            elif choice == 3:
                search_payment()
                print()
            elif choice == 4:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 4.")
                
        except ValueError:
            print("Please enter a number between 1 - 4.") 


def make_payment():

    print("===================================================")
    print("                  MAKE PAYMENT                     ")
    print("===================================================")
    print()

    if len(invoices) == 0:
        print("No invoices available!")
        return

    try:

        payment_id = int(input("Enter Payment ID: "))

        if payment_id <= 0:
            print("Payment ID must be greater than zero!")
            return

        for item in payments:
            if item.payment_id == payment_id:
                print("Payment ID already exists!")
                return

        invoice_id = int(input("Enter Invoice ID: "))

        if invoice_id <= 0:
            print("Invoice ID must be greater than zero!")
            return

        found_invoice = False

        for invoice in invoices:

            if invoice.invoice_id == invoice_id:

                found_invoice = True

                for item in payments:
                    if item.invoice_id == invoice_id:
                        print("Payment has already been made for this invoice!")
                        return

                print()
                print("Payment Methods")
                print("1. Cash")
                print("2. Credit Card")
                print("3. Debit Card")
                print("4. Online Payment")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    payment_method = "Cash"

                elif choice == 2:
                    payment_method = "Credit Card"

                elif choice == 3:
                    payment_method = "Debit Card"

                elif choice == 4:
                    payment_method = "Online Payment"

                else:
                    print("Invalid choice!")
                    return

                payment_status = "Paid"
                payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                transaction_id = f"TXN{payment_id}"
                
                amount_paid = invoice.grand_total

                payment = Payment(
                    payment_id,
                    invoice_id,
                    payment_method,
                    amount_paid,
                    payment_status,
                    payment_date,
                    transaction_id
                )

                payments.append(payment)
                save_data()

                print()
                print("===================================================")
                print("               PAYMENT RECEIPT                     ")
                print("===================================================")
                print(f"Payment ID      : {payment_id}")
                print(f"Invoice ID      : {invoice_id}")
                print(f"Transaction ID  : {transaction_id}")
                print(f"Amount Paid     : Rs. {amount_paid:.2f}")
                print(f"Payment Method  : {payment_method}")
                print(f"Payment Status  : {payment_status}")
                print(f"Payment Date    : {payment_date}")
                print("===================================================")
                print("          Payment completed successfully!          ")
                print("===================================================")

                return

        if not found_invoice:
            print("Invoice ID does not exist!")

    except ValueError:
        print("Invalid Input!")


def payment_history():

    print("=======================================================")
    print("                    PAYMENT HISTORY                    ")
    print("=======================================================")
    print()

    if len(payments) == 0:
        print("No payment records available!")
        return

    print("-" * 90)
    print(f"{'Payment ID':<12}{'Invoice ID':<12}{'Method':<18}{'Status':<12}{'Amount':<15}")
    print("-" * 90)

    for item in payments:

        amount = 0

        for invoice in invoices:
            if invoice.invoice_id == item.invoice_id:
                amount = invoice.grand_total
                break

        print(
            f"{item.payment_id:<12}"
            f"{item.invoice_id:<12}"
            f"{item.payment_method:<18}"
            f"{item.payment_status:<12}"
            f"Rs. {amount:<10.2f}"
        )

    print("-" * 90)

    print()
    print("===================================================")
    print("               PAYMENT DETAILS                     ")
    print("===================================================")

    for item in payments:

        amount = 0

        for invoice in invoices:
            if invoice.invoice_id == item.invoice_id:
                amount = invoice.grand_total
                break

        print(f"Payment ID     : {item.payment_id}")
        print(f"Invoice ID     : {item.invoice_id}")
        print(f"Amount Paid    : Rs. {amount:.2f}")
        print(f"Payment Method : {item.payment_method}")
        print(f"Payment Status : {item.payment_status}")
        print(f"Payment Date   : {item.payment_date}")
        print("-" * 50)

def search_payment():

    print("===================================================")
    print("                 SEARCH PAYMENT                    ")
    print("===================================================")
    print()

    if len(payments) == 0:
        print("No payment records available!")
        return

    try:

        payment_id = int(input("Enter Payment ID: "))

        if payment_id <= 0:
            print("Payment ID must be greater than zero!")
            return

        found = False

        for item in payments:

            if item.payment_id == payment_id:

                found = True

                print()
                print("===================================================")
                print("                PAYMENT DETAILS                    ")
                print("===================================================")
                print(f"Payment ID     : {item.payment_id}")
                print(f"Invoice ID     : {item.invoice_id}")
                print(f"Payment Method : {item.payment_method}")
                print(f"Payment Status : {item.payment_status}")
                print(f"Payment Date   : {item.payment_date}")

                for invoice in invoices:
                    if invoice.invoice_id == item.invoice_id:
                        print(f"Amount Paid    : Rs. {invoice.grand_total:.2f}")
                        break

                print("===================================================")
                break

        if not found:
            print("Payment ID does not exist!")

    except ValueError:
        print("Invalid Input!")