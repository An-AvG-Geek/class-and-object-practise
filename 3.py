# create user class for carpooling app

class User:
    total_users=0

    def __init__(self,phone,name):
        self.phone=phone
        self.name=name
        User.total_users+=1
    
    def show(self):
        print(f"name : {self.name}")
        print(f"phone : {self.phone}")
    
    @classmethod
    def get_total_users(cls):

        return f"the total users is {cls.total_users}"
    
    @staticmethod
    def is_valid_phone(phone):

        if len(phone)==3:
            return True
        else:
            return False
    
if User.is_valid_phone("123"):
    u1=User("123","felix")


u1.show()
print(User.get_total_users())