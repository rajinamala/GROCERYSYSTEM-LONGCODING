import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='grocery_shop'
)
mycursor = mydb.cursor()
print(mycursor)
class customerDetails:
    def __init__(self,customerName, password):
        self.customerName = customerName
        self.customerPassword = password

    def isAlreadyExistingUser(self):
        mycursor.execute('select customer_id, customer_name, Password from customer_details where customer_name like %s',
                         (self.customerName,))
        details = mycursor.fetchall()
        if details[0][1] == self.customerName and details[0][2] == self.customerPassword:
            return details[0][0]

class groceryItems:
    def listofGroceryItems(self):
        Gcategory = str(input("enter preferred category"))
        mycursor.execute("select grocery_id, grocery_name, price, offers from grocery_items where category like %s", (Gcategory,))
        items = mycursor.fetchall()
        for row in items:
           # print(row)
            print('item name:', row[1], ' ', 'amount:', row[2], ' ', 'offer:', row[3])

class addItemsToCart:
     def __init__(self, customer_id):
         self.customer_id = customer_id

     def addingItemsToCart(self):
         while True:
             isWhetherToAddItem = str(input('Do you want to add item to your cart? If so,Please enter Y -> yes or N ->np'))
             if isWhetherToAddItem == 'Y':
                 item_name = str(input('enter your item name'))
                 quantity = int(input('enter your item quantity'))

                 mycursor.execute('select grocery_id,price from grocery_items where grocery_name like %s',(item_name,))
                 fetchedDetails = mycursor.fetchall()

                 toMultiplyPriceWithQuantity = fetchedDetails[0][1]*quantity

                 mycursor.execute("insert into cart_details(customer_id,grocery_id,quantity,total_cost)values(%s,%s,%s,%s)",
                                 (self.customer_id,fetchedDetails[0][0],quantity,toMultiplyPriceWithQuantity,))
                 mydb.commit()
                 print("successfully added items to your cart")
             else :
                 break

class order:
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def orderTheItems(self):
        print('do you want to order the items?')
        isWhetherToOrderTheItems = str(input('Y -> yes or N-> no'))
        if isWhetherToOrderTheItems == 'Y':
            mycursor.execute('SELECT cart_details.cart_id, grocery_items.grocery_name,cart_details.quantity,cart_details.total_cost,grocery_items.offers FROM cart_details INNER JOIN grocery_items ON cart_details.grocery_id = grocery_items.grocery_id WHERE customer_id like %s',(self.customer_id,))
            cartItems = mycursor.fetchall()
            for i in range(len(cartItems)):
                rowItems = cartItems[i]
                print('cart item:',i+1,'.','item_name:', rowItems[1],'quantity:',rowItems[2],'total_cost:',rowItems[3],'offer_applied:', rowItems[2]*rowItems[4])
            while True:
                cartItemOption = int(input('Enter the option you like to order or type 0 to exit from order'))
                if cartItemOption != 0:
                    cartId = cartItems[cartItemOption - 1][0]
                    paymentMethod = str(input('what is your mode of payment, 1. online or 2.COD'))
                    now = datetime.now()
                    formattedDate = now.strftime('%Y-%m-%d %H:%M:%S')
                    if paymentMethod == 'online':
                        accountHolderName = str(input('enter account holder name'))
                        accountNumber = str(input('enter your account number'))
                        cvv = int(input('enter valid account cvv'))
                        address  = str(input('enter delivery address'))
                        mycursor.execute(
                            "INSERT INTO payment_details(cart_id,payment_method,account_holdername,account_no,cvv,timeofpayment,address)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                            (cartId, paymentMethod, accountHolderName,accountNumber, cvv,formattedDate,address,))
                        mydb.commit()
                    else:
                        address = str(input('enter your address to deliver'))
                        mycursor.execute(
                            "INSERT INTO payment_details(cart_id,payment_method,account_holdername,account_no,cvv,timeofpayment,address)Values(%s,%s,%s,%s,%s,%s,%s)",
                            (cartId, paymentMethod, accountHolderName, accountNumber, cvv, formattedDate, formattedDate,address,))
                        mydb.commit()
                else:
                    break
if __name__ == '__main__':
    customerName = str(input("ENTER YOUR NAME"))
    password = str(input("ENTER YOUR PASSWORD"))
    customerValidation = customerDetails('Raji','R123')
    existingUserId = customerValidation.isAlreadyExistingUser()
    if existingUserId:
        GroceryItemsList = groceryItems()
        GroceryItemsList.listofGroceryItems()

        cartItems = addItemsToCart(existingUserId)
        cartItems.addingItemsToCart()

        orderItems = order(existingUserId)
        orderItems.orderTheItems()

    else:
        phoneNumber = int(input("ENTER YOUR PHONE NUMBER"))
        email = str(input("ENTER YOUR EMAIL ID"))
        location = str(input("ENTER YOUR LOCATION"));
        mycursor.execute("INSERT INTO customer_details(customer_name,phone_number,email,Password,location)VALUES(%s,%s,%s,%s,%s,%s)",
                         (customerName,phoneNumber,email,password,location,))
        mydb.commit()
