import random
import os
import time

board = """

43 | 44 | 45 | 46 | 47 | 48 | 49
36 | 37 | 38 | 39 | 40 | 41 | 42
29 | 30 | 31 | 32 | 33 | 34 | 35
22 | 23 | 24 | 25 | 26 | 27 | 28
15 | 16 | 17 | 18 | 19 | 20 | 21
08 | 09 | 10 | 11 | 12 | 13 | 14
01 | 02 | 03 | 04 | 05 | 06 | 07

"""

def diceroll():
    roll = random.randint(1,6)
    return (roll)


user1 = str(input("What will be player 1's username: "))

user2 = str(input("What will be player 2's username: "))
