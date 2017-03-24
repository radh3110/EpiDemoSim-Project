import random
from infectionProbability import *

def initialinfection():
    for i in range(0, infected):     #for initially infected people assign random infectivity values
        people[infectedlist[i]][15] = 1
        people[infectedlist[i]][9] = random.randrange(1, levelsindisease+1)


def exposepeople(array, size):
    exposed1 = 0
    for p in range(0, size):
        if array[p][15] == 0:              #if an agent is not infected
            array[p][10] = calculateP(p)   #calculate the probability of getting infected
            temp = random.random()         #generate a random number 'temp'
            if temp < array[p][10]:        #if temp is less than probability to get infected
                array[p][15] = 2           #then Aagent is exposed to the infection
                exposed1 = exposed1 + 1
    return exposed1


def infectingPeople(array, size):
    infected1 = 0
    for p in range(0,size):
        if array[p][15] == 2:    #if agent is exposed
            array[p][26] += 1    #increment exposure time of agent
        if array[p][15] == 1 :   #if agent is infected
            array[p][16] += 1    #increment infection time of agent

        # if agent is exposed and exposed time is greater than latent period
        if array[p][15] == 2 and array[p][26] > latentperiod and array[p][9] == 0 :
            array[p][9] = random.randrange(1,levelsindisease+1)   #agent is assigned infectivity value randomly

        if(array[p][15] == 2 and array[p][26] > incubationPeriodstart):    #if agent is in exposed state and exposure time is greater than incubation period start
            willInfect = random.randrange(0,2)                             #generate a number either 0 or 1
            if(willInfect == 1 or array[p][26] == incubationPeriodend):    #if number is 1 or exposure time equals incubation period end
                array[p][15] = 1                                           #then agent becomes infected
                infected1 = infected1 + 1
                levels[array[p][6]] += 1

    return infected1

