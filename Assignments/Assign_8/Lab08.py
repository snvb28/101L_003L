########################################################################
##
## CS 101 Lab
## Program #8
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that calculates and displays weighted test scores.
##
## ALGORITHM:
##      1. The grade menu is displayed with the options 1, 2, 3, 4, 5, 6, D, or Q.
##      2. The user is prompted to choose to either (1) add a test score, (2) remove a test score, (3) clear the test scores, (4) add a program score, (5) remove a program score, (6) clear the program scores
##          (D) display all the scores, or (Q) quit.
##      3. If option 1 is chosen, the user is asked to enter a test score, and that score is added to the tests list.
##      4. If option 2 is chosen, the user is asked to enter a test score, and that score is removed from the tests list.
##      5. If option 3 is chosen, all values in the tests list are removed.
##      6. If option 4 is chosen, the user is asked to enter a program score, and that score is added to the programs list.
##      7. If option 5 is chosen, the user is asked to enter a program score, and that score is removed from the programs list.
##      8. If option 6 is chosen, all values in the programs list are removed.
##      9. If option D is chosen, all of the test and program scores are displayed along with their minimum value, maximum value, mean, standard deviation, and final weighted grade.
##      10. If option Q is chosen, the program ends.
##
## ERROR HANDLING:
##          ValueErrors handled with exceptions.
##
## OTHER COMMENTS:
##          No additional comments.
##
########################################################################

import statistics

def get_minT(tests):
    try:
        minimumT = min(tests)
        return minimumT
    except ValueError:
        minimumT = 'N/A'
        return minimumT
    

def get_minP(programs):
    try:
        minimumP = min(programs)
        return minimumP
    except ValueError:
        minimumP = 'N/A'
        return minimumP
        
def get_maxT(tests):
    try:
        maximumT = max(tests)
        return maximumT
    except ValueError:
        maximumT = 'N/A'
        return maximumT

def get_maxP(programs):
    try:
        maximumP = max(programs)
        return maximumP
    except ValueError:
        maximumP = 'N/A'
        return maximumP
    
def get_meanT(tests):
    try:
        tests_avg = statistics.mean(tests)
        return '{:.2f}'.format(tests_avg)
    except statistics.StatisticsError:
        tests_avg = 'N/A'
        return tests_avg

def get_meanP(programs):
    try:
        programs_avg = statistics.mean(programs)
        return '{:.2f}'.format(programs_avg)
    except statistics.StatisticsError:
        programs_avg = 'N/A'
        return programs_avg

def get_stdT(tests):
    try:
        tests_std = statistics.stdev(tests)
        return '{:.2f}'.format(tests_std)
    except statistics.StatisticsError:
        tests_std = 'N/A'
        return tests_std

def get_stdP(programs):
    try:
        programs_std = statistics.stdev(programs)
        return '{:.2f}'.format(programs_std)
    except statistics.StatisticsError:
        programs_std = 'N/A'
        return programs_std

def get_grade():
    try:
        grade = (float(get_meanT(tests))*0.6) + (float(get_meanP(programs))*0.4)
        return grade
    except ValueError:
        grade = 0.00
        return grade

def display(countT, countP):
    print('Type', s*10, '#', s*5, 'min', s*5, 'max', s*5, 'avg', s*5, 'std')
    print('='*60)
    print('Tests', s*9, countT, s*5, get_minT(tests), s*6, get_maxT(tests), s*5, get_meanT(tests), s*5, get_stdT(tests))
    print('Programs', s*6, countP, s*5, get_minP(programs), s*6, get_maxP(programs), s*5, get_meanP(programs), s*5, get_stdP(programs))
    print()
    print('The weighted scores is', get_grade())
    
def grade_menu(title):
    print(title)
    print('-'*26)
    print('1 - Add Test Score')
    print('2 - Remove Test Score')
    print('3 - Clear Test Scores')
    print('4 - Add Assignment Score')
    print('5 - Remove Assignment Score')
    print('6 - Clear Assignment Scores')
    print('D - Display Scores')
    print('Q - Quit')
    
def actions(choice, tests, programs, run):
    if choice == '1':
        newTest = int(input('Enter a new Test score 0-100 ==> '))
        tests.append(newTest)
    elif choice == '2':
        removeTest = int(input('Enter a Test score to remove 0-100 ==> '))
        if removeTest in tests:
            tests.remove(removeTest)
        else:
            print('Could not find that score to remove.')
    elif choice == '3':
        tests.clear()
    elif choice == '4':
        newAssign = int(input('Enter a new Assignment score 0-100 ==> '))
        programs.append(newAssign)
    elif choice == '5':
        removeAssign = int(input('Enter an Assignment score to remove 0-100 ==> '))
        if removeAssign in programs:
            programs.remove(removeAssign)
        else:
            print('Could not find that score to remove.')
    elif choice == '6':
        programs.clear()
    elif choice == 'D':
        display(countT, countP)

    elif choice == 'Q':
        quit()
        run = 0


if __name__ == "__main__":

    options = ['1', '2', '3', '4', '5', '6', 'D', 'Q']
    tests = []
    programs = []
    s = ' '
    countT = 0
    countP = 0
    run = 1

    while run == 1:
        print()
        title_text = 'Grade Menu'
        title = title_text.center(25)
        grade_menu(title)
        print()
        choice = input('==> ')
        actions(choice, tests, programs, run)

        countT = len(tests)
        countP = len(programs)
        get_minT(tests)
        get_minP(programs)
        get_maxT(tests)
        get_maxP(programs)
