import csv
from pprint import pprint

listDict = [    { 'Software development':0, 'Core':1, 'Finance':2, 'Consultancy':3, 'ML/AI':4 },    { 'Research groups':0, 'Technical societies':1, 'Cells':2, 'Fests':3, 'Cultural societies':4, 'Miscellaneous societies/clubs':5 },    { 'Research':0, 'Corporate':1, 'Start-up':2, 'MBA':3, 'UPSC':4 },{ 'Hindi':0, 'Malayalam':1, 'Bengali':2, 'Tamil':3, 'Telugu':4 }]

def calcDvalue(mentor, student):
    commonValue = 0
    for x in range(0,len(mentor)):
        for y in range(0,len(mentor[x]):
            if (mentor[x][y] == mentee[x][y]):
                commonValue += 1
    print commonValue
    return commonValue


def rowInfo(row, CData):
    data = []
    for i, options in enumerate(row):
        index_list = [] 
        zero_array = [0] * len(listDict[i])

        if ';' not in options:
            index = listDict[i][options]
            index_list.append(index)
        
        else:
            options = options.split(";")
            for option in options:
                index_list.append(listDict[i][option])

        for j in index_list:
            zero_array[j] = 1
        
        data.append(zero_array)
    CData.append(data)


def preprocess(csvfile):
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        CData = []
        next(csv_reader)
        for row in csv_reader:
            rowInfo(row[1:], CData)
        return CData

if __name__ == "__main__":
    csvfile = 'Response_Mentees.csv'
    studentCData = preprocess(csvfile)
    pprint(studentCData)

    csvfile = 'Response_Mentors.csv'
    mentorsCData = preprocess(csvfile)
    pprint(mentorsCData)

    calcDvalue(studentCData[3], mentorsCData[0])
