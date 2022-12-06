from csv import DictReader

def finalTable():
    new_data_dict = []

    file_handler1 = open("Subject_classmark.csv", "r", encoding="utf8")
    csv_handler1 = DictReader(file_handler1)

    file_handler2 = open("Location_classmark3.csv", "r", encoding="utf8")
    csv_handler2 = DictReader(file_handler2)

    for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
        subject, classmark = subject_classmark
        loc_classmark1, location = classmark_location
        new_data_dict.append({subject: subject_classmark[f"{subject}"], classmark: classmark_location[f"{loc_classmark1}"], location: classmark_location[f"{location}"]})
        
    return new_data_dict
# print(finalTable())

def getAllKeys(table):
    keys = list(table[0].keys())

    # locations = list(set(table )
    return keys

def getAllLocations(table):
    keys = set()
    for locs in table:
        keys.add(locs['Location'])
    return list(keys)

print(getAllLocations(finalTable()))


def printKeyOptions(opt):
    index = 0
    select =''
    for option in opt:
        select += f'{index+1}. {option}\n'
        index = index +1
    print(select)

def printLocationOptions(loc):
    index = 0
    select = ''
    for location in loc:
        select +=f'{index+1}. {location}\n'
        index = index +1
    print(select)

def getselectedlocation(index):
    return getAllLocations(finalTable())[index-1]

#print(getselectedlocation(1))

def main():
    menuInput()

def menuInput():
    
    while True:
        printKeyOptions(getAllKeys(finalTable()))       
        try:
            userChoice = int(input("Please make a selection: "))
            if userChoice not in range(1,len(getAllKeys())):
                print('invalid selection, try again')
                userChoice = int(input("Please enter: "))
        except:
            pass
        
        
        if userChoice == 1:
            userInput = input("Please enter a Subject Name: ")
           # return userInput
            for value in searchresult(userChoice, userInput):
                print('Related Subject: ' + value.split(',')[0] + ' -----> Related Classmark: ' + value.split(',')[1] + ' -----> Related Location: ' + value.split(',')[2])

        elif userChoice == 2:
            userInput = input("Please enter a Classmark: ")
           # return userInput
            for value in searchresult(userChoice, userInput):
                print('Related Subject: ' + value.split(',')[0] + ' -----> Related Classmark: ' + value.split(',')[1] + ' -----> Related Location: ' + value.split(',')[2])

        elif userChoice == 3:
            printLocationOptions(getAllLocations(finalTable()))
            userInput = input("Please make a selection: ")
           # return userInput
            location = getselectedlocation(int(userInput))
            for value in searchresult(userChoice, location):
                print('Related Subject: ' + value.split(',')[0] + ' -----> Related Classmark: ' + value.split(',')[1] + ' -----> Related Location: ' + value.split(',')[2])



def searchresult(param, search):
    Results = []
    for value in finalTable():
        if param == "Subject Name" or param == 1:
            if search.upper() in value['Subject'].upper():
                #print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Classmark"  or param == 2:
            if search.upper() in value['Classmark'].upper():
               # print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Location"  or param == 3:
            if search.upper() in value['Location'].upper():
                #print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
    return Results


def getSubjectNames():
    subject_names = []

    for subjectRow in finalTable():
        allSubjectName = subjectRow['Subject']
        subject_names.append(allSubjectName)
    return subject_names

def getClassMarks():

    class_marks = []
    
    for classmarkRow in finalTable():
        allClassmark = classmarkRow['Classmark']
        class_marks.append(allClassmark)
    final_class_marks = [x for xs in class_marks for x in xs.split(',') ]
    # for Row in class_marks:
    #     classmarkRow = Row.split(",")
    return final_class_marks

def getLocations():

    location = []
    for locationRow in finalTable():
        allLocation = locationRow['Location']
        location.append(allLocation)
    
    return location

if __name__ == '__main__':
    main()

# TO DO:
# 1. add funciton to check if csv is the right one
# 2. complete error handling in menuinput() function
# 2. Change the 'Subject Name', 'Classmark' and 'Location' strings to the getAllKeys indexes. Ensure the text aligns with tkinter
# 4. update tkinter and add teh same error handling there.