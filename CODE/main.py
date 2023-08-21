#THIS IS THE MAIN CODE
import mysql.connector as sc
import function as m
from tabulate import tabulate


#THIS BLOCK CHECK THE CONNECTION OF PYTHON WITH MYSQL and Check Database
mycon = sc.connect(host="localhost", user="root", passwd= m.C1())
cursor = mycon.cursor()

if mycon.is_connected() != True:
    print("CONNECTION ERROR")
 
#1. create database if not exist
cursor.execute("create database if not exists rudrastores")
cursor.execute("Use Rudrastores")


#3. Create management - inventory table if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory(
    Itemcode VARCHAR(10) PRIMARY KEY,
    itemName VARCHAR(40) NOT NULL,
    Category VARCHAR(40) NOT NULL,
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
               PIN int NOT NULL default '9999',
               AC_Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')


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
intro = m.l2()
print(intro)

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
        m.l1()
        while True:
            print(" ⛥ MAIN MENU ")
            print("   1. VIEW INFORMATION \n   2. ADD NEW ITEM  \n   3. Update Item details  \n   4. Remove Item  \n   5. QUIT PROGRAM")
            print()
            B1 = m.input_int("CHOOSE TASK - (1/2/3/4/5) : ")
            if B1 == 1:
                m.l6()
                while True:
                    print(" ⛥ MAIN MENU ")
                    print("   • VIEW INFORMATION  : ")
                    print("      1. Display All Item Details  \n      2. View Inventory  \n      3. Browse Categories \n      4. Customer Insights  \n      5. Return to MAIN MENU " ) 
                    print()
                    VI = m.input_int(" CHOOSE TASK (1/2/3/4/5) : ")
                    
                    
                    if VI == 1:
                        m.l1()
                        B,data,r = m.view_all()
                        if B == True:                                                                                                
                            print("ITEMS AVAILABLE :---")
                            headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
                            print(tabulate(data, headers=headers, tablefmt="grid"))
                            print("The Total Number of Items Available :",r)
                        elif B == False:
                            print("NO ITEMS AVAILABLE ! ! !")
                        m.l8()
                    
                    
                    elif VI == 2:
                        m.l1()
                        while True:
                            print(" ⛥ MAIN MENU ")
                            print("  • View Informantion  ")
                            print("     • View Inventory  :")
                            print("         1. Display Full Stock \n         2. Search for Item \n         3. Back to View Information Menu ")
                            print()
                            V12  = m.input_int(" CHOOSE TASK (1/2/3) : ")
                            if V12 == 1:
                                m.l1()
                                #VIEW ALL ITEMS WITH STOCK
                                view,data,r = m.view_stock()
                                if view == True:
                                    print("ITEMS AVAILABLE :---")
                                    headers = ["Itemcode","Item Name", "Stock Left"]
                                    print(tabulate(data, headers=headers, tablefmt='grid'))
                                    print("The Total Number of Items Available :",r)
                                else:
                                    m.l1()
                                    print("NO ITEMS AVAILABLE")
                                m.l10()
                            elif V12 == 2:
                                m.l1()
                                #VIEW PARTICULAR ITEM STOCK
                                viewpart,data,r = m.part_stock()
                                if viewpart == True:
                                    m.l1()
                                    print("SIMILAR RECORD FOUND :---")
                                    headers = ["Item Code","Item Name", "Stock Left"]
                                    print(tabulate(data, headers=headers, tablefmt='grid'))
                                    print("The Total Number of Items Available :",r)
                                    

                                elif viewpart == False:
                                    m.l1()
                                    print("ITEM DOESN'T EXIST ! ! !")
                                m.l10()
                            elif V12 == 3:
                                m.l8()
                                break
                            else:
                                m.l1()
                                print("Invalid Option. Please choose from given options only ! ! ! ")
                                m.l1()
                            
                    
                    
                    elif VI == 3:
                        m.l1()
                        while True:
                            print(" ⛥ MAIN MENU ")
                            print("  • View Informantion  ")
                            print("     • BROWSE CATEGORIES  : ")
                            print("         1. View All Categories \n         2. Browse Items by Category \n         3. Back to View Information Menu ")
                            print()
                            BM = m.input_int(" CHOOSE TASK (1/2/3) : ")
                            if BM == 1:
                                m.l1()
                                cat,data,r = m.category()
                                if cat == True:
                                    print("ALL CATEGORIES AVAILABLE : ")
                                    headers = [" CATEGORIES "]
                                    print(tabulate(data, headers=headers, tablefmt='grid'))
                                    print("The Total Number of CATEGORIES Available :",r)
                                elif cat == False:
                                    print("NO CATEGORIES AVAIALBLE ! ! !")
                                print()
                                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                print('Returning To Browse Categories MENU. . . . . ')
                                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                print()

                            elif BM == 2:
                                while True:
                                    m.l1()
                                    category = input("Please enter Category to view all Items listed in it :  ")
                                    view_citems,data,r = m.view_citems(category)
                                    if view_citems == True:
                                        print()
                                        print("SIMILAR RECORD FOUND : --- ")
                                        headers = ["Item Code","Items Available ","Price","Category"]
                                        print(tabulate(data, headers=headers, tablefmt='grid'))
                                        print("TOTAL ITEMS IN CATEGORY : ", r)
                                    elif view_citems == False:
                                        m.l1()
                                        print("NO ITEMS AVAILABLE ! ! !")
                                    m.l1()
                                    choice = m.input_alpha("DO WANT TO VIEW ITEMS IN MORE CATEGORY  (YES/NO) ? ? ? : ")
                                    if choice.upper() == 'YES':
                                        continue
                                    else:
                                        print()
                                        print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                        print('Returning To Browse Categories MENU. . . . . ')
                                        print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                        print()
                                        break
                            elif BM == 3:
                                m.l8()
                                break
                            else:
                                m.l1()
                                print("Invalid Option. Please choose from given options only ! ! ! ")
                                m.l1()
                    
                    
                    elif VI == 4:   
                        m.l1()
                        while True:
                            print(" ⛥ MAIN MENU ")
                            print("  • View Informantion  ")
                            print("     • CUSTOMER INSIGNTS  : ")
                            print("         1. View Customer Info \n         2. View Customer Orders \n         3. Read Customer Reviews  \n         4. Return to View Information Menu  ")
                            print()
                            CI = m.input_int(" CHOOSE TASK (1/2/3/4) : ")
                            if CI == 1:
                                m.l1()
                                view_cust,data,r = m.view_customerinfo()
                                if view_cust == True:
                                    print("DETAILS OF ALL CUSTOMERS : --- ")
                                    headers = ["Username","NAME","AGE","MOBILENO","ADDRESS"]
                                    print(tabulate(data, headers=headers, tablefmt='grid'))
                                    print(" TOTAL CUSTOMERS INFORMATION AVAILABLE : ",r)
                                    mycon.commit()
                                elif view_cust == False:
                                    print("NO INFORMATION AVAILABLE") 
                                m.l11()
                            

                            elif CI == 2:
                                m.l1()
                                orders,data,r = m.view_corders()
                                if orders == True:
                                    print("DETAILS OF ALL ORDERS --->")
                                    headers = ["Username", "Orderid", "Name", "Itemname", "PRICE", "QUANTITY", "TotalPrice", "Orderdate", "DELIVERY_DATE"]
                                    print(tabulate(data, headers=headers, tablefmt="grid"))
                                    print(" TOTAL NUMBER OF ORDERS AVAILABLE : ",r)
                                elif orders == False:
                                    print("NO ORDERS AVAILABLE ")
                                m.l11()
                            
                            elif CI == 3:
                                m.l1()
                                review,data,r = m.view_creview()
                                if review == True:
                                    print("DETAILS OF CUSTOMER REVIEWS --->")
                                    headers = ["USERNAME","RATING in '✮'","SUGGESTION_GIVEN","DATE_SUBMISSION"]
                                    print(tabulate(data, headers=headers, tablefmt="grid"))
                                    print("TOTAL NUMBER OF REVIEWS RECEIVED = ",r)
                                
                                elif review == False:
                                    print(" NO RECORD FOUND ! ! ! ")
                                m.l11()

                            elif CI == 4:
                                m.l8()
                                break
                            else:
                                m.l1()
                                print("Invalid Option. Please choose from given options only ! ! ! ")
                                m.l1()
                    
                    elif VI == 5:
                        m.l4()
                        break
                    else:
                        m.l1()
                        print("Invalid Option. Please choose from given options only ! ! ! ")
                        m.l1()

            elif B1 == 2:
                m.l1()
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
                        m.l4()
                        break
            
            elif B1 == 3:
                m.l1()
                while True:   
                    print(" ⛥ MAIN MENU ")
                    print("  • WHAT DO YOU WANT TO UPDATE??")
                    print("      1. ITEM NAME")
                    print("      2. CATEGORY")
                    print("      3. PRICE")
                    print("      4. ExpiryDate - (YYYYMMDD)")
                    print("      5. Stock")
                    print("      6. Return to View Information Menu ")
                    print()
                    V1 = m.input_int("UPDATE - (1/2/3/4/5) : ")
                    print()
                    if V1 == 6:
                        m.l4()
                        break
                    elif V1 in (1,2,3,4,5):
                        update = m.updateitem(V1)
                        if update != True:
                            m.l1()
                            print(update)
                            m.l1()
                    else:
                        m.l1()
                        print("Invalid Option. Please choose from given options only ! ! ! ")
                        m.l1()
                    
                    g2 = input("Do you want to update more items? (YES  /  NO): ")
                    if g2.lower() != 'yes':
                        m.l4()
                        break
                
            elif B1 == 4:
                m.l1()
                while True:
                    print(" ⛥ MAIN MENU ")
                    print(" • DELETE ITEM USING:-   \n     1. Item Name. \n     2. Item Code  \n     3. Return to MAIN MENU ")
                    G1 = m.input_int("USING (1/2)  : - ")
                    if G1 == 1:
                        m.l1()
                        delete,H1 = m.deleteitem_name()
                        if delete == True:
                                print("ITEM NAME '"+H1+"' deleted successfully.")
                                print()
                                ch2 = input("Do you want to delete more items? (YES  /  NO): ")
                                if ch2.lower() not in {'yes'}:
                                    m.l4()
                                    break
                            
                        else:
                            print()
                            print(delete)
                            print()
                        
                    elif G1 == 2:
                        print()
                        delete_code,H2 = m.deleteitem_code()
                        if delete_code == True:
                                print()
                                print("ITEM NAME '"+H2+"' deleted successfully.")
                                print()
                                
                                ch2 = input("Do you want to delete more items? (YES  /  NO): ")
                                if ch2.lower() not in {'yes'}:
                                    m.l4()
                                    break
                        else:
                            print()
                            print(delete_code)
                            print()
                    elif G1 == 3:
                        m.l4()
                        break
                    
                    else:
                        m.l1()
                        print("Invalid Option. Please choose from given options only ! ! ! ")
                        m.l1()
            
            elif B1 == 5:
                print()
                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                print('CLOSING THE PROGRAM . . . . . ')
                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                break
            else:
                m.l1()
                print("Invalid Option. Please choose from given options only ! ! ! ")
                m.l1()

    elif S2 == False:
        print("CONTACT THE ADMINISTRATOR.")
        print()


