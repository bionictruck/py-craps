#### A craps game in python
### Dice - u"\U0001F3B2"

import os
import random
import time
from decimal import Decimal

wallet = Decimal('100.00')
wager = 0
odds = 0
point_set = False
point = 0
rolled = 0

def bet():
    global wallet
    global wager
    os.system('clear')
    if wallet <= 0:
        print("You're out of money! See you next time!")
        quit()
    else:
        print("You have $" + str(wallet) + " to play with.")
        try:
            wager = Decimal(input("Place a bet between $5 and $" + str(wallet) + " $"))
        except Exception:
            print("Invalid entry. Please enter a bet between $5 and $" + str(wallet))
            time.sleep(2)
            bet()
        if wager < 5:
            print("You bet must be at least $5.")
            time.sleep(2)
            bet()
        elif wager > wallet:
            print("You don't have enough money! Enter a bet less than $" + str(wallet))
            time.sleep(2)
            bet()
        else:
            rolling()


def rolling():
    global wallet
    global rolled
    global point_set
    print(u"\U0001F3B2" + "   Rolling... " + u"\U0001F3B2")
    rolled = random.randrange(2, 13)
    if point_set == False:
        roll_out_result()
    else:
        point_result()

def roll_out_result():
    global wallet
    global wager
    global point
    global rolled
    global point_set
    global odds
    if rolled == 2 or rolled == 3 or rolled == 12 and point_set == False:
        print("A " + str(rolled) + " has been rolled. You lose. Sorry.")
        wallet -= wager
        rebet = input("Would you like to bet again? Y/N? ")
        if rebet.lower()== "y" or rebet.lower() == "yes":
            bet()
        elif rebet.lower() == "n" or rebet.lower() == "no":
            print("See you next time!")
            quit()
    elif rolled == 7 or rolled == 11 and point_set == False:
        print("A " + str(rolled) + " has been rolled. WINNER!")
        wallet += wager
        print("You now have " + str(wallet) + ".")
        again = input("Would you like to roll again? Y/N? ")
        if again.lower() == "y" or again.lower() == "yes":
            bet()
        elif again.lower() == "n" or again.lower() == "no":
            print("See you next time!")
            quit()
    elif point_set == False:
        point = rolled
        point_set = True
        print("The point is now " + str(point) + ".")
        odds_bet = input("Would you like to bet up to 2X $" + str(wager) + " to take the odds bet? Y/N?")
        if odds_bet.lower() == 'y' or odds_bet.lower() == 'yes':
            odds = input("Place your odds bet (Up to 2X $" + str(wager) + ") $")
            rolling()
        elif odds_bet.lower() == 'n' or odds_bet.lower() == 'no':
            rolling()
    

def point_result():
    global wallet
    global wager
    global point
    global rolled
    global point_set
    print("The point is " + str(point) + ".")
    print(rolled)


bet()