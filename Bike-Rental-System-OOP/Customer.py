#!/usr/bin/python3


class Customer():
    """Class Customer define request of Customer"""
    
    def __init__(self, b, c, rt, rb, fn, p):
        self.bikes = b
        self.Cost = c
        self.rentalTime = rt
        self.rentalBasis = rb
        self.fullName = fn
        self.password = p

    def requestBike(self):
        """Request a Bike"""

        bikes = input("How many bikes would you like to rent?")
        
        if bikes <= 0:
            print("That's not a positive integer!")
        else:
            self.bikes = bikes
        
        self.fullName = str(input("Your full name:"))

        return self.bikes
