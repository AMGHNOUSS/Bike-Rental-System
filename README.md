# A Bike Rental System 
A full fledged bike rental system implemented in Python using object oriented programming.

## Customers can 

* See available bikes on the shop
* Rent bikes on hourly basis $5 per hour.
* Rent bikes on daily basis $20 per day.
* Rent bikes on weekly basis $60 per week.
* Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

## The rental shops can

* issue a bill when customer decides to return the bike.
* display available inventory
* take requests on hourly, daily and weekly basis by cross verifying stock
  
Since classes are used various customers and bike rental shops can be instantiated as needed.

For simplicity we assume that any customer requests rentals of only one type i.e hourly, monthly or weekly but is free to chose the number of bikes he/she wants. However requested bikes should be less than available stock.

## Unit-Test

Test module is written alongside the main program to rigorously test the classes and methods for errors.
Most errors occur in Null values, negative values and non-integer inputs.
Most of them have been taken care of.

Incase of discrepancy please raise an issue or feel free to send pull requests.

## Running the tests

- Python 3.4+: `pytest bikeRental_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardle
ss of Python version):
`python -m pytest bikeRental_test.py`


## How to run?
This code is written in python3.6.

Simply run
``` 

python3 main.py
```