#!/usr/bin/python3

import random
import datetime

class Customer():
    """Class Customer define request of Customer"""
    
    def __init__(self):
        """Constructor"""

    def requestBike(self, rb):
        """Request a Bike"""
        if  rb == 2:
            self.rentalBasis = 5
        elif rb == 3:
            self.rentalBasis = 20
        elif rb == 4:
            self.rentalBasis = 60
        bikes = int(input("How many bikes would you like to rent? "))
        
        if bikes <= 0:
            print("That's not a positive integer!")
            return None
        else:
            self.bikes = bikes
            self.fullName = str(input("Your full name: "))
            self.password = int(self.generatePassword())
            print(f"This your password {self.password} remember it.\n")
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
        index = len(all_code) - 1
        code = ''
        for  i in range(4):
            num = random.randint(0,index)
            code += all_code[num]
        return code
    
    def returnBike(self, dict):
        """Functon for rerurn a Bike"""
        name = str(input("What's your full name: "))
        pswd = int(input("Your password: "))

        found = False  # A flag to check if the user was found
        i = 0
        for user in dict:
            if user['fullName'] == name and user['password'] == pswd:
                found = True
                return [i, user['bikes'], user['rentalBasis'], user['rentalTime']]
            i += 1
        if not found:
            print()
            print("User not found or password is incorrect.")
            return None
