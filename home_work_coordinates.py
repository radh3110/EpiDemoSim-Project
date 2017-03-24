from variables import *
import random

# 21 - workX
# 22 - workY
# 23 - homeX
# 24 - homeY

def setworkcordinates(index):
    if people[index][19] > studentage:            #if age is greater than student age
        if index > people1:                       #if they are from Region 2
            people[index][3] = 3                  #occupation is 3
            whichPlace = random.randrange(1, 3)   #choose a workplace
            #people[index][2]  represents the place the agent will be staying at present
            #here after moving to workplace agent will be staying at that workplace assigned by given number
            if whichPlace == 1:
                people[index][21] = random.randrange(workplace1X1, workplace1X2 + 1)
                people[index][22] = random.randrange(workplace1Y1, workplace1Y2 + 1)
                people[index][2] = 1
            else:
                people[index][21] = random.randrange(workplace2X1, workplace2X2 + 1)
                people[index][22] = random.randrange(workplace2Y1, workplace2Y2 + 1)
                people[index][2] = 2
        else:
            whichPlace = random.randrange(1, 4)   #if agents are from  Region 1
            if whichPlace == 1:                   #choose a workplace
                people[index][21] = random.randrange(workplace1X1, workplace1X2 + 1)
                people[index][22] = random.randrange(workplace1Y1, workplace1Y2 + 1)
                people[index][3] = 3    #is an employee
                people[index][2] = 1
            elif whichPlace == 2:
                people[index][21] = random.randrange(workplace2X1, workplace2X2 + 1)
                people[index][22] = random.randrange(workplace2Y1, workplace2Y2 + 1)
                people[index][3] = 3
                people[index][2] = 2
            else:
                people[index][21] = random.randrange(region2ResidentialX1, region2ResidentialX2 + 1)
                people[index][22] = random.randrange(region2ResidentialY1, region2ResidentialY2 + 1)
                people[index][3] = 4          #Since some people from Region 1 may also be plumbers, servents etc, they are said to work in residential area.
                people[index][2] = 3
    else:                                     #if age is less than student age
        whichPlace = random.randrange(1, 3)   #choose a school
        if whichPlace == 1:
            people[index][21] = random.randrange(schoolR1X1, schoolR1X2 + 1)
            people[index][22] = random.randrange(schoolR1Y1, schoolR1Y2 + 1)
            people[index][2] = 5
        elif whichPlace == 2:
            people[index][21] = random.randrange(schoolR2X1, schoolR2X2 + 1)
            people[index][22] = random.randrange(schoolR2Y1, schoolR2Y2 + 1)
            people[index][2] = 6



def makehouses1():     #make houses for people in Region 1
    peoplecount = 0
    xstart = 0                  #starting x coordinate at 0
    ystart = hospitalR1Y2 + 1   #starting y coordinate at 6
    while peoplecount < people1:
        if xstart == X+1:
            ystart += 1
            xstart = 0
        count = 0
        number = random.triangular(4, 8, 6)
        # we are using traingular distribution to distribute people in each house.
        # So the minimum number of people in one house in Region 1 would be 4 and maximum would be 8 with a peak of 6
        while count < number and peoplecount < people1 :
           people[peoplecount][23] = xstart
           people[peoplecount][24] = ystart
           count += 1
           peoplecount += 1
        xstart += 1
    if ystart == Ymax + 1:
        print "Re-consider housing in rural area"


def makehouses2():     #make housees for people in Region 2
    peoplecount = people1
    xstart = region2ResidentialX1
    ystart = region2ResidentialY1
    while peoplecount < population:
        if xstart == region2ResidentialX2 + 1:
            ystart += 1
            xstart = region2ResidentialX1
        count = 0
        number = random.triangular(1, 6, 4)
        # Similarly as above, considering the triangular distribution, the minimum number of people in one house in Region 2 would be 1 and maximum would be 6 with a peak of 4
        while count < number  and peoplecount < population:
           people[peoplecount][23] = xstart
           people[peoplecount][24] = ystart
           count += 1
           peoplecount += 1
        xstart += 1
    if ystart == region2ResidentialY2 + 1:
        print "Re-consider housing in residential area"