#!/usr/bin/python3

from BikeRental import BikeRental
from Customer import Customer
import unittest
import datetime

class BikeRentalTest(unittest.TestCase):
    """Class Test For class BikeRental"""

    def setUp(self):
        self.bk = BikeRental()
        self.dt = datetime.datetime.now()
        self.cus = Customer()
    
    def tearDown(self) -> None:
        print('Finish testing')

    def test_displaystock(self):
        """100 bikes"""
        self.assertEqual(self.bk.displaystock(), 100)

    # On Hourly    
    def test_rentBikeOnHourly(self):
        """Rent some bikes on hourly basis"""
        self.assertEqual(self.bk.rentBikeOnHourly(-1, self.dt), False)
    
    def test_rentBikeOnHourly_for_number_negative(self):
        """Rent some bikes on hourly basis"""
        self.assertEqual(self.bk.rentBikeOnHourly(-1, self.dt), False)
    
    def test_rentBikeOnHourly_for_zero(self):
        """Rent some bikes on hourly basis"""
        self.assertEqual(self.bk.rentBikeOnHourly(0, self.dt), False)
    
    def test_rentBikeOnHourly_for_number_positive(self):
        """Rent some bikes on hourly basis"""
        self.assertEqual(self.bk.rentBikeOnHourly(2, self.dt), True)

    def test_rentBikeOnHourly_for_number_positive_big_than_bike(self):
        """Rent some bikes on hourly basis"""
        self.assertEqual(self.bk.rentBikeOnHourly(101, self.dt), False)

    # On Daily
    def test_rentBikeOnDaily(self):
        """Rent some bikes on Daily basis"""
        self.assertEqual(self.bk.rentBikeOnDaily(-1, self.dt), False)
    
    def test_rentBikeOnDaily_for_number_negative(self):
        """Rent some bikes on Daily basis"""
        self.assertEqual(self.bk.rentBikeOnDaily(-1, self.dt), False)
    def test_rentBikeOnDaily_for_zero(self):
        """Rent some bikes on Daily basis"""
        self.assertEqual(self.bk.rentBikeOnDaily(0, self.dt), False)

    def test_rentBikeOnDaily_for_number_positive(self):
        """Rent some bikes on Daily basis"""
        self.assertEqual(self.bk.rentBikeOnDaily(2, self.dt), True)
    
    def test_rentBikeOnDaily_for_number_positive_big_than_bike(self):
        """Rent some bikes on Daily basis"""
        self.assertEqual(self.bk.rentBikeOnDaily(101, self.dt), False)
    
    # On Weekly

    def test_rentBikeOnWeekly(self):
        """Rent some bikes on Weekly basis"""
        self.assertEqual(self.bk.rentBikeOnWeekly(-1, self.dt), False)
    
    def test_rentBikeOnWeekly_for_number_negative(self):
        """Rent some bikes on Weekly basis"""
        self.assertEqual(self.bk.rentBikeOnWeekly(-1, self.dt), False)
    
    def test_rentBikeOnWeekly_for_zero(self):
        """Rent some bikes on Weekly basis"""
        self.assertEqual(self.bk.rentBikeOnWeekly(0, self.dt), False)
    
    def test_rentBikeOnWeekly_for_number_positive(self):
        """Rent some bikes on Weekly basis"""
        self.assertEqual(self.bk.rentBikeOnWeekly(2, self.dt), True)
    
    def test_rentBikeOnWeekly_for_number_positive_big_than_bike(self):
        """Rent some bikes on Weekly basis"""
        self.assertEqual(self.bk.rentBikeOnWeekly(101, self.dt), False)
    
    def test_returnBike(self):
        """Return a Bike"""
        self.assertEquals(self.bk.returnBike(), )