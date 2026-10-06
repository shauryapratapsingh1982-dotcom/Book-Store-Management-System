import mysql.connector
from mysql.connector import Error

def create_database_and_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = connection.cursor()

        # Check if the 'bookstore' database exists
        cursor.execute("SHOW DATABASES LIKE 'bookstore'")
        result = cursor.fetchone()

        if result is None:
            print("Database 'bookstore' does not exist. Creating it now...")
            cursor.execute("CREATE DATABASE bookstore")
            print("Database 'bookstore' created successfully.")
        else:
            print("Database 'bookstore' already exists.")

        cursor.execute("USE bookstore")

        # Check if the 'avail_books' table exists
        cursor.execute("SHOW TABLES LIKE 'avail_books'")
        if cursor.fetchone() is None:
            print("Table 'avail_books' does not exist. Creating it now...")
            cursor.execute("""
                CREATE TABLE avail_books (
                    bookname VARCHAR(25) PRIMARY KEY,
                    genre VARCHAR(25),
                    qty INT,
                    author VARCHAR(25),
                    price FLOAT
                )
            """)
            print("Table 'avail_books' created successfully.")

        # Check if the 'staff_details' table exists
        cursor.execute("SHOW TABLES LIKE 'staff_details'")
        if cursor.fetchone() is None:
            print("Table 'staff_details' does not exist. Creating it now...")
            cursor.execute("""
                CREATE TABLE staff_details (
                    name VARCHAR(25) PRIMARY KEY,
                    gender VARCHAR(10),
                    age INT,
                    phno VARCHAR(12),
                    address TEXT
                )
            """)
            print("Table 'staff_details' created successfully.")

        # Check if the 'sellrec' table exists
        cursor.execute("SHOW TABLES LIKE 'sellrec'")
        if cursor.fetchone() is None:
            print("Table 'sellrec' does not exist. Creating it now...")
            cursor.execute("""
                CREATE TABLE sellrec (
                    cusname VARCHAR(25),
                    phno varchar(12),
                    bookname VARCHAR(25),
                    qty INT,
                    price FLOAT,
                    total_price FLOAT,
                    FOREIGN KEY (bookname) REFERENCES avail_books(bookname)
                )
            """)
            print("Table 'sellrec' created successfully.")

        # Check if the 'signup' table exists
        cursor.execute("SHOW TABLES LIKE 'signup'")
        if cursor.fetchone() is None:
            print("Table 'signup' does not exist. Creating it now...")
            cursor.execute("""
                CREATE TABLE signup (
                    usernm VARCHAR(25) PRIMARY KEY,
                    pass VARCHAR(25)
                )
            """)
            print("Table 'signup' created successfully.")

        # Check if the 'Admin' table exists
        cursor.execute("SHOW TABLES LIKE 'Admin'")
        if cursor.fetchone() is None:
            print("Table 'Admin' does not exist. Creating it now...")
            cursor.execute("""
                CREATE TABLE Admin (
                    username VARCHAR(25) PRIMARY KEY,
                    password VARCHAR(25)
                )
            """)
            print("Table 'Admin' created successfully.")
            cursor.execute("""Insert into admin values('admin123','12345678');""")

        # Commit any changes (even though we haven't done any inserts yet)
        connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function to create the database and tables if they don't exist
create_database_and_tables()

DB=mysql.connector.connect(host="localhost",
 user="root",
 password="root",
 database="bookstore"
)
C=DB.cursor()
def addbook():
    print("Enter Book Details:-")
    book=input("Enter name of book:")
    genre=input("Enter genre:")
    qty=int(input("Enter quantity:"))
    author=input("Enter author:")
    price=float(input("Enter price of book:"))
    sql="insert into avail_books values(%s,%s,%s,%s,%s)"
    values=(book,genre,qty,author,price)
    C.execute(sql,values)
    DB.commit()
    print("""++++++++++++++++++++++++ SUCCESSFULLY ADDED ++++++++++++++++++++++++""")
    n=int(input("Want to continue?\n Yes:1 No:2\n Choice:"))
    if n==1:
        addbook()
    else:
        Admin()
