#THIS CODE CONTAINS FUNCTIONS.
import datetime as dt
import mysql.connector as sc
import random as rm
from tabulate import tabulate

print()
password = input("PLEASE ENTER YOUR MYSQL PASSWORD : ")

def C1():
    return password

mycon = sc.connect(host="localhost", user="root", passwd= password)
cursor = mycon.cursor()
if mycon.is_connected() != True:
    print("CONNECTION ERROR")
def tablestructure():
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
                AC_Created Date );''')


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

tablestructure()
#FUNCTIONS START FROM HERE....


#FUNCTIONS START FROM HERE....

#1. This function improves security.
def lock_system(prompt):
    # Function code goes here
    
    passwd = password
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        user_input = input(prompt)

        if user_input == passwd:
            print()
            print("ACCESS GRANTED ! ! !")
            # Continue with the rest of your code here
            # ...
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Incorrect password. {remaining_attempts} attempt(s) left. Try again.")
                print()
            else:
                print()
                print("LOCKED!!.")
                # Code break actions here
                # ...
                return False

    return False
#END OF 1,lock_system


#2.THIS FUNCTION IS USED SHOW ALL ITEMS AVAILABLE
def view_all():
    cursor.execute("SELECT * FROM inventory;")
    data = cursor.fetchall()
    r = cursor.rowcount
    if r > 0: 
        return True,data,r
    else:
        return False,data,r
 #END OF 2,view_all


#3. THIS FUNCTIONS IS USED TO SHOW ALL STOCK AVAILABLE 
def view_stock():
    cursor.execute("select Itemcode,ItemName,Stockleft from inventory ;")
    data = cursor.fetchall()
    r = len(data)
    if r > 0:
        return True,data,r
    else:
        return False,data,r
#END OF 3,view_stock


#4. THIS FUNCTION IS USED SHOW STOCK OF PARTICULAR ITEM 
def part_stock():
    C1 = input("ENTER ITEM NAME: ")
    print()
    cursor.execute("SELECT itemcode,ItemName, Stockleft FROM inventory WHERE itemname like '%" + C1 + "%'")
    data = cursor.fetchall()
    r = cursor.rowcount
    if r > 0:
        return True,data,r
    else:
        return False,data,r
#END OF 4,part_stock


#5. THIS FUNCTION IS USED TO VIEW ALL CATEGORY 
def category():
    cursor.execute("SELECT DISTINCT CATEGORY FROM INVENTORY;")
    data = cursor.fetchall()
    r = len(data)  # Calculate the number of rows
    if r > 0:
        return True,data,r
    else:
        return False,data,r
#END OF 5,category


#6. THIS FUNCTION IS USED SHOW ALL THE ITEMS AVAILABLE IN PARTICULAR CATEGORY
def view_citems(X1):
    cursor.execute("SELECT itemcode,itemNAME,price,Category FROM Inventory WHERE category like '%"+X1+"%';")
    data = cursor.fetchall()
    r = len(data)  # Calculate the number of rows
    if r > 0:
        return True,data,r
    else:
        return False,data,r
    

#7. THIS FUNCTION IS USED SHOWS TAX PRICE FOR ALL THE ITEMS


#8. THIS FUNCTION IS USED VIEW PROFIT REPORT FOR THE FIRM



#9. THIS FUNCTIONS IS USED SHOWS ALL CUSTOMER DETAILS
def view_customerinfo():
    cursor.execute("select * from customerinformation;")
    data = cursor.fetchall()
    r = len(data)
    if r > 0 :
        return True,data,r
    else:
        return False,data,r
#END OF 9,view_customerinfo


#10. THIS FUNCTIONS IS USED SHOWS ALL CUSTOMER ORDERS
def view_corders():
    cursor.execute("SELECT * FROM CUSTOMERORDERS ")
    data = cursor.fetchall()
    r = len(data)
    if r > 0:
        return True,data,r
    else:
        return False,data,r
#END OF 10,view_corders


#11. THIS FUNCTIONS SHOWS ALL CUSTOMER REVIEWS B6
def view_creview():
    cursor.execute("SELECT * FROM CREVIEWs ")
    data = cursor.fetchall()
    r = len(data)
    if r > 0:
        return True,data,r
    else:
        return False,data,r
#END OF 11,view_creview


#MODITY FUNCTIONS...

#12.THIS FUNCTIONS IS USED TO ENTER ITEM IN THE SERVER
def additem():
    print("ADDING ITEM IN SERVER ---")
    print()
    M0 = input_ain("ENTER ITEM CODE IN 'B0XXX' : ").upper()
    M1 = input("ITEM NAME: ").upper()
    M2 = input("CATEGORY: ").upper()
    M3 = input_int("PRICE: ")
    M4 = input_int("EXPIRY DATE IN 'YYYYMMDD': ")
    M5 = input_int("QUANTITY PURCHASED: ")
    Q2 = "INSERT INTO inventory VALUES ('" + M0 + "','" + M1 + "','" + M2 + "'," + str(M3) + "," + str(M4) + ","+str(M5)+");"
    cursor.execute(Q2)
    mycon.commit()
    r = cursor.rowcount
    if r > 0:
        return True
    else:
        return False
#END OF 12,additem

#13,14.THIS FUNCTION IS USED TO DELETE ITEM FROM THE SERVER
#USING ITEMNAME
def deleteitem_name():
    H1 = input("ENTER ITEM NAME : ").upper()
    cursor.execute("SELECT * FROM inventory WHERE itemname = '"+H1+"' ;")
    data = cursor.fetchall()
    r = len(data)
    print()
    if r > 0:
        print("RECORD FOUND : --->")
        headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print()
        print("CONFIRM TO DELETE THE RECORD")
        J1 = input_alpha("TYPE 'DEL' TO CONFIRM  : - ")
        if J1.upper() == 'DEL':
            cursor.execute("DELETE FROM inventory WHERE itemname = '"+H1+"';")
            mycon.commit()
            return True,H1
        else:
            l1()
            return "UNABLE TO CONFIRM THE DELETION",H1

    else:
        return "ITEM CODE NOT FOUND ! ! !",H1
#PARTIAL CODE END 

#14. USING ITEMCODE
def deleteitem_code():
    H2 = input_ain("ENTER ITEM CODE : ")
    cursor.execute("SELECT * FROM Inventory WHERE itemcode ='"+str(H2)+"';")
    data = cursor.fetchall()
    r = cursor.rowcount
    if r > 0:
        print()
        print("RECORD FOUND : --->")
        headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print()
        K1 = input_alpha("TYPE 'DEL' TO CONFIRM  THE DELETION :  ")
        if K1.upper() == 'DEL':
            cursor.execute("DELETE FROM inventory WHERE itemcode = '"+H2+"';")
            mycon.commit()
            return True,H2
        else:
            l1()
            return "UNABLE TO CONFIRM THE DELETION",H2
    else:
        return "ITEM CODE NOT FOUND  ! ! !",H2
    
#END OF 13,14,deleteitem_code 


#15.THIS FUNCTION IS USED TO UPDATE ITEM DETAILS
def updateitem(V1):
    if V1 == 1:
        K9 = 'ITEMNAME' 
    elif V1 == 2:
        K9 = 'CATEGORY'
    elif V1 == 3:
        K9 = 'PRICE'
    elif V1 == 4:
        K9 = 'ExpiryDate'
    elif V1 == 5:
        K9 = 'StockLeft'
    L0 = [1,2,3,4,5]


    if V1 in L0:
        new = input_ain("ENTER NEW VALUE : ")
        print()
        K10 = input_ain(f"ENTER THE ITEM CODE TO UPDATE {K9} : ")
        K10 = K10.upper()
        print()
        cursor.execute("SELECT * FROM inventory WHERE itemcode = '"+str(K10)+"';")
        data = cursor.fetchall()
        r = len(data)
        
        if r > 0:
            print("RECORD FOUND --->")
            headers = ["ITEMCODE","ITEMNAME","CATEGORY","PRICE","EXPIRY DATE","STOCKLEFT"]
            print(tabulate(data, headers=headers, tablefmt='grid'))
            print()
        
            J6 = input_alpha("TYPE 'UPD' TO CONFIRM UPDATION : ")
            if J6.upper() == 'UPD':
            
                if V1 in [1, 2, 4]:
                    cursor.execute("UPDATE inventory SET " + K9 + " = '" + new + "' WHERE itemcode = '" + K10 + "'")
                    l1()
                    print("DETAILS UPDATED SUCCESSFULLY . . .")
                    mycon.commit()
                    
                    cursor.execute("SELECT * FROM INVENTORY  WHERE ITEMCODE = '" + K10 + "'")
                    data = cursor.fetchall()
                    headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
                    print(tabulate(data, headers=headers, tablefmt="grid"))
                    l1()
                    return True

                elif V1 in [3, 5]:
                    cursor.execute("UPDATE inventory SET " + K9 + " = " + new + " WHERE itemcode = '" + K10 + "'")
                    l1()
                    print("DETAILS UPDATED SUCCESSFULLY . . .")
                    mycon.commit()


                    cursor.execute("SELECT * FROM INVENTORY  WHERE ITEMCODE = '" + K10 + "'")
                    data = cursor.fetchall()
                    headers = ['ITEMCODE', 'ITEMNAME', 'CATEGORY', 'PRICE', 'EXPIRYDATE', 'STOCKLEFT']
                    print(tabulate(data, headers=headers, tablefmt="grid"))
                    l1()
                    return True
                
            else:
                return ("CONFIRMATION FAILED ! ! ! ")
        else:
            return ("ITEM CODE NOT FOUND ! ! !")
    else:
        return ("COLUMN NOT AVAILABLE ! ! !")
#END OF 15,updateitem


#CUSTOMER UI FUNCTIONS....
#16. This functions creates account for the customer
def signup():
    V1 = 'USERNAME'
    V2 = 'NAME'
    V3 = 'AGE'
    V4 = 'MOBILE NUMEBR'
    V5 = 'ADDRESS'
    V6 = 'PIN '   

    print("PLEASE ENTER THE FOLLOWING DETAILS ('*' = COMPULSORY!! ):")
    N1 = input_ain(f"{V1} (NO SPECIAL CHARACTERS): ").lower()
    N2 = input_alpha(f"{V2} : ")
    N3 = input_int(f"{V3} : ")
    N4 = input_int(f"{V4} : ")
    N5 = input(f"{V5} : ")
    N6 = input_int(f"{V6} default(0000) : ")
    
    print()
    print("\nPLEASE VERIFY DETAILS :---")
    print()
    print(f"1. {V1} : '{N1}'")
    print(f"2. {V2} : '{N2}'")
    print(f"3. {V3} : '{N3}'")
    print(f"4. {V4} : '{N4}'")
    print(f"5. {V5} : '{N5}'")
    print(f"6. {V6} : '{N6}'")
    
    P1 = input_alpha("PLEASE ENTER 'YES' TO CONFIRM SIGNUP : ")
    while P1.lower() != 'yes':
        print()
        print("PLEASE CHOOSE WHAT DO YOU WANT CHANGE  :")
        AG  = input_int("1/2/3/4/5/6 : ")
        print()

        if AG == 1:
            N1 = input_ain(f"{V1} (ONLY SPECIAL CHARACTERS): ").lower()
        elif AG == 2:
            N2 = input_alpha(f"{V2} : ")
        elif AG == 3:
            N3 = input_int(f"{V3} : ")
        elif AG == 4:
            N4 = input_int(f"{V4} : ")
        elif AG == 5:
            N5 = input(f"{V5} : ")
        elif AG == 6:
            N6 = input_int(f"{V6} default(0000) : ")

        print()    
        print("\nPLEASE VERIFY DETAILS :---")
        print(f"USERNAME : '{N1}'")
        print(f"NAME: '{N2}'")
        print(f"AGE: '{N3}'")
        print(f"MOBILE NUMBER: '{N4}'")
        print(f"ADDRESS: '{N5}'")
        print(f"PIN: '{N6}'")
        print()
            
        P1 = input_alpha("PLEASE ENTER 'YES' TO CONFIRM SIGNUP : ")
    
    Y1 = f"INSERT INTO customerinformation VALUES ('{str(N1)}', '{str(N2)}', {N3}, {N4}, '{str(N5)}');"
    Y2 = f"INSERT INTO clogininfo VALUES ('{str(N1)}', '{str(N6)}', CURRENT_TIMESTAMP);"
    cursor.execute(Y1)
    cursor.execute(Y2)
    mycon.commit()
    r = cursor.rowcount
    if r > 0:
        return True
    else:
        return False

mycon.commit()
#END OF 17,SIGNUP


#18. This function check the user for login
def login():
    MAX_RETRIES = 3
    while True:
        for attempt in range(MAX_RETRIES):
            U1 = input_ain("ENTER USERNAME (NO SPECIAL CHARACTERS ALLOWED): ").lower()
            U2 = input_int("ENTER PIN: ")

            cursor.execute(f"SELECT username, pin FROM clogininfo WHERE username = '{U1}';")
            data = cursor.fetchall()

            if len(data) > 0:
                for row in data:
                    if U1 == row[0] and U2 == row[1]:
                        return True, U1, U2
            
            print()
            print("INVALID USERNAME OR PIN ! ! !")


            if attempt < MAX_RETRIES - 1:
                choice = input_alpha("Do you want to retry? (Y/N): ")
                print()
                if choice.lower() == "y":
                    continue
                else:
                    print("OKAY ! ! !")
                    return False, None, None

            print()
            print("MAXIMUM ATTEMPTS REACHED ! ! ! ")
            print("LOGGED OUT DUE TO SECURITY REASON ! ! !")
            print()
            return False, None, None
#END OF18,LOGIN

#19.THIS FUNCTION IS USED TO ACCEPT ORDERS BY CUSTOMER AFTER LOGIN
def acceptorders(U1,U2):
    print("How would you like to order: \n1. SEARCH ITEM. \n2. VIEW ALL ITEMS(SUGGESTED) \n3. Return to MAIN MENU \n4. MORE COMING SOON  ! ! ! ")
    J7 = input_int("USING (1/2) : ")
    
    #EXTRACTING DATA:
    #Username
    cursor.execute("SELECT username from clogininfo where username = '"+U1+"'")
    UN = cursor.fetchall()
    
    #NAME 
    cursor.execute("SELECT name from customerinformation where username = '"+U1+"'")
    NM = cursor.fetchall()
    name = NM[0][0] if NM else None

 
    #GENERATE ORDER ID
    F1 = rm.randint(1111, 9999)

    #STORE CURRENT DATE 
    td = dt.date.today().strftime("%Y%m%d")
 
    #STORE DELIVERY DATE
    dd = (dt.date.today() + dt.timedelta(days=7)).strftime("%Y%m%d")

    if J7 == 1:
        l1()
        G9 = input_ain("PLEASE ENTER ITEM : ").upper()
        print()
        cursor.execute("SELECT itemname from inventory where itemname = '"+G9+"' ")
        item = cursor.fetchall()
        r = len(item)
        
        if r > 0:
            cursor.execute("select price from inventory where itemname = '"+G9+"'")
            price = cursor.fetchall()
            OH = price[0][0] if price else None
            PR = OH
            
            print("ITEM NAME : - '"+G9+"'")
            print("PRICE : - '"+str(PR)+"'")

            Q = input_int("ENTER QUANTITY : - ") 
            TP = Q*PR
            
            print("TOTAL PRICE OF ORDER : - '"+str(TP)+"'")
            l1()
            
            print("CONFIRM DETAILS OF ORDER : -  ")
            print("USERNAME : '"+U1+"'")
            print("CUSTOMER NAME : '"+name+"'")
            print("ITEMNAME : '"+str(G9)+"'")
            print("PRICE per/item : '"+str(PR)+"'")
            print("QUANTITY : '"+str(Q)+"'")
            print("TOTAL PRICE : '"+str(TP)+"'")

            CN = input_int("ENTER YOUR PIN TO CONFIRM THE ORDER  : ")
            if CN == U2:
                                                                                                                                                                                                            
                cursor.execute("INSERT INTO customerorders VALUES ('" + str(U1) + "', " + str(F1) + ", '" + str(name) + "', '" + str(G9) + "', " + str(PR) + ", " + str(Q) + ", " + str(TP) + ", '" + str(td) + "','" + str(dd) + "');")                                                                                   
                cursor.execute("UPDATE INVENTORY SET STOCKLEFT = STOCKLEFT - "+str(Q)+";")
                mycon.commit()                                                                                                                                                                                                                                  
                return True
                

            elif CN != U2:
                return False
        
        else:
            return "ITEM NOT FOUND ! ! !"

    
    elif J7 == 2:

        cursor.execute("SELECT ITEMNAME, PRICE,EXPIRYDATE FROM INVENTORY")
        data = cursor.fetchall()
        l1()

        print("ITEMS AVAILABLE --->")
        headers = ["Item Name", "Price","EXPIRY DATE"]
        #table_data = [[index, item[0], item[1]] for index, item in enumerate(data, start=1)]
        table = tabulate(data, headers=headers, tablefmt="grid")
        print(table)

        H0 = input_ain("ENTER ITEMNAME  : ").upper()
        print()
        cursor.execute("select ITEMNAME from inventory where itemname = '"+H0+"'")
        item = cursor.fetchall()
        r = cursor.rowcount
        if r > 0 :
            cursor.execute("SELECT PRICE FROM INVENTORY WHERE ITEMNAME = '"+H0+"';")
            price = cursor.fetchall()
            OH = price[0][0] if price else None
            PR = OH

            print("ITEM NAME : - '"+H0+"'")
            print("PRICE : - '"+str(PR)+"'")
                        
            Q = input_int("ENTER QUANTITY : - ")

            TP = Q*PR
            print("TOTAL PRICE OF ORDER : - '"+str(TP)+"'")
            l1()
            

            print("CONFIRM DETAILS OF ORDER : -  ")
            print("USERNAME : '"+U1+"'")
            print("CUSTOMER NAME : '"+name+"'")
            print("ITEMNAME : '"+str(H0).upper()+"'")
            print("PRICE per/item : '"+str(PR)+"'")
            print("QUANTITY : '"+str(Q)+"'")
            print("TOTAL PRICE : '"+str(TP)+"'")
            print()

            CN = input_int("ENTER YOUR PIN TO CONFIRM THE ORDER  : ")
            if CN == U2:                                                                                                                                                           
                cursor.execute("INSERT INTO customerorders VALUES ('" + str(U1) + "', " + str(F1) + ", '" + str(name) + "', '" + str(H0) + "', " + str(PR) + ", " + str(Q) + ", " + str(TP) + ", '" + str(td) + "','" + str(dd) + "');")                                                                                   
                cursor.execute("UPDATE INVENTORY SET STOCKLEFT = STOCKLEFT - "+str(Q)+";")
                mycon.commit()                
                return True

            elif CN != U2:
                return False                                                                              

        else:
            return "ITEM NOT FOUND ! ! !"
            
    elif J7 == 3:
        return None
    else:
        return "COMING SOON ! ! !"
#END OF 19,acceptorders

#20.THIS  FUNCTION IS USED TO DISPLAY CUSTOMER's OWN ORDERS
def view_selforders(U1):
    cursor.execute("select * from customerorders where username = '"+str(U1)+"';")
    data = cursor.fetchall()
    r = len(data)
    if r > 0:
        return True,data,r 
    else:
        return "NO ORDERS AVAILABLE ! ! !",data,r
#END OF 21,view_selforders


#21. THIS FUNCTION TO ACCEPT CUSTOMER REVIEWS AND SUGGESTONS
def customer_reviews(U1):
    T1 = "✮ ✮ ✮ ✮ ✮ ~ AWESOME"
    T2 = "✮ ✮ ✮ ✮ ~ GOOD "
    T3 = "✮ ✮ ✮ ~ AVERAGE"
    T4 = "✮ ✮ ~ NEEDS IMPROVEMENT"
    T5 = "✮ ~ WORST"
    print(f"5. {T1} \n4. {T2} \n3. {T3} \n2. {T4} \n1. {T5}") 
    print()
    
    US = input_int("PLEASE ENTER ACCORDINGLY ~ (5/4/3/2/1) : ")
    UR = input("ANY SUGGESTIONS ??? : ")

    cursor.execute("INSERT INTO CREVIEWS VALUES ('" + U1 + "','"+str(US)+"','" + str(UR) + "', CURRENT_TIMESTAMP)")
    mycon.commit()
    r = cursor.rowcount
    if r > 0:
        print()
        return True,"THANK YOU FOR GIVING US YOUR PRECIOUS TIME ... "
    else:
        return False,None
#END OF 22,customer_reviews


#Miscellaneous functions
#23. This function checks the input as integer
def input_int(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")
            print()
#END OF 23,input_int


#24. This function checks the input as ALPHABETS
def input_alpha(prompt):
    while True:
        try:
            text = input(prompt)
            if not text.replace(" ", "").isalpha():
                raise ValueError
            return text
        except ValueError:
            print()
            print("Invalid input. Please enter alphabetic characters only.")
            print()
#END OF 24,input_alpha
            

#25. This function checks the input as ALPHANUMERic only
def input_ain(prompt):
    while True:
        try:
            text = input(prompt)
            if not text.replace(" ", "").isalnum():
                raise ValueError
            return text
        except ValueError:
            print()
            print("Invalid input. Please enter alphanumeric characters only (no spaces).")
            print()
#END OF 25,input_ain

#PRESENTATION FUNCTIONS..
#This function is used to print for better view
def l1():
    line = '- - - - - - - - - - - - - - - - - - - - - - - - -  '
    print()
    print(line)
    print()

#This function is used to print for better view
def l2():
    print()
    return '''╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                              WELCOME                                                       ║
