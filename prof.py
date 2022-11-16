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
        new_data_dict.append({subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']})
    return new_data_dict

# print(finalTable())

def main():
    menuInput()

def menu():
    menuDisplay = print('''
    Welcome! Please make a choice from the following menu:
    1. Subject Name
    2. Classmark
    3. Location
''')

def menu2():
    menuDisplay = print('''
    Welcome! Please make a choice from the following menu:
    1. Top Floor Back Left
    2. Top Floor Back Right
    3. Top Floor Front Left
    4. Top Floor Front Right
    5. Middle Floor
    3. Ground Floor
''')

def menu3():
    menuDisplay = print('''
    Please select Back to try again:
    1. Back    
''')

def menuInput():
    global userChoice, userInput
    
    while True:
        menu()
        try:
            userChoice = int(input("Please make a selection: "))
            if not 1 <= userChoice <=3:
                menu3()
                userChoice = int(input("Please enter: "))
        except:
            pass
        
        
        if userChoice == 1:
            userInput = input("Please enter a Subject Name: ")
            return userInput
        elif userChoice == 2:
            userInput = input("Please enter a Classmark: ")
            return userInput
        elif userChoice == 3:
            menu2()
            userInput = input("Please make a selection: ")
            return userInput
        # elif len(userInput) == 0:
        #     menu3()
        #     input("Please enter: ")
        #     userChoice = input("Please enter a valid input: ")
        # else:
        #     error = ''
        #     if len(userInput) == 0:
        #         error = "Error: no data was typed yet"
        #     print(error)
        #     menu3()

def searchresult(param, search):
    Results = []
    for value in finalTable():
        if param == "Subject Name":
            if search in value['Subject']:
                # print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Classmark":
            if search in value['Classmark']:
                # print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append(value['Subject'] +','+ value['Classmark'].replace(',', ' ') +',' + value['Location'])
        elif param == "Location":
            if search in value['Location']:
                # print('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
                Results.append('Related Subject: ' + value['Subject'] + ' -----> Related Classmark: ' + value['Classmark'] + ' -----> Related Location: ' + value['Location'])
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

# print(getClassMarks())
# print(getSubjectNames())
# print(new_data_dict)

# print(getLocations())
if __name__ == '__main__':
    main()
    for value in searchresult(userChoice, userInput):
        print(value)

# TO DO:
# 1. Using regex, make the user have option of inputing the first letter with capital or small letter for subject name, class mark or location 
# 2. Add option to select again if no response is given after being prompt to enter subject name, classmark or location
# 3. Make code more modular. Use more defined functions to ensure code is decoupled.