########################################################################
##
## CS 101 Lab
## Program #10
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that reads words from a txt file and displays their frequencies of appearance.
##
## ALGORITHM:
##      1. The program asks the user to enter in a file name to open.
##      2. If the file is not found, the user is prompted to enter a new file name.
##      3. The program displays the Top 10 most frequently used words (words that contianed more than 3 letters) in the document.
##      4. The program displays the number of words that only appear once in the document.
##      5. The program displays the number of uniqie words in the document.
##
## ERROR HANDLING:
##          Errors handled through exceptions.
##
## OTHER COMMENTS:
##          No additional comments.
##
########################################################################

import string

def get_words(user_file, punctuation, wordsList):
    file = open(user_file)
    readFile = file.read().lower()
    words = readFile.split()
    for word in words:
        word = ''.join(char for char in word if char not in punctuation)
        if len(word) > 3:
            wordsList.append(word)
    return wordsList

def create_dict(wordsList, wordsKey, wordCount):
    x = 1
    while x in range(len(wordsList)):
        wordsKey.append(wordsList[x])
        x += 1
    for key in wordsKey:
        if key in wordCount:
            wordCount[key] = wordCount[key] + 1
        else:
            wordCount[key] = 1
    return wordCount

def get_top10_val(Top10Words, wordCount, Top10Values):
    x = 0
    while x in range(len(Top10Words)):
        key = Top10Words[x]
        val = wordCount[key]
        Top10Values.append(val)
        x += 1
    return Top10Values

def display_info(Top10Words, Top10Values):
    print()
    print('    Most Frequently Used Words')
    print('{:<5} {:>12} {:>15}'.format('#', 'Word', 'Freq.'))
    print('='*34)
    x = 0
    y = 1
    while x in range(len(Top10Words)):
        print('{:<5} {:>12} {:>15}'.format(y, Top10Words[x], Top10Values[x]))
        x += 1
        y += 1


if __name__ == "__main__":
    run = 1
    while run == 1:
        try:
            user_file = input('Enter the name of a file to open ==> ')
            
            wordsList = []
            punctuation = set(string.punctuation)
            get_words(user_file, punctuation, wordsList)
            
            wordCount = {}
            wordsKey = []
            create_dict(wordsList, wordsKey, wordCount)
            
            dictCount = sorted(wordCount, key=wordCount.get, reverse=True)
            Top10Words = dictCount[0:10]
            Top10Values = []
            get_top10_val(Top10Words, wordCount, Top10Values)
            
            count = []
            unique = len(wordsList)
            for key in wordCount:
                if wordCount[key] == 1:
                    count.append(key)
            oneApp = len(count)

            display_info(Top10Words, Top10Values)
            print()
            print('There are', unique, 'words that occur only once.')
            print('There are', oneApp, 'unique words in the document.')
            
            run = 0
        except FileNotFoundError:
            print('Could not find file', user_file)
            print('Please try again.')
            print()

        except IOError:
            print('Could not find file', user_file)
            print('Please try again.')
            print()
