import random
from variables import *

def flagraised(array,size, prob, length):
    for i in range(0, size):
        randnum = random.random()    #generate a random number
        low = 0                      #lower probability value
        high = prob[array[i][6]][0]  #higher probability value ie probability value of that agent bearing that awareness level, is taken as input
        for w in range(0, length):
            if low < randnum <= high:   #if random number lies between low and high, including high
                array[i][8] = w * (array[i][7] / length)  #agent will have a diminshed susceptibility value ie suceptibility will drop from s to which length value w is at
                array[i][14] = array[i][8]
                lowered[array[i][6]][w] += 1              #number of peple whose susceptibility is lowered at that w level is incremented
                break
            else:
                low = high            #if not then low is assigned value previously stored by high
                if (w != length - 1): #uptil w does not cross the length constraint
                    high += prob[array[i][6]][w + 1]
