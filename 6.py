# food ordering system

class Item:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show_items(self):

        print('the name of the food is ',self.name)
        print(f'the price of {self.name} is {self.price}')

class Customers:

    def __init__(self,name):
        self.name=name
        self.order=[]
    
    def add_item(self,item):
        self.order.append(item)

    
food1= Item("rice",50)
food2= Item("potato",500)

c1=Customers("felix")

c1.add_item(food1)
c1.add_item(food2)

for i in c1.order:
    print(f'the order is {i.name} which has price {i.price}')
    


        