def newstaff():
    sname=str(input("Enter Full name:"))
    gender=str(input("Gender(M/F/O):"))
    age=int(input("Age:"))
    phno=int(input("Staff phone no.:"))
    add=str(input("Address:"))
    sql="INSERT INTO staff_details values(%s,%s,%s,%s,%s)"
    values=(sname,gender,age,phno,add)
    C.execute(sql,values)
    DB.commit()
    print("""++++++++++++++++++++++++++++++STAFF IS SUCCESSFULLY ADDED++++++++++++++++++++++++++++++""")
    n=int(input("Want to continue?\n Yes:1 No:2\n Choice:"))
    if n==1:
        newstaff()
    else:
        Admin()
def removestaff():
    name=(input("Staff Name to Remove: "))
    sql="delete from staff_details where name=(%s)"
    values=(name,)
    C.execute(sql,values)
    DB.commit()
    print("Above Employee is removed")
    n=int(input("Want to continue?\n Yes:1 No:2\n Choice:"))
    if n==1:
        removestaff()
    else:
        Admin()
def staffdetails():     
    detail = "SELECT * FROM staff_details"     
    C.execute(detail)     
    output = C.fetchall()     
    
    if not output:
        print("-----------------------------------------------------------------------")
        print("    No entry was found in the staff details")
        print("-----------------------------------------------------------------------")
    else:
        for x in output:         
            print("************************************")         
            print("Name of Employee:", x[0])         
            print("Gender of Employee:", x[1])         
            print("Age of Employee:", x[2])         
            print("Phone No of Employee", x[3])         
            print("Address of Employee:", x[4])         
            print("************************************")
    Admin()
def sellrec():
    C.execute("SELECT * FROM sellrec")
    data = C.fetchall()  # Fetch all rows from the query result
    if not data:
        print("---------------------------------------------------------")
        print("       No sales records found ")
        print("---------------------------------------------------------")
    else:
        for i in data:
            print("*********************************************")
            print("Buyer Name: ", i[0])
            print("Buyer Mobile Number: ", i[1])
            print("Book Purchased: ", i[2])
            print("Quantity Bought: ", i[3])
            print("Price of Book: ", i[4])
            print("Total Price of Books: ", i[5])
            print("**********************************************")
    Admin()
def delrec():
    b=input("Are you sure(Y/N):").upper()
    if b=="Y":
        C.execute("delete from sellrec")
    DB.commit()
    Admin()
def Totalincome():
    C.execute("select sum(total_price) from sellrec")
    r=C.fetchone()
    print("Total Income till date:",r[0])
    Admin()
def Availbook():
    C.execute("select * from avail_books order by bookname")
    data = C.fetchall()  # Fetch all rows from the query result
    if not data:
        print("---------------------------------------------------------")
        print("       No available books ")
        print("---------------------------------------------------------")
    else:
        C.execute("select * from avail_books order by bookname")
        for v in C:
            print("****************************************************")
            print("Book Name: ",v[0])
            print("Book Genre: ",v[1])
            print("Book Available: ",v[2])
            print("Book Author: ",v[3])
            print("Book Price: ", v[4])
            print("****************************************************")
    Admin()
#Buyer Function
def AvailbookU():
    C.execute("select * from avail_books order by bookname")
    data = C.fetchall()  # Fetch all rows from the query result
    if not data:
        print("---------------------------------------------------------")
        print("       No available books ")
        print("---------------------------------------------------------")
    else:
        C.execute("select * from avail_books order by bookname")
        for v in C:
            print("****************************************************")
            print("Book Name: ",v[0])
            print("Book Genre: ",v[1])
            print("Book Available: ",v[2])
            print("Book Author: ",v[3])
            print("Book Price: ", v[4])
            print("****************************************************")
    Buyer()
