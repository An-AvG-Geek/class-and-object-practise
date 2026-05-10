# driver_name
# start_location
# destination
# price
# available_seats


class Ride:
    total_rides = 0

    def __init__(self,driver_name,start_location,destination,price,available_seats):
        self.driver_name=driver_name
        self.start_location=start_location
        self.destination=destination
        self.price=price
        self.available_seats=available_seats
        Ride.total_rides+=1
    
    def show_ride(self):
        print(f"the driver name is {self.driver_name}")
        print(f"the start location is {self.start_location}")
        print(f"the destination is {self.destination}")
        print(f"the price of the ride is {self.price}")
        print(f"the available seats is {self.available_seats}")

    def book_seat(self):
        if self.available_seats>0:
            self.available_seats-=1
        else:
            print(f"no seats available")

    
    @classmethod
    def get_total_rides(cls):
        print(f"the total number of rides is {Ride.total_rides}")

    @staticmethod
    def is_valid_price(price):
        if price<0:
            return False
        else:
            return True
        


if Ride.is_valid_price(123):
    r1=Ride("felix","ernakulam","trivandrum",123,10)
    r1.show_ride()
    Ride.get_total_rides()
    r1.book_seat()
    r1.show_ride()




        