########################################################################
##
## CS 101 Lab
## Program #9
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that reads and displays Kansas City Police Crime Data from csv files.
##
## ALGORITHM:
##      1. The user is asked to enter in the name of a crime data file.
##      2. If the file is not found, the user is prompted to re-enter another crime data file.
##      3. The program displays the months with the highest number of crimes.
##      4. The program displays the offense with the highest number of occurances.
##      5. The user is asked to enter an offense.
##      6. If the offense is not found, the user is prompted to enter another offense.
##      7. The program displays the number of times the offense was commited at each zip code.
##
## ERROR HANDLING:
##          Errors handled with exceptions.
##
## OTHER COMMENTS:
##          Unable to incorporate create_offense_by_zip function.
##
########################################################################

import csv

def month_from_number(user_int):
    try:
        if user_int == 1:
            return months[0]
        elif user_int == 2:
            return months[1]
        elif user_int == 3:
            return months[2]
        elif user_int == 4:
            return months[3]
        elif user_int == 5:
            return months[4]
        elif user_int == 6:
            return months[5]
        elif user_int == 7:
            return months[6]
        elif user_int == 8:
            return months[7]
        elif user_int == 9:
            return months[8]
        elif user_int == 10:
            return months[9]
        elif user_int == 11:
            return months[10]
        elif user_int == 12:
            return months[11]
        else:
            print('Month must be 1-12')
    except ValueError:
        print('Month must be 1-12')

def read_in_file(filename, dataList):
    file = open(filename, encoding='utf-8')
    csvFile = csv.reader(file)
    for line in csvFile:
        data = [line[1], line[7], line[13]]
        dataList.append(data)
    return dataList

def create_reported_date_dict(dataList, keyList, keyDates):
    x = 1
    while x in range(len(dataList)):
        keyList.append(dataList[x][0])
        x += 1
    for key in keyList:
        if key in keyDates:
            keyDates[key] = keyDates[key] + 1
        else:
            keyDates[key] = 1
    return keyDates

def create_reported_month_dict(keyList, JanKey, FebKey, MarKey, AprKey, MayKey, JunKey, JulKey, AugKey, SepKey, OctKey, NovKey, DecKey):
    for index in keyList:
        month = index.split('/')
        if month[0] == '01':
            JanKey.append(month[0])
        elif month[0] == '02':
            FebKey.append(month[0])
        elif month[0] == '03':
            MarKey.append(month[0])
        elif month[0] == '04':
            AprKey.append(month[0])
        elif month[0] == '05':
            MayKey.append(month[0])
        elif month[0] == '06':
            JunKey.append(month[0])
        elif month[0] == '07':
            JulKey.append(month[0])
        elif month[0] == '08':
            AugKey.append(month[0])
        elif month[0] == '09':
            SepKey.append(month[0])
        elif month[0] == '10':
            OctKey.append(month[0])
        elif month[0] == '11':
            NovKey.append(month[0])
        elif month[0] == '12':
            DecKey.append(month[0])

def create_offense_dict(dataList, keylistO, keyOffenses):
    x = 1
    while x in range(len(dataList)):
        keyListO.append(dataList[x][1])
        x += 1
    for key in keyListO:
        if key in keyOffenses:
            keyOffenses[key] = keyOffenses[key] + 1
        else:
            keyOffenses[key] = 1
    return keyOffenses

#def create_offense_by_zip(dataList, keyListOZ, keyOffZip):
#    x = 1
#    while x in range(len(dataList)):
#        keyListOZ.append(dataList[x][1:3])
#        x += 1
#    for key in keyListOZ:
#        if key in keyOffZip:
#            keyOffZip[key] = keyOffZip[key] + 1
#        else:
#            keyOffZip[key] = 1
#    return keyOffZip

def chart(dataList, offense):
    print(offense, 'offenses by Zip Code')
    print('{:<5} {:>21}'.format('Zip Code', '# of Offenses'))
    print('='*30)
    print()

if __name__ == "__main__":

    run = 1
    while run == 1:
        try:
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            filename = input('Enter the name of the crime data file ==> ')
            print()

            dataList = []
            read_in_file(filename, dataList)
            keyList = []
            keyDates = {}
            create_reported_date_dict(dataList, keyList, keyDates)
            
            JanKey = []
            FebKey = []
            MarKey = []
            AprKey = []
            MayKey = []
            JunKey = []
            JulKey = []
            AugKey = []
            SepKey = []
            OctKey = []
            NovKey = []
            DecKey = []
            create_reported_month_dict(keyList, JanKey, FebKey, MarKey, AprKey, MayKey, JunKey, JulKey, AugKey, SepKey, OctKey, NovKey, DecKey)
            JanCount = len(JanKey)
            FebCount = len(FebKey)
            MarCount = len(MarKey)
            AprCount = len(AprKey)
            MayCount = len(MayKey)
            JunCount = len(JunKey)
            JulCount = len(JulKey)
            AugCount = len(AugKey)
            SepCount = len(SepKey)
            OctCount = len(OctKey)
            NovCount = len(NovKey)
            DecCount = len(DecKey)
            keyMonths = {'January':JanCount, 'February':FebCount, 'March':MarCount, 'April':AprCount, 'May':MayCount, 'June':JunCount, 'July':JulCount, 'August':AugCount, 'September':SepCount, 'October':OctCount, 'November':NovCount, 'December':DecCount}

            keyListO = []
            keyOffenses = {}
            create_offense_dict(dataList, keyListO, keyOffenses)

            mostMon = max(keyMonths, key=keyMonths.get)
            print('The month with the highest # of crimes is', mostMon, 'with', keyMonths.get(mostMon), 'offences')
            mostOff = max(keyOffenses, key=keyOffenses.get)
            print('The offense with the highest # of crimes is', mostOff, 'with', keyOffenses.get(mostOff), 'offences')
            print()
            while True:
                offense = input('Enter an offense ==> ')
                if offense not in keyListO:
                    print('Offense not found. Please try again.')
                    continue
                else:
                    break
            print()

            keyListOZ = []
            keyOffZip = {}
            chart(dataList, offense)
            run = 0

        except FileNotFoundError:
            print('Could not find '+filename+'. '+'Please enter file name again.')
        