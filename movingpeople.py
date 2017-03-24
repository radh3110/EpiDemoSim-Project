from variables import *

def move(index, reg):
    if reg == 1:            #if region value is one than move to  Workplace 1
        people[index][0] = random.randrange(workplace1X1, workplace1X2 + 1)  #assign the agent x and y coordinates between the constrained value of place
        people[index][1] = random.randrange(workplace1Y1, workplace1Y2 + 1)
    elif reg == 2:          #if region value is two than move to Workplace 2
        people[index][0] = random.randrange(workplace2X1, workplace2X2 + 1)
        people[index][1] = random.randrange(workplace2Y1, workplace2Y2 + 1)
    elif reg == 3:          #if region value is three than move to Residential area in Region 2
        people[index][0] = random.randrange(region2ResidentialX1, region2ResidentialX2 + 1)
        people[index][1] = random.randrange(region2ResidentialY1, region2ResidentialY2 + 1)

    elif reg == 5:          #if region value is five than move to School in Region 1
        people[index][0] = random.randrange(schoolR1X1, schoolR1X2 + 1)
        people[index][1] = random.randrange(schoolR1Y1, schoolR1Y2 + 1)
    elif reg == 6:          #if region value is six than move to School in Region 2
        people[index][0] = random.randrange(schoolR2X1, schoolR2X2 + 1)
        people[index][1] = random.randrange(schoolR2Y1, schoolR2Y2 + 1)

    elif reg == 7:          #if region value is seven than move to Hospital of Region 1
        people[index][0] = random.randrange(hospitalR1X1, hospitalR1X2 + 1)
        people[index][1] = random.randrange(hospitalR1Y1, hospitalR1Y2 + 1)
    elif reg == 8:          #if region value is eight than move to Hospital 1 of Region 2
        people[index][0] = random.randrange(hospital1R2X1, hospital1R2X2 + 1)
        people[index][1] = random.randrange(hospital1R2Y1, hospital1R2Y2 + 1)
    elif reg == 9:          #if region value is nine than move to Hospital 2 of Region 2
        people[index][0] = random.randrange(hospital2R2X1, hospital2R2X2 + 1)
        people[index][1] = random.randrange(hospital2R2Y1, hospital2R2Y2 + 1)
    if reg == 10 :          #if region value is ten than move to Market place of Region 1
        people[index][0] = random.randrange(marketR1X1, marketR1X2 + 1)
        people[index][1] = random.randrange(marketR1Y1, marketR1Y2 + 1)
    else :                  #else move to Market place of Region 2
        people[index][0] = random.randrange(marketR2X1, marketR2X2 + 1)
        people[index][1] = random.randrange(marketR2Y1, marketR2Y2 + 1)





