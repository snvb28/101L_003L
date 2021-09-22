########################################################################
##
## CS 101 Lab
## Program #3 (Week 3 Lab)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that will guess a user inputted number based on a series of questions asking whether that number, when divided by 3, has remainders of certain values. 
##
## ALGORITHM: 
##      1. The program will prompt the user to think of a number between and including 1 to 100.
##      2. The user is asked to enter the value of the remainder of the number when divided by 3. The value must be 0, 1, or 2, if not, this step is repeated.
##      3. The user is asked to enter the value of the remainder of the number when divided by 5.
##      4. The user is asked to enter the value of the remainder of the number when divided by 7.
##      5. The program finds a number between and including 1 and 100 that contains those 3 remainders when dividing by 3, 5, and 7 respectively.
##      6. The number is displayed along with a message of amazement.
##      7. The user is asked if they want to play again; user may answer with 'Y' or 'N'. If anything else is entered, this step repeats. 
##      8. If the user responds with 'Y', the program starts over with step 1. If the user responds with 'N', the program ends.
## 
## ERROR HANDLING:
##      Common SyntaxErrors (parentheses placements); solved after revision.
##
## OTHER COMMENTS:
##      No additional comments.
##
########################################################################

print('Welcome to the Flarsheim Guesser!')
print()

play_again = 'Y'


while play_again == 'Y':
    print('Please think of a number between and including 1 and 100.')
    print()
    while play_again == 'Y':
        rem_3 = int(input('What is the remainder when your number is divided by 3? '))
        if rem_3 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif rem_3 > 3:
            print('The value entered must be less than 3')
            continue
        else:
            print()
            rem_5 = int(input('What is the remainder when your number is divided by 5? '))
            print()
            rem_7 = int(input('What is the remainder when your number is divided by 7? '))
            break

    for i in range(0,101):
        if i % 3 == rem_3 and i % 5 == rem_5 and i % 7 == rem_7:
            print('Your number was', i)
            print('How amazing is that?')
            play_again = input('Do you want to play again? Y to continue, N to quit ==> ')
            if play_again == 'Y':
                print()
                continue
            elif play_again == 'N':
                break
            while play_again != 'Y' and play_again != 'N':
                play_again = input('Do you want to play again? Y to continue, N to quit ==> ')

