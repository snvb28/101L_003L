########################################################################
##
## CS 101 Lab
## Program #7
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that reads through and outputs files containing fuel economy information on select vehicles.
##
## ALGORITHM:
##      1. Program asks the user to enter in the desired minimum mpg amount.
##      2. If the entered value is not a number, greater than 0, or less than 100, the user is asked to enter in a new amount.
##      3. The user is asked to enter in a valid txt file name to take information from. If the entered file name is not found, the user is asked to enter it in again.
##      4. The user is asked to enter in a valid txt file name to create. If an invalid entry is inputed, the user is asked to enter it in again.
##      5. The program takes information from the first file and transfers it to the second file.
##
## ERROR HANDLING:
##           IOError exceptuon not triggered unless the input is empty.
##
## OTHER COMMENTS:
##          Was unable to convert information from input file to output with the min_mpg amount.
##
########################################################################

def get_min_mpg():
    while True:
        try:
            min_mpg = float(input('Enter the minimum mpg ==> '))
            if min_mpg <= 0:
                print('Fuel economy given must be greater than 0')
                
            elif min_mpg >= 100:
                print('Fuel economy must be less than 100')
                
            else:
                return min_mpg
        except ValueError:
            print('You must enter a number for the fuel economy')

def open_file(input_file):
    while True:
        try:
            input_file = input('Enter the name of the input vehicle file ==> ')
            file = open(input_file, 'r')
            return file
        except FileNotFoundError:
            print('Could not open file', input_file)
        except IOError:
            print('There is an IO Error', input_file)

def out_file(file, output_file):
    while True:
        try:
            output_file = input('Enter the name of the file to output to ==> ')
            file2 = open(output_file, 'w')
            for line in file:
                file2.write(line)
            return file2
        except IOError:
            print('There is an IO Error', output_file)



min_mpg = 0
get_min_mpg()
print()
input_file = ''
file = open_file(input_file)
file.readline()
print()
output_file = ''
file2 = out_file(file, output_file)

file.close()
file2.close()
