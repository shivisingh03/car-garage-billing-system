from database import Database
from datetime import date

class Billing:
    def __init__(self):
        self.db=Database()
        self.con=self.db.connect()
        self.cursor = self.con.cursor()
    def generate_bill(self):
        vehicle_id=int(input("Enter Vehicle ID: "))
        print("\n-----Services-----")
        print("1. Car Wash ₹500")
        print("2. Oil Change ₹1000")
        print("3. Brake Service ₹1500")
        print("4. Wheel Alignment ₹800")
        print("5. Full Service ₹5000")
        choice=int(input("\nSelect Services"))
        if choice ==1:
            service="Car Wash"
            amount=500
        elif choice==2:
            service= "Oil Change"
            amount=1000
        elif choice==3:
            service= "Brake Service"
            amount=1500
        elif choice==4:
            service= "Wheel Alignment"
            amount=800
        elif choice==5:
            service= "Full Service"
            amount=5000
        else:
            print("Invalid Choice")
            return
        sql="""
        INSERT INTO bills(vehicle_id, service,amount,bill_date)
        VALUES(%s,%s,%s)
        """
        value=(vehicle_id,service, amount,date.today())
        self.cursor.execute(sql,value)
        self.con.commit()
        print("\n----BILL----")
        print("Service:", service)
        print("Amount:₹", amount)
        print("Date",date.today())
        print("============")
        print("Bill generated seccessfully")
    def view_bills(self):
        sql="""
        SELECT
        bills.bill_id,
        customers.customer_name, 
        vehicles.vehicle_number,
        bills.service,
        bills.amount,
        bills.bill_date
        FROM customers
        INNER JOIN vehicles
        ON customers.customer_id=vehicles.customer_id
        INNER JOIN bills
        ON vehicles.vehicle_id=bills.vehicle_id;"""
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print("\n=======bills===========")
        for row in data:
            print(row)