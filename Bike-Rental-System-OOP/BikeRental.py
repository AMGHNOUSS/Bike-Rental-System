#!/usr/bin/python3

import datetime

class BikeRental():
    """Class define Bike rental"""
    
    def __init__(self):
        self.stock = 100

    def displaystock(self):
        """Display content of bikes"""
        print(f"We have currently {self.stock} bikes available to rent.")
        return self.stock

    def rentBikeOnHourly(self, n, dt):
        """Rent a bike on hourly basis"""
        if n <= 0:
            return False 
        elif (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,dt.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.\n")
            
            self.stock -= n
            return True
    
    def rentBikeOnDaily(self, n, dt):
        """Rent a bike on daily basis"""
        
        if n <= 0:
            return False 
        elif (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            print(f"You have rented a {n} bike(s) on daily basis today at {dt.month}/{dt.day}.")
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.\n")
            
            self.stock -= n
            return True
    
    def rentBikeOnWeekly(self, n, dt):
        """Rent a bike on weekly basis"""
        
        if n <= 0:
            return False 
        elif (n > self.stock):
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return False
        else:
            print(f"You have rented a {n} bike(s) on weekly basis today at {dt.month}/{dt.day}.")
            print("You will be charged $60 for each day per bike.")
            print("We hope that you enjoy our service.\n")
            
            self.stock -= n
            return True
    
    def returnBike(self, numOfBike, rentBaisis, dtOld):
        """Reuturn a bike """

        dtNew = datetime.datetime.now()
        result = dtNew.hour - dtOld.hour

        cost = result * rentBaisis * numOfBike
        
        print()
        if (3 <= numOfBike <= 5):
            print("You are eligible for Family rental promotion of 30% discount")
            cost = cost * 0.7
        print("Thanks for returning your bike. Hope you enjoyed our service!")
        print(f"That would be ${cost}")

        self.stock += numOfBike