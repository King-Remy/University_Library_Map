from csv import DictReader




# def new_data_dict:
#     new_data_dict = {}

#     file_handler1 = open("Subject_classmark.csv", "r", encoding="utf8")
#     csv_handler1 = DictReader(file_handler1)

#     file_handler2 = open("Location_classmark3.csv", "r", encoding="utf8")
#     csv_handler2 = DictReader(file_handler2)

#     for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
#         subject, classmark = subject_classmark
#         loc_classmark1, location = classmark_location
#         new_data_dict[classmark] = {subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']} 
#     return new_data_dict

# print(new_data_dict)

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
new_data_dict = {}
def searchresult(param, search): 
    

    file_handler1 = open("Subject_classmark.csv", "r", encoding="utf8")
    csv_handler1 = DictReader(file_handler1)

    file_handler2 = open("Location_classmark3.csv", "r", encoding="utf8")
    csv_handler2 = DictReader(file_handler2)

    for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
        subject, classmark = subject_classmark
        loc_classmark1, location = classmark_location
        new_data_dict[classmark] = {subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']}

        for key in new_data_dict:
            if param == 1:
                if search in new_data_dict[key]["Subject"]:
                    print('Related Subject: ' + new_data_dict[key]["Subject"] + ' -----> Related Classmark: ' + new_data_dict[key]["Classmark"] + ' -----> Related Location: ' + new_data_dict[key]["Location"])

            elif param == 2:
                if search in new_data_dict[key]["Classmark"]:
                    print('Related Subject: ' + new_data_dict[key]["Subject"] + ' -----> Related Classmark: ' + new_data_dict[key]["Classmark"] + ' -----> Related Location: ' + new_data_dict[key]["Location"])
            
            elif param == 3:
                if search in new_data_dict[key]["Location"]:
                    print('Related Subject: ' + new_data_dict[key]["Subject"] + ' -----> Related Classmark: ' + new_data_dict[key]["Classmark"] + ' -----> Related Location: ' + new_data_dict[key]["Location"])


def getSubjectNames():

    subject_names = []
    # Read the CSV file and send it to the 
    new_data_dict = {}

    csv_handler1 = DictReader(file_handler1)
    csv_handler2 = DictReader(file_handler2)

    for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
        subject, classmark = subject_classmark
        loc_classmark1, location = classmark_location
        new_data_dict[classmark] = {subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']}
        
        for subjectName in new_data_dict:
            allSubjectName = new_data_dict[subjectName]['Subject']
            subject_names.append(allSubjectName)

def getClassMarks():

    class_marks = []
    # Read the CSV file and send it to the 
    new_data_dict = {}

    csv_handler1 = DictReader(file_handler1)
    csv_handler2 = DictReader(file_handler2)

    for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
        subject, classmark = subject_classmark
        loc_classmark1, location = classmark_location
        new_data_dict[classmark] = {subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']}
        
        for subjectName in new_data_dict:
            allSubjectName = new_data_dict[subjectName]['Classmark']
            class_marks.append(allSubjectName)

    
    return class_marks

def getLocation():

    Location = []
    # Read the CSV file and send it to the 
    new_data_dict = {}

    csv_handler1 = DictReader(file_handler1)
    csv_handler2 = DictReader(file_handler2)

    for subject_classmark, classmark_location in zip(csv_handler1,csv_handler2):
        subject, classmark = subject_classmark
        loc_classmark1, location = classmark_location
        new_data_dict[classmark] = {subject: subject_classmark['Subject'], loc_classmark1: classmark_location['Classmark'], location: classmark_location['Location']}
        
        for subjectName in new_data_dict:
            allSubjectName = new_data_dict[subjectName]['Classmark']
            Location.append(allSubjectName)

    
    return Location

# print(getSubjectNames())
# print(new_data_dict)

# getSubjectNames()

main()

searchresult(userChoice, userInput)

# TO DO:
# 1. Using regex, make the user have option of inputing the first letter with capital or small letter for subject name, class mark or location 
# 2. Add option to select again if no response is given after being prompt to enter subject name, classmark or location
# 3. Make code more modular. Use more defined functions to ensure code is decoupled.