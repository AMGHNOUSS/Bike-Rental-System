#!/usr/bin/python3

import random
import datetime

class Customer():
    """Class Customer define request of Customer"""
    
    def __init__(self, b, c, rt, rb, fn, p):
        self.bikes = b
        self.Cost = c
        self.rentalTime = rt
        self.rentalBasis = rb
        self.fullName = fn
        self.password = p

    def requestBike(self, rb):
        """Request a Bike"""
        if  rb == 2:
            self.rentalBasis = 5
        elif rb == 3:
            self.rentalBasis = 20
        elif rb == 4:
            self.rentalBasis = 60
        bikes = input("How many bikes would you like to rent?")
        
        if bikes <= 0:
            print("That's not a positive integer!")
        else:
            self.bikes = bikes
            self.fullName = str(input("Your full name: "))
            self.password = int(self.generatePassword())
            print(f"This your password {self.password} remember it.")
            self.rentalTime = datetime.datetime.now()
            dict = {
                'fullName': self.fullName,
                'password': self.password,
                'bikes': self.bikes,
                'rentalTime': self.rentalTime,
                'rentalBasis': self.rentalBasis
            }
            return dict
    
    def generatePassword(self):
        """Generate a password for custmer"""
        all_code = '123456789'
        index = len(all_code)
        code = ''
        for  i in range(4):
            num = random.randint(0,index)
            code += all_code[num]
        return code
    
    def returnBike(self):
        """Functon for rerurn a Bike"""