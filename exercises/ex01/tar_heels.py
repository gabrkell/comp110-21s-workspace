"""An exercise in remainders and boolean logic."""

__author__ = "730230246"

number = int(input("Enter an int:"))
if number % 2 == 0:
    if number % 2 == 0 and number % 7 == 0:
        print("TAR HEELS") 
    else: 
        print("TAR")
else:
    if number % 7 == 0: 
        print("HEELS")
    else: 
        print("CAROLINA")