import csv
import math
from pprint import pprint

listDict = [    { 'Software development':0, 'Core':1, 'Finance':2, 'Consultancy':3, 'ML/AI':4 },    { 'Research groups':0, 'Technical societies':1, 'Cells':2, 'Fests':3, 'Cultural societies':4, 'Miscellaneous societies/clubs':5 },    { 'Research':0, 'Corporate':1, 'Start-up':2, 'MBA':3, 'UPSC':4 },{ 'Hindi':0, 'Malayalam':1, 'Bengali':2, 'Tamil':3, 'Telugu':4 }]

def calcList(Dmatrix,k,M,m):
    finalList = [[] for _ in range(len(Dmatrix))]
    for x in range(M):
        for y in range(m):
            Dmatrix[x][y]=float(Dmatrix[x][y])
    for z in range(k):
        for x in range(M):
            minIndex = Dmatrix[x].index(min(Dmatrix[x]))
            finalList[x].append([x,minIndex])
            for y in range(M):
                Dmatrix[y][minIndex] = 1
    return finalList


def calcDmatrix(studentCData, mentorsCData, M, m):
    dOuterMatrix=[]
    for x in range(M):
        dInnerMatrix=[] 
        for y in range(m):
            d = calcDvalue(studentCData[y], mentorsCData[x])
            format_float = "{:.3f}".format(d)
            dInnerMatrix.append(format_float)
        dOuterMatrix.append(dInnerMatrix)
        # dInnerMatrix.clear()
    return dOuterMatrix

def calcDvalue(mentor, student):
    intersectionValue = 0
    z=0
    for x in range(0,len(mentor)):
        for y in range(0,len(mentor[x])):
            if (mentor[x][y] == student[x][y]):
                intersectionValue += 1
            z += 1
    # print (intersectionValue)
    unionValue = (2*z)-intersectionValue
    # print (unionValue)
    return (intersectionValue/unionValue)

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
    csvfile = 'Response_Mentors.csv'
    mentorsCData = preprocess(csvfile)
    pprint(studentCData)
    print()
    pprint(mentorsCData)
    print()

    mentee_n = len(studentCData)
    mentor_n = len(mentorsCData)
    k = math.ceil(mentee_n/mentor_n)
    # print(k)
    
    Dmatrix = calcDmatrix(studentCData,mentorsCData,mentor_n, mentee_n)
    print(Dmatrix,'\n')

    masterList = calcList(Dmatrix,k,mentor_n,mentee_n)
    pprint(masterList)