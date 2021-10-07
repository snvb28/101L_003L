########################################################################
##
## CS 101 Lab
## Program #5 (Week 5 Lab)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a Linda Hall library card numbering system for students.
##
## ALGORITHM:
##      1. User is asked to enter their library card number.
##      2. The program verifies if the length of the library card number is 10 characters. If not valid, user is prompted to enter library number again.
##      3. The program verifies if the first 5 characters are letters (A-Z). If not valid, user is prompted to enter library number again.
##      4. The program verifies if the last 3 characters are digits (0-9). If not valid, user is prompted to enter library number again.
##      5. The program verifies if the 6th character is 1, 2, or 3. If not valid, user is prompted to enter library number again.
##      6. The program verifies if the 7th character is 1, 2, 3, or 4. If not valid, user is prompted to enter library number again.
##      7. Once all verifications are passed, the program displays the student's school name and grade level.
##
## ERROR HANDLING:
##      ValueError: 'substring not found' when using the string.ascii_uppercase.index() with characters located in lib_card[6:9]. Different function was used. 
##
## OTHER COMMENTS:
##      Unable to successfully incorporate the get_check_digit function.
##
########################################################################

import string

def get_school(lib_card):
    if lib_card[5] == '1':
        print('This card belongs to a student in the School of Computing and Engineering SCE')
    elif lib_card[5] == '2':
        print('This card belongs to a student in the School of Law')
    elif lib_card[5] == '3':
        print('This card belongs to a student in the College of Arts and Sciences')
    else:
        return False

def get_grade(lib_card):
    if lib_card[6] == '1':
        print('This card belongs to a Freshman')
    elif lib_card[6] == '2':
        print('This card belongs to a Sophomore')
    elif lib_card[6] == '3':
        print('This card belongs to a Junior')
    elif lib_card[6] == '4':
        print('This card belongs to a Senior')
    elif lib_card[6] == '5':
        return False

def character_value(lib_card):
    for char in lib_card:
        value = ord(char)
        return value

def verify_check_digit(lib_card):
    i = 1
    while i != 0:
        if len(lib_card) != 10:
            return False, 'The length of the number given must be 10'
        elif not lib_card[0:5].isalpha():
            return False, 'The first 5 characters must be A-Z'
        elif not lib_card[7:9].isdigit():
            return False, 'The last 3 characters must be 0-9'
        elif lib_card[5] != '1' and lib_card[5] != '2' and lib_card[5] != '3':
            return False, 'The sixth character must be 1 2 or 3'
        elif lib_card[6] != '1' and lib_card[6] != '2' and lib_card[6] != '3' and lib_card[6] != '4':
            return False, 'The seventh character must be 1 2 3 or 4'
        else:
            i = 0
            return True
        
        
if __name__ == "__main__":

    title1 = 'Linda Hall'
    title2 = 'Library Card Check'

    x = title1.center(60)
    y = title2.center(60)
    print(x)
    print(y)
    print('='*60)
    print()
    
    
    lib_card = str(input('Enter Library. Hit Enter to Exit ==> '))

    while lib_card.isalnum():
        verify_check_digit(lib_card)
        val = 'valid'
        if verify_check_digit(lib_card) == True:
            print('Library card is', val)
            get_school(lib_card)
            get_grade(lib_card)
        elif verify_check_digit(lib_card) == (False, 'The length of the number given must be 10'):
            val = 'invalid'
            print('Library card is', val)
            print(verify_check_digit(lib_card))
        elif verify_check_digit(lib_card) == (False, 'The first 5 characters must be A-Z'):
            val = 'invalid'
            print('Library card is', val)
            print(verify_check_digit(lib_card))
        elif verify_check_digit(lib_card) == (False, 'The last 3 characters must be 0-9'):
            val = 'invalid'
            print('Library card is', val)
            print(verify_check_digit(lib_card))
        elif verify_check_digit(lib_card) == (False, 'The sixth character must be 1 2 or 3'):
            val = 'invalid'
            print('Library card is', val)
            print(verify_check_digit(lib_card))
        elif verify_check_digit(lib_card) == (False, 'The seventh character must be 1 2 3 or 4'):
            val = 'invalid'
            print('Library card is', val)
            print(verify_check_digit(lib_card))
        print()
        lib_card = str(input('Enter Library. Hit Enter to Exit ==> '))

