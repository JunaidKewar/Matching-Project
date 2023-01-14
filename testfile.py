import csv

listDict = [
{ 'Software development':0, 'Core':1, 'Finance':2, 'Consultancy':3, 'ML/AI':4 },
{ 'Research groups':0, 'Technical societies':1, 'Cells':2, 'Fests':3, 'Cultural societies':4, 'Miscellaneous societies/clubs':5 },
{ 'Research':0, 'Corporate':1, 'Start-up':2, 'MBA':3, 'UPSC':4 },{ 'Hindi':0, 'Malayalam':1, 'Bengali':2, 'Tamil':3, 'Telugu':4 }
]

listQ = [[],[],[],[]]

def rowInfo(row):
    print(row)
    for i in range(0,len(row)):
        zeroArray = [0]*len(listDict[i])
        index = listDict[i][row[i]]
        zeroArray[index] = 1
        listQ[i].append(zeroArray)
        print(listQ[i])

def loadCsv(): 
    with open('Questionnaire.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                rowInfo(row[1:])
                line_count += 1
        # print(f'Processed {line_count} lines.')

loadCsv()
