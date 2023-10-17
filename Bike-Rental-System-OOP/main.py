#!/usr/bin/python3
from BikeRental import BikeRental
# The main program.
if __name__ == "__main__":
    rb = BikeRental()
    while True:
        print("1- See available bikes on the shop")
        print("2- Rent bikes on hourly basis $5 per hour.")
        print("3- Rent bikes on daily basis $20 per day.")
        print("4- Rent bikes on weekly basis $60 per week.")
        print("5- Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price")
        print("6- Exit")
        print()

        result = int(input("Your Choice:"))
        if result == 1:
            rb.displaystock()
        elif result == 2:
            rb.rentBikeOnHourly(2)
        elif result == 3:
            rb.rentBikeOnDaily(3)
        elif result == 4:
            rb.rentBikeOnDaily(1)
        elif result == 5:
            pass
        elif result == 6:
            break