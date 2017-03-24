from variables import *

#Probabilistic equation for Recovery of an Individual is given by:
#pr = 1 - [(1-(1/rT))^iT]
#where:
#rT is the recovery time
#iT is the time after which the agent is infected


def recoveringPeople(array, index):
    recovered1 = 0
    removed1 = 0
    var = 1 - (1.0/recoveryTime)
    for p in range(0, index):
        if array[p][15] == 1 and array[p][16] > 1:     #if the agent is infected and iT is greater than 1
            array[p][17] = 1 - pow(var, array[p][16])  #Probability to recover is given as
            temp1 = random.random()    #generate  a random number temp
            if temp1 < array[p][17]:   #if temp is less than probability to recover
                array[p][15] = -1      #than agent recovers
                recovered1 = recovered1 + 1
            if (array[p][16] >= recoveryTime and array[p][15] != -1):   #if iT is greater than or equal to rT and if agent has still not recovered
                array[p][15] = -2      #then agent is removed
                removed1 = removed1 + 1
                print array[p][18], "is removed\n"

    temparray = [recovered1, removed1]

    return temparray