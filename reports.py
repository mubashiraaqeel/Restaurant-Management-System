import restaurant
from datetime import datetime

# ==========================
# Reports Management
# ==========================

def all_reports():
    
    while True:
    
        print("=========================================")
        print("                 REPORTS                 ")
        print("=========================================")
        print()
        print("1. Daily Sales Report")
        print("2. Monthly Sales Report")
        print("3. Customer Report")
        print("4. Employee Report")
        print("5. Payment Report")
        print("6. Back to Main Menu")
        print("=================================================")
        
        try:
            choice = int(input("Enter an option (1-6): "))
            
            if choice == 1:
                daily_sales_report()
                print()
            elif choice == 2:
                monthly_sales_report()
                print()
            elif choice == 3:
                customer_report()
                print()
            elif choice == 4:
                employee_report()
                print()
            elif choice == 5:
                payment_report()
                print()
            elif choice == 6:
                print("Back to the Main Menu!")
                print()
                break
            else:
                print("Please enter a number between 1 and 6.")
                
        except ValueError:
            print("Please enter a number between 1 - 6.") 


def daily_sales_report():

    print("=================================================")
    print("              DAILY SALES REPORT                 ")
    print("=================================================")
    print()

    today = datetime.now().strftime("%Y-%m-%d")

    total_sales = 0
    total_orders = 0

    found = False

    for order in restaurant.orders:

        if order.order_time.startswith(today):

            found = True
            total_orders += 1
            total_sales += order.total_amount

            print(f"Order ID      : {order.order_id}")
            print(f"Customer ID   : {order.customer_id}")

            if order.table_number != 0:
                print(f"Table Number  : {order.table_number}")

            print(f"Status        : {order.order_status}")
            print(f"Amount        : Rs. {order.total_amount:.2f}")
            print(f"Time          : {order.order_time}")
            print("-" * 50)

    if not found:
        print("No sales found for today.")
        return

    print("=" * 50)
    print(f"Total Orders : {total_orders}")
    print(f"Total Sales  : Rs. {total_sales:.2f}")
    print("=" * 50)


def monthly_sales_report():
    
    print("=================================================")
    print("              MONTHLY SALES REPORT               ")
    print("=================================================")
    print()

    if len(restaurant.orders) == 0:
        print("No orders available!")
        return

    month = input("Enter Month (MM): ").strip()
    year = input("Enter Year (YYYY): ").strip()

    if not month.isdigit() or not year.isdigit():
        print("Invalid Month or Year!")
        return

    total_sales = 0
    total_orders = 0

    for item in restaurant.orders:

        if item.order_status == "Completed":

            order_date = datetime.strptime(
                item.order_time,
                "%Y-%m-%d %H:%M:%S"
            )

            if (
                order_date.month == int(month)
                and order_date.year == int(year)
            ):

                total_sales += item.total_amount
                total_orders += 1

    print("=================================================")
    print(f"Month            : {month}")
    print(f"Year             : {year}")
    print(f"Completed Orders : {total_orders}")
    print(f"Total Sales      : Rs. {total_sales:.2f}")
    print("=================================================")


def customer_report():

    print("=================================================")
    print("               CUSTOMER REPORT                   ")
    print("=================================================")
    print()

    if len(restaurant.customers) == 0:
        print("No customers available!")
        return

    dine_in = 0
    take_away = 0
    delivery = 0

    for item in restaurant.customers:

        print(f"Customer ID   : {item.customer_id}")
        print(f"Name          : {item.customer_name}")
        print(f"Phone Number  : {item.phone_number}")
        print(f"Email         : {item.email}")
        print(f"Gender        : {item.gender}")
        print(f"Visit Type    : {item.visit_type}")
        print("-" * 50)

        if item.visit_type == "Dine In":
            dine_in += 1

        elif item.visit_type == "Take Away":
            take_away += 1

        elif item.visit_type == "Delivery":
            delivery += 1

    print("=================================================")
    print(f"Total Customers : {len(restaurant.customers)}")
    print(f"Dine In         : {dine_in}")
    print(f"Take Away       : {take_away}")
    print(f"Delivery        : {delivery}")
    print("=================================================")


