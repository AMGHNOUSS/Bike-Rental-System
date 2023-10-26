#!/usr/bin/python3

from BikeRental import BikeRental
from Customer import Customer
import unittest
import datetime

class CustomerTest(unittest.TestCase):
    """Test for class Customer"""

    def setUp(self):
        """initialize Object"""
        self.cus = Customer()
    
    def test_requestBike_for_bike_neg(self):
        """test for requestBike nagative"""
        self.assertEqual(self.cus.requestBike(2, -3), None)
    
    def test_requestBike_for_bike_pos(self):
        """test for requestBike positive"""
        self.assertEqual(type(self.cus.requestBike(2, 2)), dict)
    
    def test_returnBike(self):
        """test for return a bike"""
        dt = datetime.datetime.now()
        dict = {
                'fullName': "redouane amghnouss",
                'password': 1234,
                'bikes': 2,
                'rentalTime': dt,
                'rentalBasis': 20
            }
        self.assertEqual(self.cus.returnBike(dict, 'redouane amghnouss', 1234), (0 , 2, 20, dt))