elif S1 == 2:
        while True:
            m.l1()
            print("MAIN MENU ")
            print("   1. SIGNUP. \n   2. LOGIN.")
            L1 = m.input_int(" PLEASE SELECT (1/2): - ")
            m.l1()

            if L1 == 1:
                OP = m.signup()
                if OP == True:
                    #IF LOGIN ACCOUNT SUCCESSFULLY CREATED 
                    print()
                    print("ACCOUNT SUCCESSFULLY CREATED..")
                    print()
                    print("PLEASE LOGIN AGAIN . . . ")

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
                        print("TASKS AVAILABLE NOW : \n   1. PLACE ORDER  \n   2. VIEW ORDER DETAILS \n   3. QUIT PROGRAM ")
                        L9 = m.input_int("CHOOSE TASK (1/2) : ")
                        if L9 == 1:
                            while True:
                                m.l1()
                                orders = m.acceptorders(U1,U2)
                                
                                if orders == True:
                                    m.l1()
                                    print("ORDER SUCCESFULL . . .")
                                    m.l1()
                                
                                elif orders == False:
                                    m.l1()
                                    print("INCORRECT PIN ENTERED , ORDER CANCELLED ! ! !")
                                    m.l1()
                                    
                                elif orders == None:
                                    m.l4()
                                    break           
                                    
                                else:
                                    print(orders)
                                    m.l1()
                                FG = m.input_alpha("DO YOU WANT TO ORDER MORE ITEMS (YES  /  NO) : ")
                                m.l1()
                                if FG.lower() not in {'yes'}:
                                    m.l4()
                                    break

                        
                        elif L9 == 2:
                            m.l1()
                            v_orders,data,r = m.view_selforders(U1)
                            if v_orders == True:
                                headers = ["Username", "Orderid", "Name", "Itemname", "PRICE", "QUANTITY", "TotalPrice", "Orderdate", "DELIVERY_DATE"]
                                #print(tabulate(data, headers=headers, tablefmt="grid"))
                                table = tabulate(data, headers=headers, tablefmt="grid")
                                print(table)
                                print("TOTAL ORDERS : ",r)
                            else:
                                print(v_orders)
                            m.l4()

                        elif L9 == 3:  
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
                                print()
                                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                print('CLOSING THE PROGRAM . . . . . ')
                                print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
                                break
                        
                    


                elif login_status == False:
                    print("PLEASE TRY AGAIN LATER.")
                    break
                break
            else:
                m.l1()
                print("Please Select from given options only ! ! ! ")
                m.l1()
                
        

else:
    m.l1()
    print("Invalid Option. Please choose from given options only ! ! ! ")
    m.l1() 



mycon.commit()
mycon.close
print()
outro = m.l3()
print(outro)