import csv


def subject(sub):
    with open("Subject_classmark.csv", 'r') as f:
        output = []
        reader = csv.reader(f)
        for row in reader:
            if sub in row[0]:
                output.append(row)
        return output

def classmark(classm):
    with open("Subject_classmark.csv", 'r') as f:
        output = []
        reader = csv.reader(f)
        for row in reader:
            if classm in row[1]:
                output.append(row)
        return output

def Location(loc):
    location = []
    with open('Location_classmark3.csv', 'r') as l:
        reader2 = csv.reader(l)
        for row in reader2:
            if loc in row[1]:
                location.append(row)
        return location

def LocationFile(cm):
    location = ''
    with open('Location_classmark3.csv', 'r') as l:
        reader2 = csv.reader(l)
        for row in reader2:
            if cm in row[0]:
                location = row[1]
        return location

def subjectFile(cm):
    with open("Subject_classmark.csv", 'r') as f:
        subject = ''
        reader = csv.reader(f)
        for row in reader:
            if cm in row[1]:
                subject = row[0]
        return subject

print(LocationFile('HD'))

search = input('What would you like to search with? ')
searchvalue = input('Enter the value you wnat to search for: ')

response = []
if search == 'Subject':
    for row in subject(searchvalue):
        row.append(LocationFile(row[1]))
        response.append(row)
    print(response)

elif search == 'Classmark':
    for row in classmark(searchvalue):
        row.append(LocationFile(row[1]))
        response.append(row)
    print(response)

elif search == 'Location':
    for row in Location(searchvalue):
        row.append(subjectFile(row[0]))
        response.append(row)
    print(response)