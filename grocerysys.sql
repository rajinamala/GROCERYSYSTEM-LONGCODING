CREATE  DATABASE GROCERY_SHOP;
SHOW DATABASES;
USE grocery_shop;

CREATE TABLE customer_details(customer_id INT AUTO_INCREMENT primary key NOT NULL, customer_name varchar(45), phone_number int, email varchar(45), location varchar(50));
INSERT INTO customer_details(customer_name,phone_number,email,location)VALUES('Raji',123456,'rajinamala12@gmail.com','Nellore');
SELECT * FROM customer_details;
CREATE TABLE grocery_items(grocery_id INT AUTO_INCREMENT primary key NOT NULL, grocery_name varchar(45), price int, offers int, category varchar(45), total_quantity_available varchar(50), is_best_seller varchar(50));
INSERT INTO grocery_items(grocery_name,price,offers, category, total_quantity_available, is_best_seller) VALUES('idly_Rice', 200, 2,'rice', 100, 'yes'),('poni_rice', 200, 3, 'rice', 100, 'yes'),('phenol', 70, 1,'bathroom_accessories', 200, 'no'),('harpic', 90, 1, 'bathroom_accessories', 300, 'no'),('dry_peas', 50, 3, 'pulses', 200, 'yes');
SELECT * FROM grocery_items;
CREATE TABLE cart_details(
  cart_id INT NULL AUTO_INCREMENT,
  customer_id INT ,
  grocery_id INT ,
  quantity INT NULL,
  total_cost INT NULL,
  PRIMARY KEY (cart_id));
  INSERT INTO cart_details(customer_id,grocery_id,quantity,total_cost)VALUES(1,2,5,1000);
  SELECT * FROM cart_details;
  CREATE TABLE payment_details(
  payment_id INT NOT NULL AUTO_INCREMENT,
  cart_id INT ,
  payment_method VARCHAR(45) ,
  account_holdername VARCHAR(45),
  account_no INT,
  cvv INT ,
  timeofpayment DATETIME,
  PRIMARY KEY (payment_id));
  INSERT INTO payment_details(cart_id,payment_method,account_holdername,account_no,cvv,timeofpayment)VALUES(1,'DEBIT','RAJINAMALA',234567,143,'2021-07-16 23:20:00');
  SELECT * FROM payment_details;
CREATE TABLE delivery_details(
  delivery_id INT NOT NULL,
  payment_id INT NULL,
  dperson_id INT NULL,
  delivery_status VARCHAR(45) NULL,
  delivery_time DATETIME NULL,
  feedback VARCHAR(45) NULL,
  cancel TINYINT NULL,
  refund TINYINT NULL);
  INSERT INTO delivery_details(delivery_id,payment_id,dperson_id,delivery_status,delivery_time)VALUES(001,1,2,'PACKING','2021-08-21 12:30:21');
  SELECT * FROM delivery_details;
CREATE TABLE delivery_person_details(
  dperson_id INT NOT NULL,
  dperson_name VARCHAR(45) NOT NULL,
  dperson_contact INT NOT NULL,
  UNIQUE INDEX dperson_id_UNIQUE (dperson_id ASC));
  INSERT INTO delivery_person_details(dperson_id,dperson_name,dperson_contact)VALUES(1,'raju',685749),(2,'Rahul',65789);
SELECT * FROM delivery_person_details;

