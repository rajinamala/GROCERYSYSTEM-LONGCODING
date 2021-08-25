CREATE  DATABASE GROCERY_SHOP;
SHOW DATABASES;
USE grocery_shop;

CREATE TABLE customer_details(customer_id INT AUTO_INCREMENT primary key NOT NULL, customer_name varchar(45), Password varchar(45), phone_number int, email varchar(45), location varchar(50));
INSERT INTO customer_details(customer_name,Password,phone_number,email,location)VALUES('Raji','R123',123456,'rajinamala12@gmail.com','Nellore');
SELECT * FROM customer_details;
CREATE TABLE grocery_items(grocery_id INT AUTO_INCREMENT primary key NOT NULL, grocery_name varchar(45), price int, offers int, category varchar(45), total_quantity_available varchar(50), is_best_seller varchar(50));
INSERT INTO grocery_items(grocery_name,price,offers, category, total_quantity_available, is_best_seller) VALUES('idly_Rice', 200, 2,'rice', 100, 'yes'),('poni_rice', 200, 3, 'rice', 100, 'yes'),('phenol', 70, 1,'bathroom_accessories', 200, 'no'),('harpic', 90, 1, 'bathroom_accessories', 300, 'no'),('dry_peas', 50, 3, 'pulses', 200, 'yes');
SELECT * FROM grocery_items;
CREATE TABLE cart_details(
  cart_id INT auto_increment,
  customer_id INT ,
  grocery_id INT ,
  quantity INT NULL,
  total_cost INT NULL,
  PRIMARY KEY (cart_id));
SELECT * FROM cart_details;
CREATE TABLE payment_details(
  payment_id INT NOT NULL AUTO_INCREMENT,
  cart_id INT ,
  payment_method VARCHAR(45) ,
  account_holdername VARCHAR(45),
  account_no VARCHAR(45),
  cvv INT ,
  address VARCHAR(45),
  timeofpayment DATETIME,
  PRIMARY KEY (payment_id));
  SELECT * FROM payment_details;