def purchase():
        C.execute("select * from avail_books order by bookname")
        for v in C:
            print("****************************************************")
            print("Book Name: ",v[0])
            print("Book Genre: ",v[1])
            print("Book Available: ",v[2])
            print("Book Author: ",v[3])
            print("Book Price: ", v[4])
            print("****************************************************")
        cusname = str(input("Enter customer name:"))
        phno = int(input("Enter phone number:"))
        book = str(input("Enter Book Name:"))
        C.execute("select price from avail_books where bookname=%s", (book,))
        price_result = C.fetchone()  
        if price_result is None:
            print("************************")
            print("    Book not available")
            print("************************")
            Buyer()
        price = price_result[0]  
        n = int(input("Enter quantity:"))
        C.execute("select qty from avail_books where bookname=%s", (book,))
        qty_result = C.fetchone()
        if qty_result is None:
            print("************************")
            print("   Book not available")
            print("************************")
            Buyer()
        available_qty = qty_result[0]  
        if available_qty < n:
            print("*******************************")
            print(n," books are not available!!!!")
            print("*******************************")
            Buyer()
        else:
            C.execute("select bookname from avail_books where bookname=%s", (book,))
            log = C.fetchone()
            if log is not None:
                total_price = price * n
                C.execute("insert into Sellrec (cusname, phno, bookname, qty, price, total_price) values (%s, %s, %s, %s, %s, %s)", 
                      (cusname, phno, book, n, price, total_price))
                C.execute("update avail_books set qty=qty-%s where bookname=%s", (n, book))
                DB.commit()
                print("++++++++++++++++++++++++BOOK HAS BEEN PURCHASED SUCCESSFULLY++++++++++++++++++++++++")
            else:
                print("**************************************")
                print("       BOOK IS NOT AVAILABLE!!!!!!!")
                print("**************************************")
        choice=int(input("Want to continue?\n Yes:1 No:2\n Choice:"))
        if choice==1:
            purchase()
        else:
            Buyer()
def namesearch():
    x=input("Enter Book name to search:")
    C.execute("select bookname from avail_books where bookname =%s",(x,))
    t=C.fetchone()
    if t != None:
        print("""++++++++++++++++++++++BOOK IS IN STOCK++++++++++++++++++++++""")
        C.execute("select * from avail_books where bookname =%s",(x,))

        for y in C:
            print("*******************************************")
            print("Book Name: ",y[0])
            print("Book Genre: ",y[1])
            print("Quantity Available: ",y[2])
            print("Book Author:", y[3])
            print("Book Price: ", y[4])
            print("*******************************************")

    else:
        print("*********************************")
        print("   BOOK IS NOT IN STOCK!!!!!!!")
        print("*********************************")
    Buyer()
def genresearch():
    g=input("Enter genre to search:")
    C.execute("select genre from avail_books where genre=%s",(g,))
    poll=C.fetchall()
    if poll is not None:
        print("""++++++++++++++++++++++BOOK IS IN STOCK++++++++++++++++++++++""")

        C.execute("select * from avail_books where genre=%s",(g,))

        for y in C:
            print("*******************************************")
            print("Book Name: ",y[0])
            print("Book Genre: ",y[1])
            print("Quantity Available: ",y[2])
            print("Book Author:", y[3])
            print("Book Price: ", y[4])
            print("*******************************************")
    else:
        print("*********************************************************")
        print("   BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")
        print("*********************************************************")
    Buyer()
def authorsearch():
    a=input("Enter Book's Author to search:")
    C.execute("select bookname from avail_books where Author =%s",(a,))
    t=C.fetchone()
    if t != None:
        print("""++++++++++++++++++++++BOOK IS IN STOCK++++++++++++++++++++++""")
        C.execute("select * from avail_books where Author =%s",(a,))
        for y in C:
            print("*******************************************")
            print("Book Name: ",y[0])
            print("Book Genre: ",y[1])
            print("Quantity Available: ",y[2])
            print("Book Author:", y[3])
            print("Book Price: ", y[4])
            print("*******************************************")
    else:
        print("**************************************")
        print("       BOOK IS NOT IN STOCK!!!!!!!")
        print("**************************************")
    Buyer()
