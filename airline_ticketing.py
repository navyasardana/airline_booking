import random
import pymysql as x
def dab():
    try:
            db=x.connect(host='localhost', user='root', password= 'navya123$', db="flight", auth_plugin_map={'caching_sha2_password': 'mysql_native_password'})
            cur=db.cursor()
            print("connected to sql")
            cur.execute("create database flight")
            cur.execute("use flight")
            db.commit
            print("database created")
    except:
            db=x.connect(host='localhost', user='root', password= 'navya123$', db="flight")
            cur=db.cursor()
            print("data base already exists")
        
   
    try:
        cur.execute('create table data(fname varchar(30), lname varchar(30), gender varchar(1),phone_no varchar(10) , email_no varchar(30), PNR varchar(30), dept_date date, arrival_date date, dept varchar (30), arrival varchar (30), status varchar(30))')
        print("Table -Data created")
    except:
        cur.execute("describe data")
        print('Table Data already exists')
    
        
    try:
        cur.execute("create table classes(Sno int, name varchar(10), price int)")
        cur.execute(' insert into classes values (1, "Economy", 10000)')
        cur.execute(' insert into classes values (2, "Business", 20000)')
        cur.execute(' insert into classes values (3, "Firstclass", 60000)')
        db.commit()
        print("Table- Class created")
    except:
        cur.execute("describe classes")
        print("Table- Class exists")
  

    try:
        cur.execute("create table menu (SNo int, item varchar(10), price int)")
        cur.execute("insert into menu values(1, 'Coffee', 100)")
        cur.execute("insert into menu values(2, 'Tea',100)")
        cur.execute("insert into menu values(3, 'Juice',100)")
        cur.execute("insert into menu values(4, 'Veg Sandwich',100)")
        cur.execute("insert into menu values(5, 'Non-Veg Sandwich',100)")
        cur.execute("insert into menu values(6, 'Veg Noodles',100)")
        cur.execute("insert into menu values(7, 'Non-veg Noodles',100)")
        cur.execute("insert into menu values(8, 'Soup with Salad',100)")
        cur.execute("insert into menu values(9, 'Chocolate Pastry',100)")
        cur.execute("insert into menu values(10, 'Vanilla Ice cream',100)")
        db.commit()
        print('Table- Menu Created')
    except:
        cur.execute("describe menu")
        print("Table- Menu exists")
        
    
    try:
        cur.execute("create table luggage(Sno int, weight varchar(10), price int)")
        cur.execute("insert into luggage values (1,'15Kg', 1000)")
        cur.execute("insert into luggage values (2,'20Kg', 2000)")
        cur.execute("insert into luggage values (3,'25Kg', 3000)")
        cur.execute("insert into luggage values (4,'30Kg', 4000)")
        cur.execute("insert into luggage values (5,'40Kg', 5000)")
        db.commit()
        print("Table- Luggage Created")
    except:
        cur.execute("desc luggage")
        print('Table - Luggage Exists')
    cur.close()
    db.close()

def char():
    ran = random.randint(100,999)
    r=str(ran)
    return r


def bill():
    amount=0
    db=x.connect(host='localhost', user='root', password= 'navya123$', db='flight')
    cur=db.cursor()
    cur.execute("select * from classes")
    f1=cur.fetchall()
    print("Choose the class you want to travel in here:- ")
    for w in range (len(f1)):
        for z in range(3):
            print(f1 [w][z], end= "-")
        print("\n")
    o1=int(input('enter your choice: '))
    q1="select price from classes where Sno= '%d'" %(o1)
    cur.execute(q1)
    r1=cur.fetchone()
    for g in  r1:
           amount+=int(g)
    print("_"*100)
    cur.execute("select * from luggage")    
    f2=cur.fetchall()
    print("choose the weight of your luggage")
    for c in range (len(f2)):
        for d in range(3):
            print(f2  [c][d], end= "-")
        print("\n")
    o2=int(input('enter your choice: '))
    p2=int(input("enter quantity"))
    q2="select price from luggage where Sno= '%d' "%(o2)
    cur.execute(q2)
    r2=cur.fetchone()
    for h in r2:
           amount+=int(g)*p2
    print('-'*100)
    z1=input("Would you like to order something from the menu? (Y/N): ").upper()
    if z1=="Y":
        cur.execute("select * from menu")
        f3=cur.fetchall()
        print(f3)
        '''for e in range (len(f3)):
            for f in range(len(f3)):
                print(f3 [e][f], end="-")
            print("\n")'''
        while True:
            o3 = int(input("Enter your choice:"))
            p3=int(input("Enter quantity: "))
            q3 = "select price from menu where SNo='%d' " % (o3)
            cur.execute(q3)
            r3 = cur.fetchone()
            for h in r3:
                amount+=int(h)*p3
            print('-'*100)
            z2= input ( "Anything else? (Y / N) : ").upper()
            if z2=="Y":
                continue
            else:
                break
    cur.close()
    db.close()
    return amount

