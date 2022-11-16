from csv import DictReader


file_handler2 = "Location_classmark3.csv"

def getSubjectName():

    subject_names = []
    # Read the CSV file and send it to the 
    file_handler1 = open("Subject_classmark.csv", "r", encoding="utf8")
 
    csv_handler = DictReader(file_handler1)

    for subjectName in csv_handler:
        subject_names.append(subjectName['Subject'])
    
    return subject_names

print(getSubjectName())



# def getSubjectName(file_handler1):

#     subject_names = []

#     # Read the CSV file and send it to the 
#     subject_file = open(file_handler1, "r", encoding="utf8")
 
#     csv_handler = DictReader(subject_file)

#     for subjectName in csv_handler:
#         subject_names.append(subjectName['Subject'])
    
#     return subject_names