def Admin():
    print("==================================")
    print("""    1:Add Books
    2.Staff Details
    3.Sale Record
    4.Total Income after the Latest Reset
    5. See Available Book
    6. Exit""")

    print("==================================")
    n=int(input("Enter Your Choice: "))
    #To Add Books 
    if n==1:
        addbook()
    #Choice For New Staff, Fire staff, View Staffh
    if n==2:
        print("""1:New staff entry\n2:Remove staff\n3:Existing staff details""")
        ch=int(input("Enter your choice: "))
        if ch==1:
            newstaff()
        elif ch==2:
            removestaff()
        elif ch==3:
            staffdetails()
    #Sale Record
    if n==3:
        print("""1:Sale history details\n2:Reset Sale history""")

        ty=int(input("Enter your choice:"))
        if ty==1:
            sellrec()
        if ty==2:
            delrec()

    #Total income
    if n==4:
        Totalincome()
    #Available books 
    if n==5:
        Availbook()
    if n==6:
        return
def Buyer():
    print("==================================")
    print("""1.Purchase Books\n2.Search Books\n3.Available Books\n4. Exit""")
    print("==================================")
    r=int(input("Enter Your Choice: "))
    #TO PURCHASE BOOK
    if r==1:
        purchase()
    #Searching of books using Name,Genre,Author
    if r==2:
        print("""1:Search by name\n2:Search by genre\n3:Search by author""")
        l=int(input("Search by What : "))
        if l==1:
            namesearch()
        if l==2:
            genresearch()
        if l==3:
            authorsearch()
    if r==3:
        AvailbookU()
    if r==4:
        return
#MAIN PROGRAM
print("=======================================================================================")
print("<<<<<<<<<<<<<<<<<<<<<<<<< II WELCOME TO THE BOOKSTORE II >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("=======================================================================================")
while 1:
    a=int(input("""Enter as Admin: 1\nEnter as Customer: 2\nExit : 3\n========================\nEnter : """ ))
    if a==1:
        admin_username=input("Enter Admin Username:")
        admin_pass = input("Enter Admin Password: ")

        # Check if the password matches the stored admin password
        C.execute("SELECT password FROM Admin WHERE username =%s",(admin_username,))  
        result = C.fetchone()

        if result is not None:
            stored_password = result[0]  

            if admin_pass == stored_password:
                print("************************Admin Login Success********************")
                Admin()
            else:
                print("==================================")
                print("Incorrect admin password Please try again")
                print("==================================")
        else:
            print("================================================")
            print("Admin account not found Contact system administrator")
            print("================================================")
    if a==2:
        print("""**************** BOOK STORE *********************\n1. Signup\n2. login""")
        s=int(input("Enter Your Choice: "))

        if s==1:
            usernm=input("USERNAME(ex: abcd1234): ")
            passw=input("PASSWORD: ")

            C.execute("insert into signup values(%s,%s)",(usernm,passw))
            DB.commit()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("                                  Sign Up Completed")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        else:
            user2 = input("Enter Your Username: ")

            # Check if the username exists in the database
            C.execute("SELECT pass FROM Signup WHERE usernm =%s", (user2,))
            result = C.fetchone()

            if result!=None:
                stored_password = result[0] 
                b1 = input("Enter Your Password: ")

                if b1 == stored_password:
                    print("************************ Login Successful ********************")
                    Buyer()
                else:
                    print("==================================")
                    print("Incorrect password Please try again")
                    print("==================================")
            else:
                print("=========================================")
                print("Username not found Please sign up or try again")
                print("=========================================")
    if a==3:
        print("====================================")
        print("THANKYOU FOR USING OUR PROGRAM")
        print(" Made by- Shaurya, Shashwat, Shristi")
        print("====================================")
        break
