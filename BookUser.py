def adduser():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    a=input("ENTER THE USERS NAME--------->_")
    b=int(input("ENTER LAST 3 DIGITE NUMBER OF THE USER PHONE NO.-->_"))
    c=input("ENTER POSTAL CODE----------->_")
    d=input("ENTER THE CITY NAME---------->_")
    e=input("ENTER THE DATE OF BIRTH------>_")
    A="insert into user(Name,Pno,Pcode,city,date) values('{}',{},{},'{}','{}')".format(a,b,c,d,e)
    cursor.execute(A)
    mydb.commit()
    print("USERS DETAIL IS ADDED")




def display():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    cursor.execute('select * from user')
    r=cursor.fetchall()
    for i in r:
        print(i)



def search():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    p=input("ENTER THE PHONE NUMBER OF THE USER TO BE SEARCHED:----->_")
    a="select * from user where Pno='{}'".format(p)
    cursor.execute(a)
    r=cursor.fetchall()
    print(r)






def update():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mydb.cursor()
    print("\v"*50)
    while True:
        print("*"*50)
        print("\t USER DETAILS")
        print("*"*50)
        print("<----------PRESS 1 FOR UPDATE USER BY ITS NAME------------>")
        print("<----------PRESS 2 FOR UPDATE USER BY ITS PHONE----------->")
        print("<----------PRESS 3 FOR UPDATE USER BY ITS CITY------------>")
        print("<----------PRESS 4 FOR UPDATE USER BY ITS DATE OF BIRTH--->")
        print("<----------PRESS 5 FOR UPDATE USER BY ITS POSTAL CODE----->")
        print("<----------PRESS 6 FOR EXIT------------------------------->")
        print("*"*50)
        x=int(input("ENTER THE CHOICE TO BE MODIFIED"))
        print("*"*50)
        print("NOTE==>> THE UPDATION TAKE PLACE ON THE BASIS OF PHONE NUMBER")
        if x==1:
            p=input("ENTER THE PHONE NUMBER  OF THE USER------>_")
            name=input("ENTER THE NAME TO BE MODIFIED------->_")
            A="update user set Name='{}' where Pno={}".format(name,p)
            cursor.execute(A)
            mydb.commit()
            print("DATA MODIFIED:")
        elif x==2:
            p=input("ENTER THE PHONE NUMBER  OF THE USER------>_")
            phno=input("ENTER THE PHONE NO. TO BE MODIFIED------->_")
            A="update user set Pno='{}' where Pno={}".format(phno,p)
            cursor.execute(A)
            mydb.commit()
            print("DATA MODIFIED:")
        elif x==3:
            p=input("ENTER THE PHONE NUMBER  OF THE USER------>_")
            city=input("ENTER THE CITY TO BE MODIFIED------->_")
            A="update user set city='{}' where Pno={}".format(city,p)
            cursor.execute(A)
            mydb.commit()
            print("DATA MODIFIED:")
        elif x==4:
            p=input("ENTER THE PHONE NUMBER  OF THE USER------>_")
            date=input("ENTER THE DOB TO BE MODIFIED------->_")
            A="update user set date='{}' where Pno={}".format(date,p)
            cursor.execute(A)
            mydb.commit()
            print("DATA MODIFIED:")
        elif x==5:
            p=input("ENTER THE PHONE NUMBER  OF THE USER------>_")
            Pcode=input("ENTER THE POSTAL CODE  TO BE MODIFIED------->_")
            A="update user set Pcode={} where Pno={}".format(Pcode,p)
            cursor.execute(A)
            mydb.commit()
            print("DATA MODIFIED:")
        elif x==6:
            break
        else:
            print("ENTER VALID DATA TO CONTINUE")





def delete():
     import mysql.connector
     mydb=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
     cursor=mydb.cursor()
     print("\v"*50)
     p=input("ENTER THE Pcode OF THE USER TO BE DELETED:----->_")
     a="delete from user where Pcode={}".format(p)
     cursor.execute(a)
     mydb.commit()
     print("DATA HAS BEEN DELETED")
    
            












        

    
    
