#!/usr/bin/python3

from BikeRental import BikeRental
import unittest

class BikeRentalTest():
    """Class Test For class BikeRental"""

    def test_displaystock(self):
        """Like 100 bikes"""
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)