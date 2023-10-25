#!/usr/bin/python3

from BikeRental import BikeRental
from Customer import Customer
import unittest
import datetime

class CustomerTest(unittest.TestCase):
    """Test for class Customer"""

    def setUp(self):
        """initialize Object"""
        cus = Customer()