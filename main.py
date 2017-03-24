from strategy import *
from cost import *
from variables import *
from initialise import *
import xlrd
import numpy as np
from varassigning import *

#plottype = input("1.cumulative plots 2.instant plots. choice: ")
#we are reading input from a text file here. If you want kindly modify it to read from excel file.

plottype = 1

readfrom = open("input.txt", "r+") #reading input from text file

power[0] = int(readfrom.read(1))  #power value for people in awareness level 0
readfrom.read(1)
power[1] = int(readfrom.read(1))  #power value for people in awareness level 1
readfrom.read(1)
power[2] = int(readfrom.read(1))  #power value for people in awareness level 2
readfrom.read(1)

sus[0] = float(readfrom.read(5))  #initial susceptibility value for people in awareness level 0
sus[1] = float(readfrom.read(5))  #initial susceptibility value for people in awareness level 1
sus[2] = float(readfrom.read(5))  #initial susceptibility value for people in awareness level 2

for outer in range(0,3):
    for inner in range (0,length):
        costs[outer][inner] = float(readfrom.read(5))   #costs is taken as a matrix input where each value represents the different cost associated with individual to bring down the suceptibility value at that point

for outer in range(0,3):
    for inner in range (0,length):
        prob[outer][inner] = float(readfrom.read(5))   #probabilities are also taken as input wherein different probability values represent different strategies.

delay = int(readfrom.read(3))  #delay is stated as the time after which the government starts taking action.
readfrom.read(1)

varassigning()       #varassigning() is used as data representing agent's basic parameters like workX, workY, age, gender etc is already stored in excel file and we want to use the same data for different strategies
#initialisation()    #if you want to intialize the variables differently all together, use initialisation().

#use either of them as after initialisation the data gets stored in data.xlsx . If you want to use the same data for each simulation run and across strategies than comment initialisation() and use varassigning()
#if you want differnt data every time you run the simulation, comment varassigning() and use initialisation() instead


print "strategy - s0"
strat(plottype, delay, 1)



#Here each strategy is takes different inputs for probability and delays representing variations in two strategies.
for outer in range(0,3):
    for inner in range (0,length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))

print "strategy - s1"
strat(plottype, delay, 2)


for outer in range(0,3):
    for inner in range (0,length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))
print "strategy - s2"
strat(plottype, delay, 3)



for outer in range(0, 3):
    for inner in range(0, length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))
print "strategy - s3"
strat(plottype, delay, 4)



for outer in range(0, 3):
    for inner in range(0, length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))
print "strategy - s4"
strat(plottype, delay, 5)



for outer in range(0, 3):
    for inner in range(0, length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))
print "strategy - s5"
strat(plottype, delay,6)



for outer in range(0, 3):
    for inner in range(0, length):
        prob[outer][inner] = float(readfrom.read(5))
delay = int(readfrom.read(3))
readfrom.close()
print "strategy - s6"
strat(plottype, delay,7)


#for strategy s7, we have taken the probability values as those of stratgey zero but only reducing the initial susceptibilities to s/3.
print "strategy - s7"
strat(plottype, delay,8)