from variables import *

def gotoHospi(array, i):
    peopletoHospi1 = 0
    willGo = random.random()  #generate a random number
    if array[i][25] == 0 and willGo < probabilitytoHospi:   #if hospital visits is zero and random number is less than probability to go to hospital
            array[i][25] = 1                                #then go to hospital
            peopletoHospi1 += 1
            whichHospi = random.randrange(1, 4)             #choose which hospital
            if (whichHospi == 1):
                array[i][0] = random.randrange(hospitalR1X1, hospitalR1X2 + 1)
                array[i][1] = random.randrange(hospitalR1Y1, hospitalR1Y2 + 1)
            elif (whichHospi == 2):
                array[i][0] = random.randrange(hospital1R2X1, hospital1R2X2 + 1)
                array[i][1] = random.randrange(hospital1R2Y1, hospital1R2Y2 + 1)
            else:
                array[i][0] = random.randrange(hospital2R2X1, hospital2R2X2 + 1)
                array[i][1] = random.randrange(hospital2R2Y1, hospital2R2Y2 + 1)
    if (array[i][25] == 1) and (array[i][27] < 3):    #if already in hospital and time spent in hospital is less than 3 hours
         array[i][27] += 1                            #then increment time
         if array[i][27] == 2:                        #if time spent in hospital equals 2 hours
            array[i][0] = array[i][23]                #then go back home
            array[i][1] = array[i][24]

    return peopletoHospi1
