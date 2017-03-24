from variables import *
import math

def calculatecost():
    initial = 0
    for z in range(0, population):
        drop = people[z][7] - people[z][8]  #drop in susceptibility is given as (natural susceptibility value - diminished susceptibility value)
        if drop > 0:    #if there is a drop
            index = int(length * (people[z][8] / people[z][7]))   #calculate index value
            initial += pow(costs[people[z][6]][index], power[people[z][6]])  #Total cost is given by sum of cost at that index raised to the power value for that index both taken a input from user

    return initial
