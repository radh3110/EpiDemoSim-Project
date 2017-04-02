import random
from variables import *

#we are diving susceptibility into 4 parts : 0, s/3, 2s/3 and lastly  s.  Let each represent 4 values ie 0,1,2 and 3 respectively.
# len here represents at what length the value will drop down to. Here from 3 to 2.
def measure2(array,size,length , len):  # measure2 ie reduction of susceptibility from s to 2s/3. Delay here we are considering as 50, len = 2
    for i in range(0, size):
        randnum = random.random()       # generate a random number
        low =  prob[array[i][6]][1] + prob[array[i][6]][0]   #assign probability values for low and high
        #here low and high would maintain a upper and lower limit of the probability so that the susceptibility is reduced at that point
        high = prob[array[i][6]][2] + prob[array[i][6]][1] + prob[array[i][6]][0]
        if low < randnum <= high and array[i][15] != 1:      #if low < randnum <= high and agent is not infected
                array[i][8] = len * (array[i][7] / length)  #reduce the susceptibility to 2s/3
                array[i][14] = array[i][8]                  #assign susceptibility as diminished susceptibility
                lowered[array[i][6]][len] += 1              #number of peple whose susceptibility is lowered at that 'len' level is incremented


def measure1(array,size, length, len):  # measure1 ie reduction of susceptibility from s to s/3 or from 2s/3 to s/3. Delay here we are considering as 80, len = 1
    for i in range(0, size):
            randnum = random.random()     #generate a random number
            low = prob[array[i][6]][0]   #assign probability values for low and high
            #here low and high would maintain a upper and lower limit of the probability so that the susceptibility is reduced at that point
            high = prob[array[i][6]][1] + prob[array[i][6]][0]
            if low < randnum <= high and array[i][15] != 1: #if low < randnum <= high and agent is not infected
                array[i][8] = len * (array[i][7] / length)  # reduce the susceptibility to s/3
                array[i][14] = array[i][8]                  #assign susceptibility as dimninshed susceptibility
                lowered[array[i][6]][len] += 1              #number of peple whose susceptibility is lowered at that 'len' level is incremented



def measure0(array,size, length , len):   # measure0 ie reduction of susceptibility from s to 0 or from 2s/3 to 0 or from s/3 to 0. Delay here we are considering as 100, len = 0
    for i in range(0, size):
        randnum = random.random()         #generate a random number
        low = 0                           #assign low value as 0
        high = prob[array[i][6]][0]       #assign high value as probability value at zero of agent bearing that awareness level
        if low < randnum <= high and array[i][15] != 1:     #if low < randnum <= high and agent is not infected
                array[i][8] = len * (array[i][7] / length)  #reduce susceptibility to 0, or in other words vaccinate the individual
                array[i][14] = array[i][8]                  #assign susceptibility as dimninshed susceptibility
                lowered[array[i][6]][len] += 1              #number of peple whose susceptibility is lowered at that 'len' level is incremented


