CREATE DATABASE garage_db1;
USE garage_db1;
CREATE TABLE customers
(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(100) NOT NULL,
mobile VARCHAR (15) NOT NULL
);

CREATE TABLE vehicles
(
vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
vehicle_number VARCHAR(20) UNIQUE,
vehicle_name VARCHAR(50),

FOREIGN KEY(customer_id)
REFERENCES customers(customer_id)
ON DELETE CASCADE
);
CREATE TABLE bills
(
bill_id INT AUTO_INCREMENT PRIMARY KEY,
vehicle_id INT,
service VARCHAR(50),
amount DECIMAL(10,2),
bill_date DATE,
FOREIGN KEY (vehicle_id)
REFERENCES vehicles(vehicle_id)
ON DELETE CASCADE
);
INSERT INTO customers(customer_name, mobile)
VALUES
("Rahul", "9876543210");
INSERT INTO vehicles(customer_id, vehicle_number, vehicle_name)
VALUES
(1,"UP32AB1234","Swift");
INSERT INTO bills(vehicle_id, service, amount, bill_date)
VALUES
(1,"Car Wash", 500, CURDATE());
SELECT 
customers.customer_name, 
vehicles.vehicle_number,
bills.service,
bills.amount,
bills.bill_date
FROM customers
INNER JOIN vehicles
ON customers.customer_id=vehicles.customer_id
INNER JOIN bills
ON vehicles.vehicle_id=bills.vehicle_id;

