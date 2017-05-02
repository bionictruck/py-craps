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
dice_1 = 0
dice_2 = 0
payout = Decimal('0.00')

def bet():
    global wallet
    global wager
    global odds
    odds = 0
    wager = 0
    os.system('clear')
    if wallet < 5:
        print("You're don't have enough money! You finished with only $" + str(wallet))
        print("See you next time!")
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
    global dice_1
    global dice_2
    global point_set
    os.system('clear')
    print(u"\U0001F3B2" + "   Rolling... " + u"\U0001F3B2")
    time.sleep(1)
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    if point_set == False:
        roll_out_result()
    else:
        point_result()

def roll_out_result():
    global wallet
    global wager
    global point
    global dice_1
    global dice_2
    global point_set
    global odds
    if dice_1 + dice_2 == 2 or dice_1 + dice_2 == 3 or dice_1 + dice_2 == 12 and point_set == False:
        print(str(dice_1 + dice_2) + " has been rolled. You lose. Sorry.")
        wallet -= wager
        rebet()
    elif dice_1 + dice_2 == 7 or dice_1 + dice_2 == 11 and point_set == False:
        print(str(dice_1 + dice_2) + " has been rolled. WINNER!")
        wallet += wager
        print("You now have " + str(wallet) + ".")
        rebet()
    elif point_set == False:
        point = dice_1 + dice_2
        point_set = True
        print("The point is now " + str(point) + ".")
        odds_bet()

def odds_bet():
    global odds
    global wager
    take_odds = input("Would you like to bet up to 2X $" + str(wager) + " to take the odds bet? Y/N?")
    if take_odds.lower() == 'y' or take_odds.lower() == 'yes':
        odds = input("Place your odds bet (Up to 2X $" + str(wager) + ") $")
        try:
            odds = int(odds)
        except Exception:
            print("Invalid entry. Enter a bet up to 2X $" + str(wager))
            odds_bet()
        if odds <= wager * 2:
            rolling()
        elif int(odds) > int(wager) * 2:
            print("You can only bet up to 2X $" + str(wager))
            odds_bet()
    elif take_odds.lower() == 'n' or take_odds.lower() == 'no':
        rolling()
    else:
        print("Invalid entry. Please use Y or N.")
        time.sleep(1)
        os.system('clear')
        odds_bet()
    

def point_result():
    global wallet
    global wager
    global point
    global dice_1
    global dice_2
    global point_set
    global odds
    global payout
    print("The point is " + str(point) + ".")
    print(str(dice_1 + dice_2) + " has been rolled.")
    if point == dice_1 + dice_2:
        print("The point has been hit! You win $" + str(wager) + " on the Pass Line bet!")
        wallet += wager
        if int(odds) > 0:
            if point == 4 or point == 10:
                payout = Decimal((int(odds) * 2))
                print("Your odds bet pays 2:1. You win $" + str(payout) + "!")
                wallet += Decimal((int(odds) * 2))
            elif point == 5 or point == 9:
                payout = Decimal((int(odds) * 3 / 2))
                print("Your odds bet pays 3:2. You win $" + str(payout) + "!")
                wallet += Decimal((int(odds) * 3 / 2))
            elif point == 6 or point == 8:
                payout = Decimal((int(odds) * 6 / 5))
                print("Your odds bet pays 6:5. You win $" + str(payout) + "!")
                wallet += Decimal((int(odds) * 6 / 5))
            rebet()
        else:
            rebet()
    elif dice_1 + dice_2 == 7:
        print("Seven out! You lose your Pass Line bet of $" + str(wager) + ".")
        wallet -= wager
        if int(odds) > 0:
            print("You lose your odds line bet of $" + str(odds) + ".")
            wallet -= Decimal(odds)
        point_set = False
        rebet()
    else:
        print("Your bet(s) are not affected.")
        roll_again()

def rebet():
    global point_set
    global wallet
    point_set = False
    bet_again = input("Would you like to bet again? Y/N? ")
    if bet_again.lower()== "y" or bet_again.lower() == "yes":
        bet()
    elif bet_again.lower() == "n" or bet_again.lower() == "no":
        print("You finished with $" + str(wallet) + ".")
        print("See you next time!")
        quit()
    else:
        print("Invalid entry. Please enter Y or N.")
        rebet()

def roll_again():
    again = input("Would you like to roll again? Y/N? ")
    if again.lower() == "y" or again.lower() == "yes":
        rolling()
    elif again.lower() == "n" or again.lower() == "no":
        print("You finished with $" + str(wallet) + ".")
        print("See you next time!")
        quit()
    else:
        print("Invalid entry. Please enter Y or N.")
        roll_again()

bet()