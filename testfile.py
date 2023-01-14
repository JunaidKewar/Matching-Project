import csv

listDict = [
{ 'Software development':0, 'Core':1, 'Finance':2, 'Consultancy':3, 'ML/AI':4 },
{ 'Research groups':0, 'Technical societies':1, 'Cells':2, 'Fests':3, 'Cultural societies':4, 'Miscellaneous societies/clubs':5 },
{ 'Research':0, 'Corporate':1, 'Start-up':2, 'MBA':3, 'UPSC':4 },{ 'Hindi':0, 'Malayalam':1, 'Bengali':2, 'Tamil':3, 'Telugu':4 }
]

def rowInfo(row):
    print(row)
    for i in range(0,len(row)):
        indexList = [] #stores the ticked option value shown in dictionary
        zeroArray = [0]*len(listDict[i])

        # If only single option is ticked
        if ';' not in row[i]:
            index = listDict[i][row[i]]
            indexList.append(index)
        
        # if multiple options are ticked
        else:
            breakpoints = [0]
            loopNumber = 0
            # finding number of ';' breakpoints
            for k in row[i]:
                if k==';':
                    breakpoints.append(loopNumber)
                loopNumber += 1
            # seperating the string according to the breakpoints
            for n in range(0,len(breakpoints)):
                # print (n)
                if (n==0):
                    indexList.append(listDict[i][row[i][breakpoints[n]:breakpoints[n+1]]])
                elif (n<len(breakpoints)-1):
                    indexList.append(listDict[i][row[i][breakpoints[n]+1:breakpoints[n+1]]])
                else:
                    indexList.append(listDict[i][row[i][breakpoints[n]+1:]])
        
        # converting the 0's in the array to 1's according to the options ticked
        for j in indexList:
            zeroArray[j] = 1
        print(zeroArray)

def loadcsv():
    with open('Questionnaire.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                rowInfo(row[1:])

loadcsv()
