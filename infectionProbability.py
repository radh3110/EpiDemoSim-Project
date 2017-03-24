from variables import *

import math


#probability of infecting a susceptible individual is given by:
        #pi =  1- exp(tau *(sigma)reR [Nr * ln(1-r*si*p)])
         #where:
            #tau is the duration of exposure
            #R is the set of infectivities of the infected individual at that location
            #Nr is the Number of infectious individual with infectivity r
            #si is the susceptibility of individual i
            #p is the transmissibility
            #(sigma) is summation

#The refernce for this formula is given in paper.

def calculateP(i):
    term = 0
    for l in range(0,levelsindisease):
        if coordinates[people[i][0]][people[i][1]][l] != 0 :
            t1 = ((l+1)/10.0) * people[i][14] * transmissibility  #r*si*p
            lnterm = math.log(1 - t1)   #ln(1-r*si*p)
            term += (coordinates[people[i][0]][people[i][1]][l] * lnterm)  #(sigma)reR [Nr * ln(1-r*si*p)]
    exponential = math.exp(term * people[i][4])   #exp(tau *(sigma)reR [Nr * ln(1-r*si*p)])
    return (1 - exponential)
