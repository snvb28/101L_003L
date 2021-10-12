########################################################################
##
## CS 101 Lab
## Program #6 (Week 6 Lab)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that runs the Caesar Cipher, encoding and decoding a cipher.
##
## ALGORITHM:
##      1. The user is prompted to either encode a string (option1), decode a string (option2), or quit the program (option3).
##      2. If options 1 or 2 are selected, the user is asked to enter a line of text. If option 3 is selected, the program ends.
##      3. The user is asked for the desired shift value for their text input.
##      4. During encoding, each character's value of the user's inputed text increases by the user's shift value.
##      5. During decoding, each character's value of the user's inputed text decreases by the user's shift value.
##      6. The new encrypted/decrypted text is displayed.
##      7. Program returns to Step 1.
##      
## ERROR HANDLING:
##          No additional error handling.      
##
## OTHER COMMENTS:
##          Did not utilize the string module or .find() function.
##
########################################################################

def encrypt(string_text, int_key) -> str:
    en_text = ''
    for char in string_text:
        if char == ' ':
            en_text = en_text + char
        elif char.isupper():
            en_text = en_text + chr((ord(char) + int_key - 65) % 26 + 65)
        else:
            en_text = en_text + chr((ord(char) + int_key - 97) % 26 +97)
    print('Encrpyted: '+en_text.upper())
    print()
    main()

def decrypt(string_text, int_key) -> str:
    de_text = ''
    for char in string_text:
        if char == ' ':
            de_text = de_text + char
        elif char.isupper():
            de_text = de_text + chr((ord(char) - int_key - 65) % 26 + 65)
        else:
            de_text = de_text + chr((ord(char) - int_key - 97) % 26 + 97)
    print('Decrpyted: '+de_text.upper())
    print()
    main()

def get_input()->str:
    selection = input('Enter your selection ==> ')
    print()
    if selection == '1':
        string_text = input('Enter (brief) text to encrypt: ')
        int_key = int(input('Enter the number to shift letters by: '))
        encrypt(string_text, int_key)
    elif selection == '2':
        string_text = input('Enter (brief) text to decrypt: ')
        int_key = int(input('Enter the number to shift letters by: '))
        decrypt(string_text, int_key)
    elif selection == 'Q':
        exit()
    else:
        print('Not a valid input, please enter your selection again.')
        main()

def print_menu():
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('3) Quit')


def main():
    
    print_menu()
    get_input()

    
main()