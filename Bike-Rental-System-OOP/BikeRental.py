#!/usr/bin/python3

import datetime

class BikeRental():
    """Class define Bike rental"""
    
    def __init__(self):
        self.stock = 100

    def displaystock(self):
        """Display content of bikes"""
        print(f"We have currently {self.stock} bikes available to rent.")

    def rentBikeOnHourly(self, n):
        """Rent a bike on hourly basis"""
        if (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            dt = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,dt.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            
            self.stock -= n
            return dt
    
    def rentBikeOnDaily(self, n):
        """Rent a bike on daily basis"""
        if (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            dt = datetime.datetime.now()
            print(f"You have rented a {n} bike(s) on daily basis today at {dt.month}/{dt.day}.")
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            
            self.stock -= n
            return dt
    
    def rentBikeOnWeekly(self, n):
        """Rent a bike on weekly basis"""
        if (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            dt = datetime.datetime.now()
            print(f"You have rented a {n} bike(s) on weekly basis today at {dt.month}/{dt.day}.")
            print("You will be charged $60 for each day per bike.")
            print("We hope that you enjoy our service.")
            
            self.stock -= n
            return dt
    
    def returnBike(self, numOfBike, rentBaisis, dtOld):
        """Reuturn a bike """

        dtNew = datetime.datetime.now()
        result = dtNew.hour - dtOld.hour

        if rentBaisis == 2:
            baisis = 5
        elif rentBaisis == 3:
            baisis = 20
            result = result / 24
        elif rentBaisis == 4:
            baisis = 60
            result = result / 168

        cost = result * baisis * numOfBike
        
        if (3 <= numOfBike <= 5):
            print("You are eligible for Family rental promotion of 30% discount")
            cost = cost * 0.7
        print("Thanks for returning your bike. Hope you enjoyed our service!")
        print(f"That would be ${cost}")

        self.stock += numOfBike