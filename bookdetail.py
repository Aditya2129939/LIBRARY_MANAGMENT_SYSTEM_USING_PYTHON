
def addbook():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mycon.cursor()
    print("\v"*150)
    A=int(input('ENTER BOOK ID:---------------------------->_'))
    B=input('ENTER BOOK NAME:------------------------->_')
    C=input('ENTER THR AUTHOR''S NAME--------------->')

    G="INSERT INTO  book (i_d,name,author) VALUES ({},'{}','{}')".format(A,B,C)
    cursor.execute(G)
    mycon.commit()
    print("NEW BOOK RECORD ADDED")
    print("*"*100)



def display():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mycon.cursor()
    print("\v"*150)
    cursor.execute("select * from book")
    r=cursor.fetchall()
    for i in r:
        print(i)
    
    print('-/'*100)



def update():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mycon.cursor()
    print("\v"*150)
    
    print('-/'*100)
    print("\v"*50)
    print("**********************MENU FOR MODIFICATION OF DETAILS*******************")
    print("\n")
    print("<------------PRESS 1 FOR BOOK ID---------------->")
    print("<------------PRESS 2 FOR BOOK NAME-------------->")
    print("<------------PRESS 3 FOR AUTHOR NAME------------>")
    print("*"*50)
    q=int(input("ENTER YOUR CHOICE FROM THE MENU WHICH YOU WANT TO MODIFY:----->_"))
    if q==1:
        print('\n')
        x=input('ENTER BOOK ID TO BE ADDED------>_')
        z=input('ENTER BOOK ID TO BE REMOVE----->_')
        y="update book set i_d={} where i_d={}".format(x,z)
        cursor.execute(y)
        mycon.commit()
        print('UPDATED RECORD')
    elif q==2:
        print('\n')
        x=input('ENTER BOOK NAME  TO BE CHANGE TO------------->_')
        z=input('ENTER BOOK NAME BY WHICH YOU WANT TO CHANGE----->_')
        y="update book set name='{}' where name='{}'".format(x,z)
        cursor.execute(y)
        mycon.commit()
        print('UPDATED RECORD')
    elif q==3:
        print('\n')
        x=input('ENTER AUTHOR NAME TO BE CHANGE ----------------------->_')
        z=input('ENTER AUTHOR NAME WHICH YOU WANT TO REPLACE----->_')
        y="update book set author='{}' where author='{}'".format(x,z)
        cursor.execute(y)
        mycon.commit()
        print('UPDATED RECORD')
    else:
       print("ENTER VALID DATA")



def deletebook():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mycon.cursor()
    print("\v"*50)
    print('PRESS 1 FOR DELETE BY BOOK NAME \n PRESS 2 FOR  DELETE BY BOOK ID \n PRESS 3 FOR DELETE BY AUTHOR NAME')
    print("\-"*50)
    ch=int(input("ENTER YOUR CHOICE---->_"))
    if ch==1:
        x=input('ENTER THE BOOK NAME WHICH YOU WANT TO DELETE---->_')
        y="delete from book where name='{}'".format(x)
        cursor.execute(y)
        mycon.commit()
    elif ch==2:
        x=input('ENTER BOOK  NAME TO DELETE---->_')
        Y="delete from book where i_d={}".format(x)
        cursor.execute(Y)
        mycon.commit()
    elif ch==3:
        x=input('ENTER BOOK AUTHOR TO DELETE---->_')
        Y="delete from book where author='{}'".format(x)
        cursor.execute(Y)
        mycon.commit()
    else:
        print("WRONG INPUT")
    print('DELETE')
    print("*")




def search():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="aditya",database='library')
    cursor=mycon.cursor()
    print("\v"*50)
    A="select * from book"
    cursor.execute(A)
   
    for i in cursor:   #cursor got the details of the value books
        b=list(i)
    
    print('/'*50)
    print('********************MENU FOR SEARCHING DETAILS ON THE BASIS OD CHOICE*******************')
    print("<------------PRESS 1 FOR BOOK ID---------------->")
    print("<------------PRESS 2 FOR BOOK NAME-------------->")
    print("<------------PRESS 3 FOR AUTHOR NAME------------>")
    print("\n")
    ch=int(input("ENTER YOUR CHOICE"))
    if ch==1:
        x=int(input("ENTER THE BOOK ID TO SEARCH------>_"))
        
        y="select * from book where i_d={}".format(x)
        cursor.execute(y)
        r=cursor.fetchall()
        print(r)
        
    elif ch==2:
        x=input("ENTER THE BOOK NAME TO SEARCH------>_")
        
        y="select * from book where name='{}'".format(x)
        cursor.execute(y)
        r=cursor.fetchall()
        print(r)
        
    elif ch==3:
        x=input("ENTER THE AUTHOR NAME OF THE BOOK TO SEARCH------->_")
        
        y="select * from book where author='{}'".format(x)
        cursor.execute(y)
        r=cursor.fetchall()
        print(r)
        
    else:
        print('ENTER VALID INPUT')


        
        






























        
        
