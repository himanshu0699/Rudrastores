#THIS IS THE MAIN CODE
import mysql.connector as sc
import function as m
from tabulate import tabulate



#THIS BLOCK CHECK THE CONNECTION OF PYTHON WITH MYSQL and Check Database
mycon = sc.connect(host="localhost", user="root", passwd= m.C1() )
cursor = mycon.cursor()

if mycon.is_connected() != True:
    print("CONNECTION ERROR")
 
#1. create database if not exist
cursor.execute("create database if not exists rudrastores")
cursor.execute("Use Rudrastores")


#3. Create management - inventory table if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory(
    Itemcode VARCHAR(10) PRIMARY KEY,
    itemName VARCHAR(25) NOT NULL,
    Category VARCHAR(15) NOT NULL,
    Price FLOAT(10,3) NOT NULL,
    ExpiryDate DATE NOT NULL DEFAULT '2024-03-31', 
    StockLeft DOUBLE(10,3) NOT NULL
    )''')


#4. Create customer - customerinformation table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS customerinformation(
    Username VARCHAR(15) PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Age INT(11) NOT NULL,
    MobileNo BIGINT(20) NOT NULL,
    Address VARCHAR(50)
);
''')

#5. Create management - customerinfo table if not exists
cursor.execute('''create table if not exists clogininfo (
               USERNAME varchar(15) primary key ,
               PIN int NOT NULL default '0000',
               AC_Creadted TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')


#6. Create table management - customerorders  #ADDRESS VARCHAR(20) NOT NULL,,Delivery DATE NOT NULL
cursor.execute('''CREATE TABLE IF NOT EXISTS customerorders(
    Username VARCHAR(15) NOT NULL,
    Orderid INT PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Itemname VARCHAR(20) NOT NULL,
    PRICE INT NOT NULL,
    QUANTITY INT NOT NULL,
    TotalPrice INT NOT NULL, 
    Orderdate DATE NOT NULL,
    DELIVERY_DATE DATE NOT NULL
);
''')

#7. create REVIEW TABLE - customer reviews
cursor.execute('''CREATE TABLE IF NOT EXISTS creviews (
    USERNAME VARCHAR(15) NOT NULL,
    RATING int NOT NULL,
    SUGGESTIONS_GIVEN VARCHAR(200) NOT NULL,
    SUBMISSION_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')


mycon.commit()

print()
m.l9()
print('''                                                                 WELCOME 
                                                                   TO 
                                                              RUDRA  STORES''')
m.l9()

#USER INTERFACE SELECTION
print()
print("YOU ARE  ??  \n1. MANAGEMENT  \n2. CUSTOMER ")
S1 = m.input_int("PLEASE CONFIRM  (1/2) : " )
if S1 == 1:#ENTERS MANAGEMENT OPERATION
    print()
    print(" HINT : - SQL PASSWORD")
    S2 = m.lock_system("ENTER PASSWORD TO ACCESS DATABASE :- ")#CHECK PASSWORD FUNCTION
   # m.l1()
    if S2 == True:
        while True:
            m.l1()
            print("PLEASE SELECT ACTION :  ")
            print("1. VIEW DATABASE. \n2. MODIFY DATABASE.")#SELECT THE OPERATION TO PERFORM
            
            A1 = m.input_int("CHOOSE ACTION - (1/2) : ")
            m.l1()
            if A1 == 1:
                print("AVAILABLE TASKS : \n1. VIEW ALL ITEMS DETAILS .\n2. VIEW STOCK. \n3. VIEW CATEGORY. \n4. View All Customer Information. \n5. VIEW ALL CUSTOMER ORDERS. \n6. VIEW CUSTOMER REVIEWS.  \n7. TO EXIT THE MENU..  \n8. OTHER OPTIONS COMING SOON.. ")  # B1

                B1 = m.input_int("CHOOSE TASK - (1/2/3/4/5/6/7) : ")
                #B1 : 1 - VIEW ALL ITEMS IN THE SERVER 
                if B1 == 1:
                    m.l1()
                    B,data,r = m.view_all()
                    if B == True:                                                                                                
                        print("ITEMS AVAILABLE :---")
                        headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                        print("The Total Number of Items Available :",r)
                        m.l1()
                    elif B == False:
                        print("NO ITEMS AVAILABLE ! ! !")
                        m.l1()

                #B1 : 2 - VIEW STOCK
                elif B1 == 2:
                    m.l1()
                    print("AVAILABLE TASKS : \n1. VIEW FULL STOCK. \n2. SEARCH PARTICULAR ITEM. \n3.TO EXIT THE MENU.. ")
                    B2 = m.input_int("CHOOSE TASK - (1/2) : ")
                    print()
                    if B2 == 1:
                        #VIEW ALL ITEMS WITH STOCK
                        view,data,r = m.view_stock()
                        if view == True:
                            m.l1()
                            print("ITEMS AVAILABLE :---")
                            headers = ["Itemcode","Item Name", "Stock Left"]
                            print(tabulate(data, headers=headers, tablefmt='grid'))
                            print("The Total Number of Items Available :",r)
                            m.l1()
                        else:
                            m.l1()
                            print("NO ITEMS AVAILABLE")
                            m.l1()
                        mycon.commit()
                            


                    elif B2 == 2:
                        #VIEW PARTICULAR ITEM STOCK
                        viewpart,data,r = m.part_stock()
                        if viewpart == True:
                            m.l1()
                            print("SIMILAR RECORD FOUND :---")
                            headers = ["Item Code","Item Name", "Stock Left"]
                            print(tabulate(data, headers=headers, tablefmt='grid'))
                            print("The Total Number of Items Available :",r)
                            m.l1()

                        elif viewpart == False:
                            m.l1()
                            print("ITEM DOESN'T EXIST ! ! !")
                            m.l1()
                        mycon.commit()

                    elif B2 == 3:
                        break


                    #TO PREVENT CRASH IF NOT CHOSE CORRECT OPTION    
                    elif B2 not in['1','2','3']:
                        print()
                        print("CHOOSE CORRECT OPTION ! ! !")
                        print()
                        mycon.commit()
                
                #B1 : 3 - VIEW  CATEGORY
                elif B1 == 3:
                    # VIEW ALL CATEGORY
                    m.l1()
                    cat,data,r = m.category()
                    if cat == True:
                        headers = ["CATEGORIES AVAILABLE : - "]
                        print(tabulate(data, headers=headers, tablefmt='grid'))
                        print("The Total Number of CATEGORIES Available :",r)
                        m.l1()

                        X1 = m.input_alpha("DO YOU WANT TO SEE ALL ITEMS IN ANY CATEGORY?? (YES  /  NO): ")
                        while True:
                            # TO VIEW ITEMS IN ANY CATEGORY
                            
                            print()
                            if X1.lower() == 'yes':
                                Z1 = m.input_alpha("ENTER CATEGORY :  ").upper()
                                print()
                                cursor.execute("SELECT itemcode,itemNAME,price FROM Inventory WHERE category = '"+Z1+"';")
                                data = cursor.fetchall()
                                r = len(data)  # Calculate the number of rows
                                if r > 0:
                                    headers = ["Item Code","Items Available in '"+Z1+"'","Price"]
                                    print(tabulate(data, headers=headers, tablefmt='grid'))
                                    print("TOTAL ITEMS IN CATEGORY : ", r)
                                    m.l1()

                                    # TO CHECK ONE MORE?
                                    X1 = m.input_alpha("Do you want to see Items in another Category? (YES  /  NO): ")
                                    print()
                                    if X1.lower() == 'yes':
                                        continue
                                    elif X1.lower() != 'yes':
                                        break
                                        
                                else:
                                    print("NO RECORD FOUND ! ! ! ")
                                    print()
                                    break
                            else:
                                break
                    elif cat == False:
                        print("NO CATEGORY AVAILABLE ! ! !")
                        m.l1()

                #VIEW CUSTOMER INFORMATION
                elif B1 == 4:
                    m.l1()
                    view_cust,data,r = m.view_customerinfo()
                    if view_cust == True:
                        print("DETAILS OF ALL CUSTOMERS : --- ")
                        headers = ["Username","NAME","AGE","MOBILENO","ADDRESS"]
                        print(tabulate(data, headers=headers, tablefmt='grid'))
                        print(" TOTAL CUSTOMERS INFORMATION AVAILABLE : ",r)
                        m.l1()
                        mycon.commit()
                    elif view_cust == False:
                        print("NO INFORMATION AVAILABLE") 
                        m.l1()

                #VIEW CUSTOMERS ORDERS
                elif B1 == 5:
                    m.l1()
                    orders,data,r = m.view_corders()
                    if orders == True:
                        print()
                        print("DETAILS OF ALL ORDERS --->")
                        headers = ["Username", "Orderid", "Name", "Itemname", "PRICE", "QUANTITY", "TotalPrice", "Orderdate", "DELIVERY_DATE"]
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                        print(" TOTAL NUMBER OF ORDERS AVAILABLE : ",r)
                        m.l1()
                    elif orders == False:
                        print("NO ORDERS AVAILABLE ")
                        m.l1()
                        

                elif B1 == 6: 
                    m.l1()
                    review,data,r = m.view_creview()
                    if review == True:
                        print("DETAILS OF CUSTOMER REVIEWS --->")
                        headers = ["USERNAME","RATING in '✮'","SUGGESTION_GIVEN","DATE_SUBMISSION"]
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                        print("TOTAL NUMBER OF REVIEWS AVAILABLE = ",r)
                        m.l1()
                    
                    elif review == False:
                        print(" NO RECORD FOUND ! ! ! ")
                        m.l1()

                elif B1 == 7:
                    print()
                    print("OK ! ! ! ")
                    break
    
                else:
                    m.l1()
                    print("PLEASE SELECT APPROPRIATE OPTION ! ! ! !")
                    m.l1()
            
            #MODIFY IN DATABASE
            elif A1 == 2:
                print("CHOOSE TASK :- \n1.ADD ITEM TO SERVER.  \n2.DELETE ITEM FROM SERVER. \n3.UPDATE ITEM DETAILS. \n4.MORE COMING SOON...")
                D1 = m.input_int("TASK (1/2/3/4): ")
                m.l1()
                #ADDING ITEM
                if D1 == 1:
                    while True:
                        add = m.additem()
                        if add == True:
                            print()
                            print("DATABASE UPDATED! ! ! ")
                            print()
                        else:
                            print("ERROR OCCURED  ! ! ! ")
                            print()
                        ch2 = input("Do you want to add more items? (YES  /  NO): ")
                        print()
                        if ch2.lower() not in {'yes'}:
                            break
                
                #DELETING ITEM
                elif D1 == 2:
                    while True:
                        print("DELETE ITEM USING:-   \n 1.Item Name. \n 2.Item Code ")
                        G1 = m.input_int("USING (1/2)  : - ")
                        if G1 == 1:
                            m.l1()
                            delete,H1 = m.deleteitem_name()
                            if delete == True:
                                    print("ITEM NAME '"+H1+"' deleted successfully.")
                                    print()
                                    ch2 = input("Do you want to delete more items? (YES  /  NO): ")
                                    if ch2.lower() not in {'yes'}:
                                        break
                                
                            elif delete == False:
                                print("ITEM NOT FOUND ! ! !")
                                m.l1()
                                break
                            else:
                                print(delete)
                        elif G1 == 2:
                            print()
                            delete_code,H2 = m.deleteitem_code()
                            if delete_code == True:
                                    print()
                                    print("ITEM NAME '"+H2+"' deleted successfully.")
                                    print()
                                    
                                    ch2 = input("Do you want to delete more items? (YES  /  NO): ")
                                    if ch2.lower() not in {'yes'}:
                                        break
                            else:
                               print()
                               print(delete_code)
                               print()
                        else:
                            print()
                            print("PLEASE SELECT APPROPRIATE OPTION ! ! ! !")
                            break


                #UPDATING ITEM DETAILS
                elif D1 == 3:
                    while True:
                        print("WHAT DO YOU WANT TO UPDATE??")
                        print("1. ITEM NAME")
                        print("2. CATEGORY")
                        print("3. PRICE")
                        print("4. ExpiryDate - (YYYYMMDD)")
                        print("5. Stock")
                        
                        V1 = m.input_int("UPDATE - (1/2/3/4/5) : ")
                        print()
                        
                        update = m.updateitem(V1)
                        if update != True:
                           m.l1()
                           print(update)
                           m.l1()

                        g2 = input("Do you want to update more items? (YES  /  NO): ")
                        print()
                        if g2.lower() != 'yes':
                            break

                        
                else:
                    print("MORE OPTIONS WILL BE UPDATED SOON...")
                    m.l1()
            else:
                print("PLEASE SELECT APPROPRIATE OPTION ! ! ! !")
                m.l1()
            
            
            ch3 = input("Do you want execute more task? (YES  /  NO): ")
            print()
            if ch3.lower() not in {'yes'}:
                break
    
    elif S2 == False:
        print("CONTACT THE ADMINISTRATOR.")
        


elif S1 == 2:
        while True:
            m.l1()
            print("PLEASE SELECT : - ")
            print("1. SIGNUP. \n2. LOGIN.")
            L1 = m.input_int("CONFIRM (1/2): - ")
            m.l1()

            if L1 == 1:
                OP = m.signup()
                if OP == True:
                    #IF LOGIN ACCOUNT SUCCESSFULLY CREATED 
                    print()
                    print("ACCOUNT SUCCESSFULLY CREATED..")

                elif OP == False:
                    print()
                    print("ERROR OCCURED . . . \n PLEASE TRY AGAIN ! ! !")
                    print()
                    break

            #LOGIN CONDITION
            elif L1 == 2:
                login_status, U1, U2 = m.login()  # Call the login function without passing the cursor object

                if login_status == True:
                    m.l1()
                    print("LOGIN SUCCESSFUL...")
                    m.l1()

                    while True:
                        print("TASKS AVAILABLE NOW : \n1. PLACE ORDER  \n2. VIEW ORDER DETAILS. ")
                        L9 = m.input_int("CHOOSE TASK (1/2) : ")
                        m.l1()
                        if L9 == 1:
                            while True:
                                orders = m.acceptorders(U1,U2)
                                if orders == True:
                                    m.l1()
                                    print("ORDER SUCCESFULL . . .")
                                    m.l1()
                                
                                elif orders == None:
                                    print("INVALID PIN . ORDER NOT CONFIRMED ! ! !")
                                    break           
                                    
                                else:
                                    print(orders)
                                    m.l1()
                                FG = m.input_alpha("DO YOU WANT TO ORDER MORE ITEMS (YES  /  NO) : ")
                                print()
                                if FG.lower() not in {'yes'}:
                                    break
                        
                        elif L9 == 2:
                                v_orders,data,r = m.view_selforders(U1)
                                if v_orders == True:
                                    headers = ["Username", "Orderid", "Name", "Itemname", "PRICE", "QUANTITY", "TotalPrice", "Orderdate", "DELIVERY_DATE"]
                                    #print(tabulate(data, headers=headers, tablefmt="grid"))
                                    table = tabulate(data, headers=headers, tablefmt="grid")
                                    print(table)
                                    print("TOTAL ORDERS : ",r)
                                    m.l1()
                
                                else:
                                    print(v_orders)
                                    m.l1()
                                    
                        else:
                            print("PLEASE SELECT APPROPRIATE OPTION ! ! ! ")
                            print()
                        
                        print()
                        GP = input("Do you want execute more task? (YES  /  NO): ")
                        if GP.lower() != 'yes':
                            m.l1()
                            CH = m.input_alpha("We value your feedback. Could you kindly share your experience with us????  ~   (Y / N) : ")
                            if CH.lower() == 'y':
                                print()
                                review,msg = m.customer_reviews(U1)
                                if review == True:
                                    print(msg)
                                    m.l1()
                                break
                            else:
                                break
                    break


                elif login_status == False:
                    print("PLEASE TRY AGAIN LATER.")
                    break
                break
            else:
                m.l1()
                print("PLEASE CHOOSE APPROPRIATE OPTION!")
                m.l1()
                
        

else:
    m.l1()
    print("PLEASE CHOOSE APPROPRIATE OPTION ! ! !")
    m.l1()



mycon.commit() 
print()
m.l9()
print('''                                                                THANK YOU 
                                                       @COPYRIGHT OWNER:- Rudra Stores
                                                       ALL RIGHTS RESERVED SINCE  -  2023 
                                                       *** MADE WITH  ❤️️   IN UDAIPUR ***''')
m.l9()

