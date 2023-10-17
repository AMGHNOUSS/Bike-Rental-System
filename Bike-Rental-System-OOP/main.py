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

        choix = int(input("Your Choice:"))
        if choix == 1:
            rb.displaystock()
        elif choix == 2:
            dateRental = rb.rentBikeOnHourly(2)
        elif choix == 3:
            dateRental = rb.rentBikeOnDaily(3)
        elif choix == 4:
            dateRental = rb.rentBikeOnDaily(1)
        elif choix == 5:
            rb.returnBike(3, choix, dateRental)
        elif choix == 6:
            break