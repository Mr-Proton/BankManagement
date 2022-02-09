import mysql.connector as sql
import sys

passw=input("Enter the pass word of database ")

try: #Checking password
    mydb=sql.connect(host="localhost",user="root",passwd=passw)
    print()
    print("success")
    print()
except:
    print("incorrect password")
    sys.exit()
print()


try: #Checking whether database exists or not
    mydb=sql.connect(host="localhost",user="root",passwd=passw,database="BankDB")
    i=1
    mydb.close()
except:
    i=0
print()


if i==0: #Creating database if it doesn't exist
    db=sql.connect(host="localhost",user="root",passwd=passw)
    cursor=db.cursor()
    cursor.execute("create database BankDB;")
    db.close()
    print()
    print("Database Created")
    print()
    mydb=sql.connect(host="localhost",user="root",passwd=passw,database="BankDB")
    mycursor=mydb.cursor
else:
    mydb=sql.connect(host="localhost",user="root",passwd=passw,database="BankDb")
    mycursor=mydb.cursor()
    print()
    print("Connection established")
    print()

try: #Checking whether table "bank" exists
    mycursor.execute('create table bank(ACCNO varchar(10) primary key,NAME varchar(20),MOBILE varchar(10),EMAIL varchar(40),ADDRESS varchar(20),CITY varchar(20),COUNTRY varchar(20),BALANCE float(12));')
    print("Table created")
    print()
except: 
    print()

    

print()

def Menu(): #Function to display the main menu
    print ("*"*140)
    print()
    print("MAIN MENU".center(140) )
    print("1. Insert Record/Records".center(140) )
    print("2. Display Records as per Account Number".center(140) )
    print(" a. Sorted as per Account Number".center(140) )
    print(" b. Sorted as per Customer Name".center(140) )
    print(" c. Sorted as per Customer Balance".center(140) )
    print("3. Search Record Details as per the account number".center(140) )
    print("4. Update Record".center(140) )
    print("5. Delete Record".center(140) )
    print("6. TransactionsDebit/Withdraw from the account".center(140) )
    print(" a. Debit/Withdraw from the account".center (140) )
    print(" b. Credit into the account".center(140) )
    print("7. Exit".center(140) )
    print()
    print("*"*140)
    print()
    ch=(input("Enter your choice (1,2,3,4,5,6,7) "))
    if ch=='1':
        Insert()
    elif ch=='2':
        MenuSort()
    elif ch=='3':
        DispSearchAcc()
    elif ch=='4':
        Update()
    elif ch=='5':
        Delete()
    elif ch=='6':
        MenuTransaction()
    elif ch=='7':
        print("Exiting...")
        sys.exit()
    else:
        print("Incorrect input, try again")
        Menu()


def MenuSort(): #Function to display sorting menu
    print()
    print(" a. Sorted as per Account Number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print(" d. Back".center(140))
    print("*"*140)
    ch=input("Enter your choice (a,b,c,d) ")
    if ch=="a" or ch=='A':
        DispSortAcc()
    elif ch=="b" or ch=="B":
        DispSortName()
    elif ch=="c" or ch=="C":
        DispSortBalance()
    elif ch=="d" or ch=="D":
        Menu()
    else:
        print("Incorrect input, try again")
        MenuSort()


def MenuTransaction(): #Function to display transaction menu
    print(" a. Debit/Withdraw from the account".center(140) )
    print(" b. Credit into the account".center(140) )
    print(" c. Back".center(140))
    ch=input("Enter your choice (a,b,c) ")
    if ch=="a" or ch=='A':
        Debit()
    elif ch=="b" or ch=="B":
        Credit()
    elif ch=="d" or ch=="D":
        Menu()
    else:
        print("Incorrect input, try again")
        MenuTransaction()
    
    
def Insert(): #Function to enter records to table
    while True:
        Acc=input("Enter account no \n")
        Name=input("Enter Name\n")
        Mob=input("Enter Mobile\n")
        email=input("Enter Email\n")
        Add=input ("Enter Address\n")
        City=input("Enter City\n")
        Country=input("Enter Country\n")
        Bal=float(input("Enter Balance\n") )
        Rec=[Acc, Name.upper(), Mob, email.upper() ,Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s);"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records? (y/n)")
        if ch=="n" or ch=="N":
            break
    Menu()


def DispSortAcc(): #Function to Display records as per ascending order of Account Number
    cmd="select * from BANK order by ACCNO;"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    print("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE")
    print()
    for i in data:
        print(i)
        print()
    print ("="*125)
    ch=input("Do you want to exit or go back to menu? (e/m) ")
    if ch=="e" or ch=="E":
        sys.exit()
    elif ch=="m" or ch=="M":
        Menu()
    else:
        print("Incorrect input. Exiting...")
        sys.exit()


