# create a class car with brand and price and print them

class Car:
    def __init__(self,brand, price):

        self.brand=brand
        self.price=price
   
# car1=Car("ford",3000)
# car2=Car("ferrari",599)

# print(f"the brand of car is {car1.brand} and the price is {car1.price}")
# print(f"the brand of car is {car2.brand} and the price is {car2.price}")

#create a clas named rectangle and print its area

class Rectangle:

    def __init__(self,length,breadth):

        self.length=length
        self.breadth=breadth

    def print_area(self):

        print(f"the area is {self.breadth*self.length}")

# rect=Rectangle(20,30)

# rect.print_area()

# create class bank acc with deposit and withdraw funct

class Bank:
    def __init__(self,accno,initial):
        self.accno=accno
        self.balance=initial

    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-amt
    def deposit(self,amt):
        if amt<0:
            print("invalid input")
        else:
            self.balance=self.balance+amt
    def show_amount(self):
        print(f"the account number is {self.accno}")
        print(f"the balance is {self.balance}")


# user1=Bank(1,400)
# user1.show_amount()
# user1.deposit(100)
# user1.show_amount()
# user1.withdraw(100000)
# user1.show_amount()
# user1.withdraw(50)
# user1.show_amount()
# user1.deposit(-100)


#create a class student with name and marks as list and method average to compute average of students and print them also

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"the name of the student is {self.name}")
        print(f"the marks of the student is {self.marks}")

    def average(self):
        print(f"the average of all the marks of the student is {sum(self.marks)/len(self.marks)}")

# s1=Student("felix",[1,2,3,4,5])
# s1.display()
# s1.average()


class Students:
    school="ABC"

    def __init__(self,name):
        self.name=name
    def print_name(self):
        print(f"the name of the student is {self.name}")
        print(f"the name of the school is {Students.school}")

# s1=Students("felix")
# # s1.print_name()

#  Students.school="my school"
# # s1.print_name()

# create class employee with class variable company name and instance variable name and salary

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    company="Yes bank"

    def print_emp_details(self):
        print(f'the name of the company is {self.company}')
        print(f"the name of the employee is {self.name}")
        print(f'the salary of the employee is {self.salary}')

# e=Employee("felix",7888)

# e.print_emp_details()