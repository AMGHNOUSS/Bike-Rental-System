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