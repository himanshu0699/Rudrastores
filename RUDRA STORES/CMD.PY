#THIS ONE EXECUTES PERSONALIZED QUERY;
import mysql.connector as sc
#import function as m
mycon = sc.connect(host='localhost', user = 'root', passwd = 'user',database = 'rudrastores')

if mycon.is_connected() == 'False':
    print("CONNECTION ERROR")

cursor = mycon.cursor()
while True:
    Q1 = input("ENTER PERSONAIZED QUERY TO EXECUTE :-  ")
    cursor.execute(Q1)
    row = cursor.rowcount
    if row > 0:
        data = cursor.fetchall()
        for x in data:
            print(x)
        m.l1()    
        ch = input("DO YOU WANT TO EXECUTE MORE QUERIES - (Y/N)  :-  ")
        m.l1()
        if ch.lower() != 'y':
            break
    else:
        print("SUCCESS")
print()
print("QUERY SUCCESSFULLY EXECUTED ! ! ! ")
m.l5()