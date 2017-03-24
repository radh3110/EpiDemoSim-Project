from variables import *
from movingpeople import *

def gotoMarket(i, t):

    if people[i][28] == 0:                     #if not in market
        if t >= activehoursStart and t <= activehoursStop:   #if 9am <= current time <= 5pm
            probability = probtomarket         #prob to go to market is 0.05
        else:
            probability = probabilitytoMarket  #else 0.2
        if random.random() < probability:      #if random number is within the probability range
            people[i][28] = 1                  #go to market
            reg = random.randrange(10, 12)     #choose which market and go there
            move(i, reg)                       #and move within
            return 1
    elif people[i][28] == 1:                   #if already in market
        if random.random() < probtocomeback:   #Generate a random number. If random number is less than probability to come back
            people[i][0] = people[i][23]       #return to home
            people[i][1] = people[i][24]
            people[i][28] = -1
        else:                                  #if not than stay in market
            reg = random.randrange(10, 12)     #choose a marketplace
            move(i, reg)                       #and move within

    return 0