def booking():
    db=x.connect(host='localhost', user='root', password= 'navya123$', db='flight')
    cur=db.cursor()
    print("Please enter the follwoing details for booking your ticket.")
    dept_date=input("Date of departure (YYYY/MM/DD) : ")
    arrival_date=input("Date of arrival (YYYY/MM/DD) : ")
    dept=input("Departure airport: ")
    arrival=input("Arrival airport: ")
    p=int(input("number of passengers:  "))
    for i in range (p):
        if p==1:
            print( "Passenger details: ")
        elif p>1:
            print("Passenger", i+1)
        fname=input("First name: ")
        lname=input("Last name: ")
        gender= input("Gender (M/F) ")
        phone_no=int(input("Phone number:  "))
        email_id=input("Email ID:  ")
        status="BOOKED"
        PNR=fname+char()
        q="insert into data values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(fname, lname, gender, phone_no, email_id ,PNR, dept_date, arrival_date, dept, arrival,  status)
        cur.execute(q)
        db.commit()
        print('PNR=' , PNR)
        result=bill()
        charge=random.randrange(20000,90000,1000)
        print('-'*100)
        print("Base Charge -",charge)
        print('-'*100)
        print("Surcharge -",result)
        print('-'*100)
        print("Total Amount -",result+charge)
        print("-"*100)
    print(" TICKET(S) BOOKED! ")
    cur.close()
    db.close()

def status():
    db=x.connect(host='localhost', user='root', password='navya123$',db='flight')
    cur=db.cursor()
    cur.execute("select * from data")
    r=cur.fetchall()
    while True:
        print("Choose a method to retrieve your ticket status: ")
        print("1. PNR")
        print("2. Email Id")
        print("3. Phone Number")
        print("4. Exit")
        z=int(input("Enter your choice: "))
        f=0
        if z==1:
            a=input("Enter your PNR number: ").upper()
            if a == PNR :
                result="Booked"
                f=f+1
                break
            else:
                f=0
            if f==1:
                print("Ticket Status -", result)
                print('='*100)
                break
            if f ==0:
                print("Not Booked")
                print('-'*100)
                break
        elif z ==2 :
            b=input("Enter your Email Id: ").upper()
            if a== email_id :
                result="Booked"
                f = f + 1
                break
            else:
                f = 0
            if f ==1 :
                print("Ticket Status -", result)
                print (' =' * 100 )
                break
            if f ==0:
                print("not booked")
                print('-' *100)
                break
        elif z ==3 :
            c=int(input("Enter your phone number: "))
            if c== phone_id:
                result="Booked"
                f=f+1
                break
            else:
                 f=0
            if f==1:
                print("Ticket Status -",result)
                print('=' *100)
                break
            if f==0:
                print("Not booked")
                print('-'*100)
                break
            elif z==4:
                break
            else:
                print("Please choose a valid option")
                print('- '*100)
    cur.close()
    db.close()
def cancel():
    db=x.connect(host='localhost', user='root', password='navya123$',db='flight')
    cur=db.cursor()
    cur.execute("select * from data")
    r=cur.fetchall()
    while True:
        print("Choose a method to cancel your ticket")
        print("1. PNR")
        print("2. Email Id")
        print("3. Phone Number")
        print("4. Exit")
        z=int(input("Enter your choice:"))
        f=0
        if z==1:
            a=input("Enter your PNR number: ").upper()
            for i in range(len(r)):
                if a == r[i][-2]:
                    q="update data set status='%s' where PNR='%s' " % ('CANCELLED', a)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print('='*100)
                break
            if f==0:
                print("Not Found")
                print('=' *100)
                break
        elif z==2:
            b=input("Enter your Email Id: ").upper()
            for j in range(len(r)):
                if b ==r[j][4]:
                    q=" update data set status='%s' where email_id='%s' " % ('CANCELLED', b)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print("="*100)
                break
            if f==0:
                print("Not Found")
                print('=' *100)
                break
        elif z==3:
            c=int(input("Enter your phone number:"))
            for k in range(len(r)):
                if c== r[k][3]:
                    q="update data set status='%s' where phone_no='%s' " %('CANCELLED',c)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print('=' *100)
                break
            if f==0:
                print("Not Found")
                print('-'*100)
                break
        elif z==4:
            break
        else:
            print(" Please choose a valid option")
            print("-"*100)
    cur.close()
    db.close()
def main():
    print("\t\t\t\t\t\t WELCOME TO DREAM AIRWAYS\t\t\t\t\t\t")
    dab()
    while True:
        print("Please select one of the following options  to continue: ")
        print("1. Book your tickets ")
        print("2. check your ticket status ")
        print("3. cancel ticket ")
        print("4. Exit")
        print('-'*200)
        n= int(input("Please enter your choice: "))
        if n==1:
            booking()
        elif n==2:
            status()
        elif n==3:
            cancel()
        elif n==4:
            print("\t\t\t\t\t\tThank you for visiting DREAM AIRWAYS \t\t\t\t\t\t")
            break
        else:
            print("Please choose a valid option, thankyou!")
            print('-'*200)
main()
   
        
    
