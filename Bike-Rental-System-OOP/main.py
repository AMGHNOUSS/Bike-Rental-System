#!/usr/bin/python3
from BikeRental import BikeRental
from Customer import Customer
import os
import time

# The main program.
if __name__ == "__main__":
    rb = BikeRental()
    cus = Customer()
    listCustomer = []
    while True:
        print()
        print("\t ============= Bike rental shop ==============")
        print("\t| 1- See available bikes on the shop          |")
        print("\t| 2- Rent bikes on hourly basis $5 per hour.  |")
        print("\t| 3- Rent bikes on daily basis $20 per day.   |")
        print("\t| 4- Rent bikes on weekly basis $60 per week. |")
        print("\t| 5- Return a bike.                           |") 
        print("\t| 6- Exit.                                    |")
        print("\t =============================================")
        print()

        choix = int(input("Your Choice: "))
        if choix == 1:
            rb.displaystock()
        elif choix == 2:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnHourly(customer['bikes'], customer['rentalTime'])
        elif choix == 3:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnDaily(customer['bikes'], customer['rentalTime'])
        elif choix == 4:
            customer = cus.requestBike(choix)
            listCustomer.append(customer)
            rb.rentBikeOnWeekly(customer['bikes'], customer['rentalTime'])
        elif choix == 5:
            print(listCustomer)
            rem = cus.returnBike(listCustomer)
            listCustomer.pop(rem[0])
            rb.returnBike(rem[1], rem[2], rem[3])
        elif choix == 6:
            break
        else:
            print("Number incorrect")
            print()
        input("Tape eny button.")
        os.system('cls' if os.name == 'nt' else 'clear')