def DispSortName(): #Function to Display records as per ascending order of Name
    cmd="select * from BANK order by NAME;"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    print("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE")
    print()
    for i in data:
        print(i)
        print()
    print ("="*125)
    ch=input("Do you want to exit or go back to menu? (e/m) ")
    if ch=="e" or ch=="E":
        sys.exit()
    elif ch=="m" or ch=="M":
        Menu()
    else:
        print("Incorrect input. Exiting...")
        sys.exit()


def DispSortBalance(): #Function to Display records as per ascending order of Balance
    cmd="select * from BANK order by BALANCE;"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    print("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE")
    print()
    for i in data:
        print(i)
        print()
    print ("="*125)
    ch=input("Do you want to exit or go back to menu? (e/m) ")
    if ch=="e" or ch=="E":
       sys.exit()
    elif ch=="m" or ch=="M":
        Menu()
    else:
        print("Incorrect input. Exiting...")
        sys.exit()


def DispSearchAcc(): #Function to Search for the Record from the File with respect to the account number
    cmd="select * from BANK"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    ch=input("Enter the accountno to be searched ")
    for i in data:
        if i[0]==ch:
            print(i)
            print()
            print("="*125)
            break
    else:
        print("Record Not found")
        print("="*125)
    print()
    ch=input("Do you want to exit or go back to menu? (e/m) ")
    if ch=="e" or ch=="E":
        sys.exit()
    elif ch=="m" or ch=="M":
        Menu()
    else:
        print("Incorrect input. Exiting...")
        sys.exit()


def Update(): #Function to change the details of a customer
    cmd="select * from BANK"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    num=input("Enter the AccNo. who's records need to be changed")
    for i in data:
        if i[0]==num:
            i=list(i)
            
            ch=input("Change Name(Y/N) ")
            if ch=='y' or ch=='Y':
                i[1]=input("Enter Name ")
                i[1]=i[1].upper()
            
            ch=input("Change Mobile(Y/N) ")
            if ch=='y' or ch=='Y':
                i[2]=input("Enter Mobile ")
            
            ch=input("Change Email(Y/N) ")
            if ch=='y' or ch=='Y':
                i[3]=input("Enter Email ")
                i[3]=i[3].upper()
            
            ch=input("Change Address(Y/N) ")
            if ch=='y' or ch=='Y':
                i[4]=input("Enter Address ")
                i[4]=i[4].upper()
            
            ch=input("Change City(Y/N) ")
            if ch=='y' or ch=='Y':
                i[5]=input("Enter City ")
                i[5]=i[5].upper()
            
            ch=input("Change Country(Y/N) ")
            if ch=='y' or ch=='Y':
                i[6]=input("Enter Country ")
                i[6]=i[6].upper()
            
            ch=input("Change Balance(Y/N) ")
            if ch=='y' or ch=='Y':
                i[7]=float(input("Enter Balance "))
                
            cmd="UPDATE BANK SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
            new=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
            mycursor.execute(cmd,new)
            mydb.commit()
            print("Account updated")
            break 
    else:
        print("Record not found")
    Menu()
        

def Delete(): #Function to Delete the details of a customer
    Cmd="select * from BANK"
    mycursor.execute(Cmd)
    data=mycursor.fetchall()
    num=input("Enter the AccNo. who's records need to be Detail ")
    for i in data:
        if i[0]==num:
            cmd="delete from bank where AccNo=%s"
            acc=(i[0],)
            mycursor.execute(cmd,acc)
            mydb.commit()
            print("Account Deleted")
            print()
            print("="*125)
            break
    else:
        print("Record not found")
        print()
        print("="*125)
    Menu()


def Credit():  #Function to credit into an account
    cmd="select * from BANK"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    num=input("Enter the AccNo. to which money needs to be credit ")
    for i in data:
        if i[0]==num:
            i=list(i)
            amt=float(input("Enter the amount to be credited "))
            i[7]=i[7]+amt
            cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
            val=(i[7],i[0])
            mycursor.execute(cmd,val)
            mydb.commit()
            print("Amount credited")
            print()
            print("="*125)
            break
    else:
        print("Account not found")
        print()
        print("="*125)
    Menu()


def Debit():  #Function to Debit from an account
    cmd="select * from BANK"
    mycursor.execute(cmd)
    data=mycursor.fetchall()
    num=input("Enter the AccNo. to which money needs to be debited ")
    for i in data:
        if i[0]==num:
            i=list(i)
            amt=float(input("Enter the amount to be debited, provided that there's a balance of 5000 rupees "))
            if (i[7]-amt)>=5000:
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=((i[7]-amt),i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount debited")
                print()
                print("="*125)
            else:
                print("Insufficient balance")
                print()
                print("="*125)
            break
    else:
        print("Record not found")
        print()
        print("="*125)
    Menu()

Menu()

        
                
    