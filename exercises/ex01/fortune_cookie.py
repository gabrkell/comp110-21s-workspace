"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730230246"

from random import randint
print("Your fortune cookie says...")
number: int = randint(1, 100)
Fortune_1 = str("You will succeed in this class.")
Fortune_2 = str("You will have a great day.")
Fortune_3 = str("You will have a happy life.")
Fortune_4 = str("You will be successful in life.")

if number >= 1: 
    if number <= 25:
        print(Fortune_1)
    else:
        if number <= 50:
            print(Fortune_2)
        else:      
            if number <= 75:
                print(Fortune_3)
            else:
                print(Fortune_4)
                
print("Now, go spread positive vibes!")