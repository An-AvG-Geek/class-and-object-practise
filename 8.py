#library management system
class Book:

    def __init__(self,name,author,available_copies):
        self.name=name
        self.author=author
        self.available_copies=available_copies

        self.borrowers=[]

    def book_details(self):
        print(f'''the name of the book is {self.name}
                it is written by {self.author}
                there are {self.available_copies} of the books''')
        
class User:

    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.borrowed=[]

    def user_details(self):
        print(f''' name : {self.name}
               phone : {self.phone}'''
                )
        
        print(f'the borrowed books are ')

        if len(self.borrowed)==0:
            print('there are no books borrowed by {self.name}')

        else:
            for i in self.borrowed:
                print(i.name)

    def borrow_book(self,book):
        if book.available_copies>=1:
            self.borrowed.append(book)
            book.borrowers.append(self)
            book.available_copies-=1

        else:
            print("there are not enough books to be borrowed")

    def return_book(self,book):

        if book not in self.borrowed:
            print("invalid book .. cannot be returned")
        else:
            self.borrowed.remove(book)
            book.borrowers.remove(self)
            book.available_copies+=1


b1=Book("science textg book","hc verma",5)
b2=Book("maths text book","rd sharma",2)
b3=Book("english textbook","ncert",0)

u1=User("felix",34555)


u1.borrow_book(b2)
u1.user_details()
b2.book_details()
        


