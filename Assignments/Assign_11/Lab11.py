########################################################################
##
## CS 101 Lab
## Program #11
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that uses a class to create a clock that can keep track of hours, minutes, and seconds.
##
## ALGORITHM:
##      1. The user is asked to choose the clock format.
##      2. The user is prompted to enter the hour(s), minute(s), and second(s).
##      3. If a ValueError occurs, the user is prompted to re-enter the hour(s), minute(s), and second(s).
##      4. The clock is displayed with the time running.
##
## ERROR HANDLING:
##          Errors handled with exceptions.
##
## OTHER COMMENTS:
##          Unable to incorporate tick method in Clock class, tick located in main instead.
##          Only able to incorporate AM and PM labels in the 24hr format.
##
########################################################################

import time

class Clock:

    def __init__(self, hour, minute, second, Ctype=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.Ctype = Ctype

    def __str__(hour, minute, second, Ctype):
        if Ctype == 0:
            if hour > 12:
                hour = 1
                print('{:02}:{:02}:{:02}'.format(hour, minute, second))
            else:
                print('{:02}:{:02}:{:02}'.format(hour, minute, second))
        elif Ctype == 1:
            if hour > 24:
                hour = 1
                print('{:02}:{:02}:{:02} AM'.format(hour, minute, second))
            else:
                if (hour == 1) or (hour == 2) or (hour == 3) or (hour == 4) or (hour == 5) or (hour == 6) or (hour == 7) or (hour == 8) or (hour == 9) or (hour == 10) or (hour == 11) or (hour == 24):
                    print('{:02}:{:02}:{:02} AM'.format(hour, minute, second))
                elif (hour == 13) or (hour == 14) or (hour == 15) or (hour == 16) or (hour == 17) or (hour == 18) or (hour == 19) or (hour == 20) or (hour == 21) or (hour == 22) or (hour == 23):
                    print('{:02}:{:02}:{:02} PM'.format(hour, minute, second))


def main():

    run = 1
    subRun = 1
    while run == 1:
        try:

            while subRun == 1:
                Ctype = int(input('Choose clock format (0) 12hr (1) 24hr ==> '))
                if Ctype == 0 or Ctype == 1:
                    subRun = 0
                    break
                else:
                    print('Please choose option 0 or 1')
        
            hour = int(input('Enter the current hour ==> '))
            minute = int(input('Enter the current minute ==> '))
            second = int(input('Enter the current second ==> '))

            run = 0
            
        except ValueError:
            print('Please enter valid values')
        
    while True:
        Clock.__str__(hour, minute, second, Ctype)
        if second < 60:
            second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1

main()
