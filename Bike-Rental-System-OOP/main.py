#!/usr/bin/python3
from BikeRental import BikeRental
from Customer import Customer
# The main program.
if __name__ == "__main__":
    rb = BikeRental()
    cus = Customer()
    listCustomer = []
    while True:
        print("\t=========== Bike rental shop ================")
        print("\t1- See available bikes on the shop")
        print("\t2- Rent bikes on hourly basis $5 per hour.")
        print("\t3- Rent bikes on daily basis $20 per day.")
        print("\t4- Rent bikes on weekly basis $60 per week.")
        print("\t5- Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price")
        print("\t6- Exit")
        print("\t===============================================")
        print()

        choix = int(input("Your Choice:"))
        if choix == 1:
            rb.displaystock()
        elif choix == 2:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnHourly(customer['bikes'])
        elif choix == 3:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnDaily(customer['bikes'])
        elif choix == 4:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnWeekly(customer['bikes'])
        elif choix == 5:
            pass
        elif choix == 6:
            break