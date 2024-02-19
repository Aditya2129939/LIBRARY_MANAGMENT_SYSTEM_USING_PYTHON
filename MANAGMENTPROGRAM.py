print("\t","\t","\t","\t","\t","\t","********","WELCOME TO DIGITAL LIBRARY MANAGMENT SOFTWARE","**********",)
print("************************************************************************************************************************************************************************")
import bookdetail
import BookUser
import issuebook
def Book():
    while True:
        print("*"*149)
        print("\t\tBOOK MENU")
        print("*"*149)
        print("<------PRESS 1 FOR ADDING MORE BOOKS---->")
        print("<------PRESS 2 FOR REMOVING BOOKS------->")
        print("<------PRESS 3 FOR DIPLAY BOOKS--------->")
        print("<------PRESS 4 FOR SEARCH BOOK---------->")
        print("<------PRESS 5 FOR UPDATE BOOK---------->")
        print("<------PRESS 6 FOR RETURN TO MAIN MENU-->")
        print("*"*149)
        choice=int(input("<===ENTER THE CHOICE===>_"))
        print("*"*149)
        if choice==1:
            bookdetail.addbook()
        elif choice==2:
            bookdetail.deletebook()
        elif choice==3:
            bookdetail.display()
        elif choice==4:
            bookdetail.search()
        elif choice==5:
            bookdetail.update()
        elif choice==6:
            break
        else:
            print("PRESS ANY KEY TO CONTINUE AND BACK TO MENU")
        ch=input('<----ENTER ANY KEY---->_')

def User():
    while True:
        print("*"*149)
        print("\t\tUSER DETAILS")
        print("*"*149)
        print("<------PRESS 1 FOR ADDING USER DETAIL--------->")
        print("<------PRESS 2 FOR DISPLAY USER DETAIL-------->")
        print("<------PRESS 3 FOR SEARCH USER---------------->")
        print("<------PRESS 4 FOR UPDATE USER---------------->")
        print("<------PRESS 5 FOR DELETE USER DETAIL--------->")
        print("<------PRESS 6 FOR RETURN TO MAIN MENU-------->")
        print("*"*149)
        choice=int(input("<===ENTER THE CHOICE===>_"))
        print("*"*149)
        if choice==1:
            BookUser.adduser()
        elif choice==2:
            BookUser.display()
        elif choice==3:
            BookUser.search()
        elif choice==4:
            BookUser.update()
        elif choice==5:
            BookUser.delete()
        elif choice==6:
            break
        else:
            print("INVALID ENTERY")

def Issue():
    while True:
        print("*"*149)
        print("\t\tUSER DETAILS")
        print("*"*149)
        print("<------PRESS 1 FOR ISSSUE BOOK----------------->")
        print("<------PRESS 2 FOR SEARCH PERSON DETAIL-------->")
        print("<------PRESS 3 FOR RETURN BOOKS---------------->")
        print("<------PRESS 4 FOR DISPLAY ISSUED BOOK--------->")
        print("<------PRESS 5 FOR RETURN TO MAIN MENU--------->")
        print("*"*149)
        choice=int(input("<===ENTER THE CHOICE===>_"))
        print("*"*149)
        if choice==1:
            issuebook.issues()
        elif choice==2:
            issuebook.search()
        elif choice==3:
            issuebook.returnbook()
        elif choice==4:
            issuebook.display()
        elif choice==5:
            break

        else:
            print("PRESS ANY KEY TO CONTINUE AND BACK TO MENU")
            ch=input('<----ENTER ANY KEY---->_')




while True:
    print("\t","\t","\t","\t","\t","\t","*****---","MENU DRIVE","---*******",)
    print("\v"*149) 
    print("<------PRESS 1 FOR BOOK DETAILS MENU DRIVE------------------------>")
    print("<------PRESS 2 FOR BOOK USER MENU DRIVE--------------------------->")
    print("<------PRESS 3 FOR BOOK ISSSUE AND DEPOSITING MUNU DRIVE --------->")
    print("<------PRESS 4 FOR EXIT------------------------------------------->")
    print("\v"*149)
    CH=int(input('ENTER YOUR CHOICE AGAIN:======>_'))
    if CH==1:
        Book()
    elif CH==2:
        User()
    elif CH==3:
        Issue()
    elif CH==4:
        break
    else:
        print("ENTER VALID DATA")
