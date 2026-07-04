class book:
    def __init__(self,bookno,bookname,auther):
        self.bookno=bookno
        self.bookname=bookname
        self.auther=auther

    def show(self):
        print("Book no: ",self.bookno)
        print("Book name: ",self.bookname)
        print("Auther's Name: ",self.auther)

class library:
    def __init__(self):
        self.book=[]
    
    def add_book(self):
        bookno=int(input("Enter book No.: " ))
        bookname=input("Enter Book Name: ")
        auther=input("Enter auther's Name: ")

        b=book(bookno,bookname,auther)

        self.book.append(b)
        b.show()
        print("Book added Successfully")

    def search_book(self):
        bookno=int(input("Enter book No.: "))
        for b in self.book:
            if bookno==b.bookno:
                print("book Found")
                b.show()
                return
            print("book Not Found")
                

    def delete_book(self):
        bookno=int(input("Enter book No.: "))
        for b in self.book:
            if bookno==b.bookno:
                self.book.remove(b)
                print("Book Deleted")
                return
            print("Book Not Found")
                
        
    def exit(self):
        print("Thank You! ")

a=library()
while True:
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        a.add_book()
    elif choice==2:
        a.search_book()
    elif choice==3:
        a.delete_book()
    elif choice==4:
        a.exit()
        break
    else:
        print("wrong Choice")

