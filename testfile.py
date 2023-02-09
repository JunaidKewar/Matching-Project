import csv
import math
from pprint import pprint
import pandas as pd

listDict = [{'AE':0, 'AG':1, 'AR':2, 'BT':3, 'CH':4, 'CY':5, 'CE':6, 'CS':7, 'EE':8, 'EC':9, 'EX':10, 'GG':11, 'HS':12, 'IM':13, 'IE':14, 'ME':15, 'MT':16, 'MI':17, 'MA':18, 'MF':19, 'NA':20, 'PH':21},
{ 'Software development':0, 'Core':1, 'Finance':2, 'Consultancy':3, 'ML/AI':4, 'Management':5 },
{ 'Research groups':0, 'Technical societies':1, 'Cells':2, 'Fests':3, 'Cultural societies':4, 'Miscellaneous societies/clubs':5, 'None':6 },
{ 'Research':0, 'Corporate':1, 'Start-up':2, 'MBA':3, 'UPSC':4, 'Other':5 },
{ 'English':0, 'Hindi/ Urdu':1, 'Malayalam':2, 'Bengali':3, 'Tamil':4, 'Telugu':5 },
{ 'Chess':0, 'Bridge':1, 'Football':2, 'Cricket':3, 'Hockey':4, 'Basketball':5, 'Squash':6, 'Volleyball':7, 'Tennis':8, 'Table Tennis':9, 'Badminton':10, 'Athletics':11, 'Other':12 }, 
{ 'Religious Philosophy (Dealing with Philosophical arguments for existence of God in light of the Quran, Understanding the wisdom behind our Moral stances. Refuting all the “isms”(athiesm, liberalism etc.) using application of classical Aqeedah.)':0, 'Moral Code (Dealing with islamic laws and their understanding in different scenarios)':1, 'The miracles of Quran (Exploring literary patterns and trends of the Quran which are impossible for a human mind or AI to generate. Exploring the scientific acuteness of the Quran)':2, 'History (Trying to relive the Good and Bad parts of Islamic History)':3, '':4 },
{ 'Public speaking':0, 'Writing':1, 'Design/Presentation':2,'Management/Leadership':3, 'Other':4},
{'':0}]

newDict = [{'No':0, 'Yes':1}]*46
listDict.extend(newDict)

# pprint(listDict)

def calcList(Dmatrix,k,M,m,dum):
    finalList = [[] for _ in range(len(Dmatrix))]
    for x in range(M):
        for y in range(m+dum):
            Dmatrix[x][y]=float(Dmatrix[x][y])
    for z in range(k):
        for x in range(M):
            minIndex = Dmatrix[x].index(min(Dmatrix[x]))
            if minIndex < m:
                finalList[x].append([x,minIndex])
            for y in range(M):
                Dmatrix[y][minIndex] = 2
    return finalList



def calcDmatrix(studentCData, mentorsCData, M, m,dummyDvalue):
    dOuterMatrix=[]
    for x in range(M):
        dInnerMatrix=[] 
        for y in range(m):
            d = calcDvalue(studentCData[y], mentorsCData[x])
            format_float = "{:.3f}".format(d)
            dInnerMatrix.append(format_float)
        for _ in range(dummyDvalue):
            dInnerMatrix.append(1.000)
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
        if i==8:
            continue
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
            # pprint(row)
            row = row[4:12] + row[13:]
            rowInfo(row, CData)
        # print(CData)
        return CData


def main(csvfile1, csvfile2):
    # csvfile = 'Questionnaire_Mentees.csv'
    studentCData = preprocess(csvfile1)
    # csvfile = 'Questionnaire_Mentors.csv'
    mentorsCData = preprocess(csvfile2)
    pprint(studentCData)
    print()
    pprint(mentorsCData)
    print()

    mentee_n = len(studentCData)
    mentor_n = len(mentorsCData)
    k = math.ceil(mentee_n/mentor_n)
    # dummyDvalue is the number of dummy students added so that the value of k is integer
    dummyDvalue = (k*mentor_n) - mentee_n
    print(k)
    
    Dmatrix = calcDmatrix(studentCData,mentorsCData,mentor_n, mentee_n,dummyDvalue)
    print(Dmatrix,'\n')

    masterList = calcList(Dmatrix,k,mentor_n,mentee_n,dummyDvalue)
    pprint(masterList)

    df = pd.DataFrame(masterList)
    df.to_csv('mapping.csv', index=False, header=False)

if __name__ == "__main__":
    
    main('Questionnaire_Mentees 2.0.csv','Questionnaire_Mentors 2.0.csv')