def employee_report():

    print("=================================================")
    print("               EMPLOYEE REPORT                   ")
    print("=================================================")
    print()

    if len(restaurant.employees) == 0:
        print("No employees available!")
        return

    manager = 0
    chef = 0
    waiter = 0
    cashier = 0
    other = 0

    for item in restaurant.employees:

        print(f"Employee ID   : {item.employee_id}")
        print(f"Name          : {item.employee_name}")
        print(f"Phone Number  : {item.phone_number}")
        print(f"Position      : {item.position}")
        print(f"Email         : {item.email}")
        print(f"Salary        : Rs. {item.salary:.2f}")
        print(f"Shift         : {item.shift}")
        print("-" * 50)

        if item.position == "Manager":
            manager += 1

        elif item.position == "Chef":
            chef += 1

        elif item.position == "Waiter":
            waiter += 1

        elif item.position == "Cashier":
            cashier += 1

        else:
            other += 1

    print("=================================================")
    print(f"Total Employees : {len(restaurant.employees)}")
    print(f"Managers        : {manager}")
    print(f"Chefs           : {chef}")
    print(f"Waiters         : {waiter}")
    print(f"Cashiers        : {cashier}")
    print(f"Others          : {other}")
    print("=================================================")


def payment_report():
    
    print("=================================================")
    print("                PAYMENT REPORT                   ")
    print("=================================================")
    print()

    if len(restaurant.payments) == 0:
        print("No payment records available!")
        return

    total_payments = 0
    total_amount = 0

    cash = 0
    card = 0
    online = 0

    for item in restaurant.payments:

        amount = 0

        for invoice in restaurant.invoices:
            if invoice.invoice_id == item.invoice_id:
                amount = invoice.grand_total
                break

        print(f"Payment ID     : {item.payment_id}")
        print(f"Invoice ID     : {item.invoice_id}")
        print(f"Payment Method : {item.payment_method}")
        print(f"Payment Status : {item.payment_status}")
        print(f"Amount         : Rs. {amount:.2f}")
        print(f"Payment Date   : {item.payment_date}")
        print("-" * 50)

        total_payments += 1
        total_amount += amount

        if item.payment_method == "Cash":
            cash += 1

        elif item.payment_method == "Card":
            card += 1

        elif item.payment_method == "Online":
            online += 1

    print("=================================================")
    print(f"Total Payments : {total_payments}")
    print(f"Total Amount   : Rs. {total_amount:.2f}")
    print(f"Cash Payments  : {cash}")
    print(f"Card Payments  : {card}")
    print(f"Online Payments: {online}")
    print("=================================================")



# ==========================
# Statistics
# ==========================



def statistics():

    print("=================================================")
    print("                 STATISTICS                      ")
    print("=================================================")
    print()

    total_customers = len(restaurant.customers)
    total_employees = len(restaurant.employees)
    total_menu_items = len(restaurant.menu)
    total_orders = len(restaurant.orders)
    total_invoices = len(restaurant.invoices)
    total_payments = len(restaurant.payments)
    total_tables = len(restaurant.tables)

    available_tables = 0
    reserved_tables = 0

    for item in restaurant.tables:
        if item.status == "Available":
            available_tables += 1
        elif item.status == "Reserved":
            reserved_tables += 1

    available_food = 0
    unavailable_food = 0

    for item in restaurant.menu:
        if item.availability:
            available_food += 1
        else:
            unavailable_food += 1

    pending_orders = 0
    completed_orders = 0
    cancelled_orders = 0

    for item in restaurant.orders:
        if item.order_status == "Pending":
            pending_orders += 1
        elif item.order_status == "Completed":
            completed_orders += 1
        elif item.order_status == "Cancelled":
            cancelled_orders += 1

    total_sales = 0

    for item in restaurant.payments:
        total_sales += item.amount_paid

    print(f"Total Customers      : {total_customers}")
    print(f"Total Employees      : {total_employees}")
    print(f"Total Menu Items     : {total_menu_items}")
    print(f"Available Food Items : {available_food}")
    print(f"Unavailable Food     : {unavailable_food}")
    print()
    print(f"Total Tables         : {total_tables}")
    print(f"Available Tables     : {available_tables}")
    print(f"Reserved Tables      : {reserved_tables}")
    print()
    print(f"Total Orders         : {total_orders}")
    print(f"Pending Orders       : {pending_orders}")
    print(f"Completed Orders     : {completed_orders}")
    print(f"Cancelled Orders     : {cancelled_orders}")
    print()
    print(f"Total Invoices       : {total_invoices}")
    print(f"Total Payments       : {total_payments}")
    print(f"Total Sales          : Rs. {total_sales:.2f}")
    print("=================================================")