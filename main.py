from restaurant import (menu_management, customer_management, employee_management, table_management, order_management, 
                        billing_management, payment_management,load_data)

from reports import (all_reports, statistics,)

load_data()

while True:
    
    print("==========================================================================")
    print("                       RESTAURANT MANAGEMENT SYSTEM                       ")
    print("==========================================================================")
    print()
    print("Welcome to the Restaurant Management System!")
    print()
    print("1. Menu Management")
    print("2. Customer Management")
    print("3. Employee Management")
    print("4. Table Management")
    print("5. Order Management")
    print("6. Billing & Invoices")
    print("7. Payment Management")
    print("8. Show Reports")
    print("9. Show Statistics")
    print("10. Exit")
    print("==========================================================================")
    try:
        choice = int(input("Enter an option (1-10): "))
        if choice == 1:
            menu_management()
            
        elif choice == 2:
            customer_management()
           
        elif choice == 3:
            employee_management()
          
        elif choice == 4:
            table_management()
            
        elif choice == 5:
            order_management()
            
        elif choice == 6:
            billing_management()
           
        elif choice == 7:
            payment_management()
            
        elif choice == 8:
            all_reports()
         
        elif choice == 9:
            statistics()
          
        elif choice == 10:
            print("Thank you for using the Restaurant Management System...") 
            print("Goodbye!") 
            print()
            break
        else:
            print("Please enter a number between 1 and 10.")
            
        
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")