║                                                                TO                                                          ║
║                                                          RUDRA  STORES                                                     ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'''
    
#This function is used to print for better view
def l3():
    print()
    mycon.commit()
    mycon.close()
    return '''╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                              THANK YOU                                                     ║
║                                                  @COPYRIGHT OWNER:- Rudra Stores                                           ║
║                                                  ALL RIGHTS RESERVED SINCE  -  2023                                        ║
║                                                  ***MADE WITH   ❤️   IN UDAIPUR***                                          ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'''


#This function is used to print for better view
def l4():
     print()
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print('Returning To Main Menu . . . . . ')
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print()

#This function is used to print for better view
def l8():
     print()
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print('Returning To VIEW INFORMATION MENU . . . . . ')
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print()

#This function is used to print for better view
def l5():
    line = ">" * 45
    print(line)

#This function is used to print for better view
def l6():
    line = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  '*2
    print()
    print(line)
    print()

 
#This function is used to print for better view
def l9():
    line = ">" * 140
    print()
    print(line)
    print()

def l10():
     print()
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print('Returning To VIEW INVENTORY MENU . . . . . ')
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print()


def l11():
     print()
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print('Returning To CUSTOMER INSIGHTS MENU . . . . . ')
     print('- - - - - - - - - - - - - - - - - - - - - - - - -  ')
     print()

