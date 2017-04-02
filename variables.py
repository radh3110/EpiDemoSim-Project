#properties of individal agents is as stated follows corresponding to each number
# 0 - x coordinate at present
# 1 - y coordinate at present
# 2 - region staying at present: if  0-slum 1-workplace1  2--workplace2   3--residentialArea 4-people staying at home in ra 5--school1 6--school2 7--region1 hospital1 8--hospital1r2, 9-hospital2r2  -- workplace
#        10 - market1 11 - market2
# 3 -occupation : if Value 1 is teacher, 2 is doctor, 3 is employees-- working at workplace, 4 - working at residential area, 0- children(students), 5-stay at home

# 4 - duration of exposure

# 5 - education
# 6 - level of awareness
# 7 - natural susceptibity
# 8 - diminished susceptibility
# 9 - infectivity - 0,1,2..5
# 10 - probability of getting infected

# 11 - old x
# 12 - old y
# 13 - level3 duration

# 14 - susceptibility
# 15 - infected? 0 if not infected; 1 if infected, 2 is exposed, -1 if recovered, -2 removed
# 16 - time after person is infected
# 17 - probability to recover
# 18 - name of person(number)
# 19 - age
# 20 - gender
# 21 - workX
# 22 - workY
# 23 - homeX
# 24 - homeY
# 25 - number of hospital visits
# 26 - exposed time
# 27 - time spent in hospital
# 28 - is in market?


import random

properties = 29                    #the total number of properties each agent has. For our model its 29 as stated above
people1 = 4000                     #People in  Region1
people2 = 2000                     #people in Region2
population = people1 + people2     #Total Population of agents in the model
people = [[0 for k in range(properties)] for v in range(population)]
#Here Region1 means Slum Area. People here are living in considerably high population Density.
#Region2 means Urabn Area. Here the population Density is much lesser as compared to Region1 and they are also more educated as compared to people of Region1.




levels = [0 for v in range(3)]                   #awareness levels of people. Here we have considered 3 awareness levels
alcount = [0 for v in range (3)]                 #count of people in each awareness level
alpeople10 = [0 for v in range (population) ]    #indices of people in awareness level 0
alpeople11 = [0 for v in range (population) ]    #indices of people in awareness level 1
alpeople12 = [0 for v in range (population) ]    #indices of people in awareness level 2



length = 3                                                #The number of parts you want to divide the susceptibility into
prob = [[0 for k in range(length)] for v in range(3)]     #probability matrix
costs = [[0 for k in range(length)] for v in range(3)]    #cost matrix
lowered = [[0 for k in range(length)] for v in range(3)]  #suceptibility lowered people in each awareness level
power = [0 for v in range(3)]                             #power matrix
sus = [0 for v in range(3)]                               #suceptibility input matrix
delay = [0 for v in range(3)]                             #delay input matrix
#since here we re considering 3 levels ie awareness levels, the value of 'v' in the matrix formation is considered to be in range(3)



#time is considered in hours
recoveryTime = 60               #time to recover after getting infected
totalTime = 1200                #total simulation time


#we are using influenza infection parameters here. So the next four parameters are diseases specific
incubationPeriodstart = 30      #time step at which incubation period starts after going through the latent period
incubationPeriodend = 72        #time step at which incubation period ends
latentperiod = 26               #latent period duration
transmissibility = 1.0/34.0     #transmissibility is a diseases specific property



activehoursStart = 9   #Morning 9am the activity begins
activehoursStop = 17   #Evening 5pm they return home from their workplaces
markethoursStart = 18  #Evening 6pm most of the people go to the market while some may visit between 9am to 5pm
markethoursStop = 20   #evening 8pm they return home from market. Can return in between as well



infected = 50                   #initially Infected count
probabilitytoHospi = 0.4        #Probability to go to Hospital
probabilitytoMarket = 0.2       #Probability to go to the Market in the evening
probtomarket = 0.05             #Probability to go to the Market between 9am to 5pm
probabilitytoStay = 0.3         #probability to stay at home
Probabilityforwomentostay = 0.5 #Probability for wiomen to stay at home between 9am to 5pm ie mostly housewives and due to other personal reasons
probabilityformentostay = 0.1   #probability for men to stay at home between 9am to 5pm
probtocomeback = 0.9            #probability to come back from market

infectedlist = random.sample(range(0, population), infected)     #initialize infected person



levelsindisease = 5     #5 levels in diseases
coordinates = [[[0 for p in range(levelsindisease)] for q in range(101)] for r in range(101)]   #initialised to 0



doctorsguess = population / 100     #max number of total doctors will be population/100
teachersguess = population / 50     #max number of total teachers will be population/50
doctorage = 25                      #min age requirement of doctors
teacherage = 20                     #min age requirement of teachers
studentage = 18                     #max age requirement of student




X = 20         #x axis dividing Region1 and Region2
Xmax = 100     #maximum value of x coordinate
Ymax = 100     #maximum value of y coorinate
#ie it is a 100 * 100 grid



#Below we have defined the location of each place depending upon the x and y coordinates assigned to them.
#R1 being Region 1 ie Slum region, R2 being Region 2 ie Urban region
#X1 being the start X coordinate, X2 being the ending X coordinate
#Y1 being the start Y coordinate, Y2 being the ending Y coordinate


#this residential area is only in Region2
region2ResidentialX1 = 70
region2ResidentialX2 = 100
region2ResidentialY1 = 20
region2ResidentialY2 = 70


#both Workplaces are in Region2
workplace1X1 = 45
workplace1X2 = 60
workplace1Y1 = 20
workplace1Y2 = 30
workplace2X1 = 80
workplace2X2 = 95
workplace2Y1 = 80
workplace2Y2 = 95


#one hospital in Region1 and other two being in Region2
#hospital1R2X1 = 80 means Hospital 1  in Region 2 is having starting X coordinate as 80
hospitalR1X1 = 15
hospitalR1X2 = 20
hospitalR1Y1 = 0
hospitalR1Y2 = 5
hospital1R2X1 = 80
hospital1R2X2 = 90
hospital1R2Y1 = 10
hospital1R2Y2 = 15
hospital2R2X1 = 50
hospital2R2X2 = 60
hospital2R2Y1 = 80
hospital2R2Y2 = 90


#two markets, one in Region1 and other in Region2
marketR1X1 = 6
marketR1X2 = 14
marketR1Y1 = 0
marketR1Y2 = 5
marketR2X1 = 45
marketR2X2 = 65
marketR2Y1 = 50
marketR2Y2 = 60


#Two schools, one in Region1 and other in Region2
schoolR1X1 = 0
schoolR1X2 = 5
schoolR1Y1 = 0
schoolR1Y2 = 5
schoolR2X1 = 30
schoolR2X2 = 40
schoolR2Y1 = 70
schoolR2Y2 = 90

