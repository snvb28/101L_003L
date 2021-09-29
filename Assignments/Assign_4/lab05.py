########################################################################
##
## CS 101 Lab
## Program #4 (Week 4 Lab)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that simulates a slot machine located in Pierson Hall.
##
## ALGORITHM: 
##      1. User is asked to enter the amount of chips that they are starting the slots game with.
##      2. User is asked to enter the amount that they would like to wager. The amount must not exceed the starting amount.
##      3. The slot generates 3 reel values that are between 1 and 10 for each.
##      4. If all 3 reels match, the payout is given by multiplying the wager by 10 and subtracting by itself.
##         If 2 of the reels match, the payout is given by multiplying the wager by 3 and subtracting by itself.
##         If no reels match, the payout is the negative value of the wager.
##      5. The user is prompted the enter the wager amount until their bank amount is 0.
##      6. Once the bank amount is 0, the total loss is displayed along with the number of rounds played.
##      7. The highest total bank amount is displayed.
##      8. The user is promted to play again. The program ends if the user enters 'NO' or 'N'.
##         The program starts over if the user enters 'YES' or 'Y'.
## 
## ERROR HANDLING:
##      No Errors Prompted
##
## OTHER COMMENTS:
##      Was unable to write correct code on lines 130 and 131 to display total loss, matches, and highest amount. 
##
########################################################################

#import modules needed

import random

def play_again() -> bool:
    while True:
        play = input('Do you want to play again? ==> ')
        if play == 'Y' or play == 'YES':
            return True
        elif play == 'N' or play == 'NO':
            return False
        else:
            print()
            print('You must enter Y/YES/N/NO to continue. Please try again.')
            continue
    return True
     
def get_wager(bank : int) -> int:
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
            continue
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
            continue
        else:
            break
    return wager        

def get_slot_results() -> tuple:
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    matches = 0
    if reela == reelb:
        matches += 2
        if reela == reelc:
            matches += 1
    elif reela == reelc:
        matches += 2
        if reela == reelb:
            matches += 1
    elif reelb == reelc:
        matches += 2
        if reelb == reela:
            matches += 1
    return matches

def get_bank() -> int:
    while True:
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank >= 101:
            print('Too high a value, you can only choose 1 - 100 chips')
            continue
        elif bank <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            continue
        else:
            break
    return bank


def get_payout(wager, matches):
    if matches == 3:
        payout = (wager * 10) - wager
    elif matches == 2:
        payout = (wager * 3) - wager
    elif matches == 0:
        payout = wager * -1
    return payout


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", bank, "in", matches, "spins")
        print("The most chips you had was", bank)
        playing = play_again()
