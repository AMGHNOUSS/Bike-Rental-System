#!/usr/bin/python3

from  BikeRental import BikeRental
import unittest
import datetime

class BikeRentalTest(unittest.TestCase):
    """Class Test For class BikeRental"""

    def test_displaystock(self):
        """100 bikes"""
        bk = BikeRental()
        self.assertEqual(bk.displaystock(), 100)
    
    def test_rentBikeOnHourly(self):
        """Rent some bikes on hourly basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnHourlyBasis(-1, dt), False)
    
    def test_rentBikeOnHourly_for_number_negative(self):
        """Rent some bikes on hourly basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnHourlyBasis(-1, dt), False)
    
    def test_rentBikeOnHourly_for_zero(self):
        """Rent some bikes on hourly basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnHourlyBasis(0, dt), False)
    
    def test_rentBikeOnHourly_for_number_positive(self):
        """Rent some bikes on hourly basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnHourlyBasis(2, dt), True)

    def test_rentBikeOnHourly_for_number_positive_big_than_bike(self):
        """Rent some bikes on hourly basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnHourlyBasis(101, dt), False)

    def test_rentBikeOnDaily(self):
        """Rent some bikes on Daily basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnDailyBasis(-1, dt), False)
    
    def test_rentBikeOnDaily_for_number_negative(self):
        """Rent some bikes on Daily basis"""
        bk = BikeRental()
        dt = datetime.datetime.now()
        self.assertEqual(bk.rentBikeOnDailyBasis(-1, dt), False)
    