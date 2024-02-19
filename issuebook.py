def issues():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    
    print("ISSUE THE BOOK")
    print("*"*50)
    a=input('ENTER BOOK ID----->')
    b=input('ENTER BOOK NAME->')
    c=input("ENTER AUTHOR NAME--->")
    print("*"*50)
    E="insert into issue (i_d,name,author) values({},'{}','{}')".format(a,b,c)
    #f="delete from book where i_d={}".format(a)
    cursor.execute(E)
    #cursor.execute(f)

    mydb.commit()
    print("--------------***INFORMATION ADDED***----------------")
    print("--------------***BOOK HAS BEEN ISSUED***----------------")
    print("\n")


    

def search():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    a=input("ENTER PERSON ID")
    w="select * from issue where i_d={}".format(a)
    
    cursor.execute(w,a)
    r=cursor.fetchall()
    print(r)
    print("\n")

def returnbook():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    e=input('ENTER BOOK ID------------------>_')
    b=input("ENTER BOOK NAME---------------->_")
    c=input("ENTER THE AUTHOR NAME-->_")
    j="insert into book (i_d,name,author) values({},'{}','{}')".format(e,b,c)
    #l="delete from issue where i_d={}".format(e)
    cursor.execute(j)
    #cursor.execute(l)
            
    mydb.commit()
    print("FILE IS UPDATED")

def display():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    
    w="select * from issue "
    
    cursor.execute(w)
    r=cursor.fetchall()
    print(r)
    print("\n")
