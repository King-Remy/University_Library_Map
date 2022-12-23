'''
FIlename: 21027699
AUthor: King Remy Igbokwe
Date: 17/12/2022

Keele University Library program that stores the following information:
Subject, Classmark, Location

User can search any subject, classmark or location in the Library
'''

from csv import DictReader

def finalTable():           # Method for returning a list containing a dictionary containing Subject Name, Classmark, Location
    try:
        new_data_dict = []

        # Reading CSVs
        file_handler1 = open("Subject_Classmark.csv", "r", encoding="utf8")
        csv_handler1 = DictReader(file_handler1)

        file_handler2 = open("Classmark_Location.csv", "r", encoding="utf8")
        csv_handler2 = DictReader(file_handler2)

        # merging csvs and forming a nested dictionary of containing subject name, classmark and location
        for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
            subject_col, classmark_col = subject_classmark
            loc_classmark_col, loc_location_col = classmark_location
            new_data_dict.append({subject_col: subject_classmark[f"{subject_col}"], classmark_col: classmark_location[f"{loc_classmark_col}"], loc_location_col: classmark_location[f"{loc_location_col}"]})
            
        return new_data_dict
    # Ensures hte right CSVs are uploaded
    except:
        print("Wrong file loaded")
        SystemExit

def getAllKeys(table):          # Method takes in dictionary table and returns the column headers Subject, Classmark, Location and 'Exit'
    keys = list(table[0].keys())

    keys.append('Exit')

    return keys

def getAllLocations(table):         # Method takes in dictionary table returns returns a list of all unique locations
    location = set()

    for locs in table:
        location.add(locs['Location'])
    return list(location)

def printKeyOptions(keys):           # Method takes in list of keys from dictionary table and prints it out in new lines
    index = 0
    select =''
    for option in keys:
        select += f'{index+1}. {option}\n'
        index = index +1
    print(select)

def printLocationOptions(loc):             # Method takes in list of keys from dictionary table and prints it out in new lines
    index = 0
    select = ''
    for location in loc:
        select +=f'{index+1}. {location}\n'
        index = index +1
    print(select)

def getSelectedLocation(index):         # Method returns the selected location 
    return getAllLocations(finalTable())[index-1]

def main():             # Method starts the Menu option
    menuInput()

def menuInput():            # Method prompts the user to select a subject name, classmark or a location
    retry = True
    while retry:
        print("Please make a selection: ")
        printKeyOptions(getAllKeys(finalTable()))       
        userChoice = int(input('-> '))

        if userChoice == 1:
            userInput = input("Please enter a Subject Name: ")
            # prints related classamrk and Location from selection 
            for value in searchresult(userChoice, userInput):
                print(f"\n'Subject: ' + {value.split(',')[0]} + ' || Classmark: ' + {value.split(',')[1]} + ' || Location: ' + {value.split(',')[2]}\n")

        elif userChoice == 2:
            userInput = input("Please enter a Classmark: ")
            # prints related subject name and Location from selection
            for value in searchresult(userChoice, userInput):
                print(f"\nSubject: {value.split(',')[0]} || Classmark: {value.split(',')[1]} || Location: {value.split(',')[2]}\n")

        elif userChoice == 3:
            printLocationOptions(getAllLocations(finalTable()))
            userInput = input("Please make a selection: ")
            # prints related Subject name and Classmark from selection
            location = getSelectedLocation(int(userInput))
            for value in searchresult(userChoice, location):
                print(f"\n'Subject: ' + {value.split(',')[0]} + ' || Classmark: ' + {value.split(',')[1]} + ' || Location: ' + {value.split(',')[2]}\n")
        
        elif userChoice == 4:
            # stops the iteratioin once 4. Exit is selected
            retry=False
            SystemExit
        else:
            # If any number out of range 1 - 4 is selected, below message presented
            print('invalid selection, please try again\n')

def searchresult(param, search):            # Method takes in user's selected search parameter and related search and returns a list of searched paramters
    Results = []
    for value in finalTable():
        if param == "Subject" or param == 1:
            if search.upper() in value['Subject'].upper():          # To accept lower case searches
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Classmark"  or param == 2:           # To accept lower case searches
            if search.upper() in value['Classmark'].upper():
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Location"  or param == 3:            # To accept lower case searches
            if search.upper() in value['Location'].upper():
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
    return Results

def getAllSubjectNames():          # Method returns a list of all subject name
    subject_names = []

    for subjectRow in finalTable():
        allSubjectName = subjectRow['Subject']
        subject_names.append(allSubjectName)
    return subject_names

def getAllClassMarks():            # Method returns a list of all classmark
    class_marks = []
    
    for classmarkRow in finalTable():
        allClassmark = classmarkRow['Classmark']
        class_marks.append(allClassmark)
    final_class_marks = [x for xs in class_marks for x in xs.split(',') ] # splits classmarks with ','
    return final_class_marks

def getLocations():         # Method returns a list of all unique locations
    location = set()

    for locs in finalTable():
        location.add(locs['Location'])
    return list(location)

if __name__ == '__main__':          # Prevents invoking the script when not ran
    main()