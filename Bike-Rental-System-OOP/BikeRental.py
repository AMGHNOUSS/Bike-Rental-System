#!/usr/bin/python3

import datetime

class BikeRental():
    """Class define Bike rental"""
    
    def __init__(self):
        self.stock = 100

    def displaystock(self):
        print(f"We have currently {self.stock} bikes available to rent.")