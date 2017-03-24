from variables import *
from home_work_coordinates import *
from infecting import *
import xlsxwriter


def initialisation():
    workbook = xlsxwriter.Workbook('data.xlsx')  #writing data to excel sheet
    worksheet = workbook.add_worksheet()
    row = 1
    col = 0
    worksheet.write('A1', 'ID')         #18     #the numbers depicted here as comments are the corresponding property number assigned in variables.py
    worksheet.write('B1', 'Occupation') #3
    worksheet.write('C1', 'Education')  #5
    worksheet.write('D1', 'Level of awareness')     #6
    worksheet.write('E1', 'Natural Susceptibility') #7
    worksheet.write('F1', 'Infected?') #15
    worksheet.write('G1', 'Age')       #19
    worksheet.write('H1', 'Gender')    #20  0 female 1 male
    worksheet.write('I1', 'WorkX')     #21
    worksheet.write('J1', 'WorkY')     #22
    worksheet.write('K1', 'HomeX')     #23
    worksheet.write('L1', 'HomeY')     #24
    worksheet.write('M1', 'Place staying at present') #2
    worksheet.write('N1', 'Suceptibility')            #14
    worksheet.write('O1', 'Diminished Suceptibility') #8

    doctors = 0            #initializing to 0 first
    teachers = 0
    for i in range(0,3):
        alcount[i] = 0

    # sets home coordinates - 23,24
    makehouses1()    #for agents in Region1
    makehouses2()    #for agents in Region2

    for i in range(0, population):  # initialising some info
        alpeople10[i] = 0
        alpeople11[i] = 0
        alpeople12[i] = 0

        people[i][3] = 0                    #occupation

        randomnumber = random.random()   #generate a random number
        #assign education levels based on that random number
        #different critera for people in Region1 and Region2
        if i < people1:                                  #education levels 0 to 4 for people in Region1
            if randomnumber <0.5:
                people[i][5] = 0
            elif 0.5<= randomnumber < 0.7 :
                people[i][5] = 1
            elif 0.7<= randomnumber < 0.85 :
                people[i][5] = 2
            elif 0.85<= randomnumber < 0.95 :
                people[i][5] = 3
            else :
                people[i][5] = 4
        else:
            if randomnumber <0.1:                        #education levels 0 to 4 for people in Region2
                people[i][5] = 0
            elif 0.1<= randomnumber < 0.3 :
                people[i][5] = 1
            elif 0.3<= randomnumber < 0.5 :
                people[i][5] = 2
            elif 0.5<= randomnumber < 0.8 :
                people[i][5] = 3
            else :
                people[i][5] = 4

        people[i][18] = i                           #name of person
        people[i][19] = random.randrange(1, 101)    #age
        people[i][20] = random.randrange(0, 2)      #gender

        if people[i][20] == 0 and randomnumber < Probabilityforwomentostay :    #if gender is female and random number is less than prob for women to stay
            people[i][3] = 5    #assign occupation as 5 ie agents will stay at home
            if i < people1:
                # assign region staying at present
                people[i][2] = 0  #0 means Region1
            else:
                people[i][2] = 4  #people in Region2 Residential Area
        elif people[i][20] == 1 and randomnumber < probabilityformentostay:  #if gender is male and random number is less than prob for men to stay
            people[i][3] = 5      #assign  occupation as 5 ie agents will stay at home
            if i < people1:
                # assign region staying at present
                people[i][2] = 0     #0 means Region1
            else:
                people[i][2] = 4     #people in Region2 Residential Area
        else:
            setworkcordinates(i)   #set work cordinates


    #here we are assigning awareness levels to each individual depending upon certain criteria
    z0 = 0
    z1 = 0
    z2 = 0
    for i in range(0, population):
        #awareness level assigned is zero if any two of the following criteria are satisfied:
        # 1) if age is less than or equal to 10 or  greater than or equal to 70
        # 2) agent is from Region1
        # 3) its education level is less than 3
        if ((people[i][19] <= 10 or people[i][19] >= 70) and i < people1) or ((people[i][19] <= 10 or people[i][19] >= 70) and people[i][5] <= 2) or (i < people1 and people[i][5] <= 2):
            people[i][6] = 0  #then awareness level is 0
            alpeople10[z0] = i
            z0 += 1
        # if age is between 11 and 69 and agent is from Region 2 and its education level is greater than 2
        elif ((people[i][19] >= 11 or people[i][19] <= 69) and i > people1 and people[i][5] > 2):
            people[i][6] = 2  #then awareness level 2
            alpeople12[z2] = i
            z2 += 1
        else:
            people[i][6] = 1  #else awareness level is 1
            alpeople11[z1] = i
            z1 += 1
        alcount[people[i][6]] += 1
        people[i][7] = sus[people[i][6]]    # natural susceptibility of agent
        people[i][8] = people[i][7]         #initializing diminished susceptibility as natural susceptibility


    alist = random.sample(range(people1, population), doctorsguess)
    for i in range(0, doctorsguess):             # doctors
            if people[alist[i]][19] > doctorage and people[alist[i]][3] != 5 and people[alist[i]][5] != 0: #if age is greater than min doctor age and agent is not staying at home and education level is not zero
                people[alist[i]][3] = 2     #then he is a doctor
                people[alist[i]][14] = 0.1  #suceptibility value for doctors is 0.1
                doctors = doctors + 1
                whichPlace = random.randrange(1, 4)
                if whichPlace == 1:
                    people[alist[i]][21] = random.randrange(hospitalR1X1, hospitalR1X2 + 1)
                    people[alist[i]][22] = random.randrange(hospitalR1Y1, hospitalR1Y2 + 1)
                    people[alist[i]][2] = 7   #doctor assigned to hospital 1 of Region 1
                elif whichPlace == 2:
                    people[alist[i]][21] = random.randrange(hospital1R2X1, hospital1R2X2 + 1)
                    people[alist[i]][22] = random.randrange(hospital1R2Y1, hospital1R2Y2 + 1)
                    people[alist[i]][2] = 8   #doctor assigned to hospital 1 of Region 2
                else:
                    people[alist[i]][21] = random.randrange(hospital2R2X1, hospital2R2X2 + 1)
                    people[alist[i]][22] = random.randrange(hospital2R2Y1, hospital2R2Y2 + 1)
                    people[alist[i]][2] = 9  #doctor assigned to hospital 2 of Region 2
                alcount[people[alist[i]][6]] -= 1
                people[alist[i]][6] = 2
                alcount[people[alist[i]][6]] += 1
                alpeople12[z2] = i
                people[alist[i]][7] = sus[2]
                z2 += 1

    blist = random.sample(range(people1, population), teachersguess)
    for i in range(0, teachersguess):        #teachers
            if people[blist[i]][19] > teacherage and people[blist[i]][3] != 5 and people[blist[i]][5] != 0 and people[blist[i]][3] != 2:
                # if age is greater than min teacher age and agent is not staying at home and education level is not zero and agent is not a doctor
                people[blist[i]][3] = 1   #then agent is a teacher
                teachers = teachers + 1
                whichSchool = random.randrange(1, 3)
                if (whichSchool == 1):
                    people[blist[i]][21] = random.randrange(schoolR1X1, schoolR1X2 + 1)
                    people[blist[i]][22] = random.randrange(schoolR1Y1, schoolR1Y2 + 1)
                    people[blist[i]][2] = 5   #teacher assigned to school of Region 1
                elif (whichSchool == 2):
                    people[blist[i]][21] = random.randrange(schoolR2X1, schoolR2X2 + 1)
                    people[blist[i]][22] = random.randrange(schoolR2Y1, schoolR2Y2 + 1)
                    people[blist[i]][2] = 6  #teacher assigned to school of Region 2


    #write to worksheet
    for i in range (0, population):
        worksheet.write(row, col, people[i][18])      #ID of agent
        worksheet.write(row, col + 1, people[i][3])   #Occupation
        worksheet.write(row, col + 2, people[i][5])   #education level
        worksheet.write(row, col + 3, people[i][6])   #level of awreness
        worksheet.write(row, col + 4, people[i][7])   #natural susceptibility based on awareness level
        worksheet.write(row, col + 5, people[i][15])  #is Infected?
        worksheet.write(row, col + 6, people[i][19])  #Age
        worksheet.write(row, col + 7, people[i][20])  #Gender
        worksheet.write(row, col + 8, people[i][21])  #WorkX
        worksheet.write(row, col + 9, people[i][22])  #WorkY
        worksheet.write(row, col + 10, people[i][23]) #HomeX
        worksheet.write(row, col + 11, people[i][24]) #HomeY
        worksheet.write(row, col + 12, people[i][2])  #region staying at present
        worksheet.write(row, col + 13, people[i][14]) #Suceptibility
        worksheet.write(row, col + 14, people[i][8])  #Diminished Suceptibility
        row += 1

def secondinitialisation(parameter):
    gf = 0
    infected = 50
    gt = 0
    for i in range(0, population):    # initialising some info
        people[i][0] = people[i][23]  # x
        people[i][1] = people[i][24]  # y
        people[i][4] = 0              # duration of exposure
        people[i][9] = 0              # infectivity
        people[i][10] = 0             # probability of getting infected
        if parameter == 8:
            people[i][7] = sus[people[i][6]] / 3   #this is done for last strategy that we are considering
        people[i][14] = people[i][7]  # susceptibility
        people[i][15] = 0             # is infected?
        people[i][16] = 0             # time after the person is infected
        people[i][17] = 0             # probability to recover
        people[i][25] = 0             # hospital visits
        people[i][26] = 0             # exposed time
        people[i][27] = 0             # time spent in hospital
        people[i][28] = 0             # is in market?
    initialinfection()
    for i in range(0, 100):
        for k in range(0, 100):
            for v in range(0, levelsindisease):
                coordinates[i][k][v] = 0  # 3*3 matrix of x cord, y cord and levels in diseases
    for i in range(0, 3):
        levels[i] = 0
        for j in range(0,3):
            lowered[i][j] = 0 #initialising for counting suceptibility lowered people in each level