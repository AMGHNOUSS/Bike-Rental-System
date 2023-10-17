#!/usr/bin/python3

import random

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
        self.password = int(self.generatePassword())

        return self.bikes
    
    def generatePassword(self):
        """Generate a password for custmer"""
        all_code = '0123456789'
        index = len(all_code)
        code = ''
        for  i in range(4):
            num = random.randint(0,index)
            code += all_code[num]
        return code