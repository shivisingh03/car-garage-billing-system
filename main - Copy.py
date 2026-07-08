from customer import Customer
from billing import Billing
customer = Customer()
bill=Billing()
while True:
    print("\n" + "=" *40)
    print(" CAR GARAGE BILLING SYSTEM")
    print("=" *40)
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Vehicle")
    print("4. View Vehicles")
    print("5. Generate Bill")
    print("6. View Bills")
    print("7. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        customer.add_customer()
    elif choice == 2:
        customer.view_customers()
    elif choice == 3:
        customer.add_vehicle()
    elif choice == 4:
        customer.view_vehicle()
    elif choice == 5:
        bill.generate_bill()
    elif choice == 6:
        bill.view_bills()
    elif choice == 7:
        print("Thank You...")
        break
    else:
        print("Invalid Choice")
