
from variables import *
from initialise import *
from home_work_coordinates import *
from movingpeople import *
from infecting import *
from recovery import *
from gotohospi import *
from gotomarket import *
from suscep import *
from ploting import *
from cost import *
import random
import varassigning

def strat(plottype, delay, number):
    gf = 0
    gt = 0

    infectionresult = [[0 for x in range(totalTime)] for y in range(2)]   #initialise
    recoveryresult = [[0 for x in range(totalTime)] for y in range(2)]
    infectedtemp = 0
    exposedtemp = 0
    recoveredtemp = 0
    removedtemp = 0
    peopletoHospi = [0 for x in range(totalTime)]
    peopleH = 0
    iterHospi = 0
    goingtoMarket = 0
    takencare = 0
    peopleinmarket = [0 for z in range((totalTime/24) + 1)]
    f = 0
    over = 0
    vaccinated = 0
    probabilitytomove = 0.5
    peak = 0
    peaktime = 0

    secondinitialisation(number)   #call secondinitialisation()

    for j in range(0, totalTime):   #for a Total Time

        iterHospi= 0

        if j%24 == markethoursStop+1 :        #at 9pm
            peopleinmarket[f] = goingtoMarket #initialized to zero to calculate for next day
            f += 1
            goingtoMarket = 0

        for i in range(0,people1+people2):  #calculate duration of exposure here
            if people[i][11] == people[i][0] and people[i][12] == people[i][1]:   #if agents are at same cocordinates at the next time stamp as well
               people[i][4] += 1    #Duration of exposure is incremented
            else:
                people[i][4] = 0    #else made to zero

            if people[i][9] > 0:   #if infectivity value is greater than 0
                coordinates[people[i][0]][people[i][1]][people[i][9]  - 1] += 1   #Each time a person moves onto that grid the number people with that same infectivity level increases by one
                if j > 0 :
                    coordinates[people[i][11]][people[i][12]][people[i][9] - 1] -= 1 #and in previous coordinates decrements by 1
            people[i][11] = people[i][0]
            people[i][12] = people[i][1]

        infectionresult[0][j] = exposepeople(people, population)  #calculate exposed count

        if (j % 24 >= activehoursStart) and (j % 24 <= activehoursStop) : #if 9am <= current time <= 5pm
            if j % 24 == activehoursStart :             #if time is 9am
                for i in range(0, population):
                    if(people[i][15] != 1) and (people[i][15]!= -2) and people[i][3] != 5:   #if agent is not infected and he is not removed and agent is not staying at home
                        willStay = random.random()         #then generate a random number
                        if willStay < probabilitytoStay:   #if random number is less than probability to stay at home
                            people[i][0] = people[i][23]   #agent will stay at home
                            people[i][1] = people[i][24]
                        else:
                            people[i][0] = people[i][21]  #else he is assigned workplace coordinates
                            people[i][1] = people[i][22]
                    elif people[i][15] == 1:              #if agent is infected
                        willGo = random.random()          #generate a random number
                        if willGo < probabilitytoHospi:   #if random number is less than probability to go to hospital
                            people[i][0] = people[i][21]  #he is assigned workplace coordinates
                            people[i][1] = people[i][22]
                    elif people[i][3] == 5:               #if agent stays at home
                        goingtoMarket += gotoMarket(i,j)  #agent can go to market

            elif (j % 24 > activehoursStart and j % 24 < activehoursStop):  #between 9am to 5pm
                for i in range(0, people1+people2):
                    if (people[i][15] != 1) and (people[i][15] != -2) and people[i][3] != 5:  #if agent is not infected and he is not removed and agent is not staying at home
                        if random.random() < probabilitytomove:   #if random number is less than probability to move
                            move(i,people[i][2])    #then agent will move
                    elif people[i][3] == 5:         #if agent stays at home
                        goingtoMarket += gotoMarket(i,j) #agent can go to market

                    elif people[i][15] == 1:               #if agent is infected
                        iterHospi += gotoHospi(people, i)  #agent will go to hospital
                peopletoHospi[j] = iterHospi

            elif (j % 24 == activehoursStop):   #at 5pm
                for i in range(0, people1+people2):
                    if people[i][3] != 5:             #if agent has not returned back at home
                        people[i][0] = people[i][23]  #agent will retuen back at home
                        people[i][1] = people[i][24]
                    elif people[i][3] == 5:               #if agents are at home
                        goingtoMarket += gotoMarket(i,j)  #agents can go to market

        elif (j % 24 == markethoursStart or  j% 24 == markethoursStart+1):  #between 6pm and 8pm
            for i in range(0, people1 + people2):
                goingtoMarket += gotoMarket(i,j)  #people will go to market

        elif j % 24 == markethoursStop :  #at 8pm
            for i in range(0, people1+people2):
                people[i][0] = people[i][23]  #people will return back home
                people[i][1] = people[i][24]
                people[i][28] = 0

        infectionresult[1][j] = infectingPeople(people, population) #calculate number of infected agents
        if peak < infectionresult[1][j] :
            peak = infectionresult[1][j]  #calculate peak value
            peaktime = j                  #and peak time

        #print j, ": ", infectionresult[1][j]
        infectedtemp += infectionresult[1][j]  #calculate total infected
        exposedtemp += infectionresult[0][j]   #calculate total exposed
        peopleH += peopletoHospi[j]            #calculate people who went to hospital

        if number != 8:
            if gf == 0 and infectedtemp > population/25 :  #if government flag is zero and number of infected exceeds population/25
                gf = 1  #set government flag as one
                gt = 0  #set government time as zero
                print "flag is raised at", j   #government flag is raised at jth time stamp
            #this is to test the strategies based on delay. Government flag is raised meaning government now knows about the infection spread.
            #government time starts a counter. Delay will define after a delay of how many time units will the government take actions even after its already come to the notice of authorities.
            if gf == 1: #if government flag is one
                gt += 1              #increment government time
                if gt == delay[0]:   #if government time is delay[0]
                    print gt         #print gt  
                    measure2(people, population, length, 2)  #call measure2 function
                if gt == delay[1]:   #if government time is delay[1]
                    print gt         #print gt 
                    measure1(people, population, length, 1)  #call measure1 function
                if gt == delay[2]:   #if government time is delay[2]
                    print gt         #print gt 
                    measure0(people, population, length, 0)   #call measure0 function 


        temparray = recoveringPeople(people, people1 + people2)
        recoveryresult[0][j] = temparray[0]     #recovered
        recoveryresult[1][j] = temparray[1]     #removed
        recoveredtemp += recoveryresult[0][j]   #calculate total recovered
        removedtemp += recoveryresult[1][j]     #calculate total removed

    infectionresult[1][0] = 50             #initially 50 agents are infected
    infectedtemp += infectionresult[1][0]  #add to that the count of later infected over simulation

    doplot(plottype, recoveryresult, infectionresult, totalTime, number)  #plotting
    economyimpact = (1 * levels[0]) + (2 * levels[1]) + (3 * levels[2])   #calculate economic impact


    print "After all iterations, number of people of each awareness level: ", alcount
    print "After all iterations, number of exposed people: ",exposedtemp
    print "After all iterations, number of infected people: ",infectedtemp
    print "peak: ", peak, "peaktime: ", peaktime
    print "After all iterations, number of infected people of each awareness level: ",levels
    print "After all iterations, number of succeptibility lowered people: ", lowered
    print "The economic impact caused is: ", economyimpact
    if number != 8:
        print "The cost is: ", calculatecost()
    print "After all iterations, number of recovered people: ", recoveredtemp
    print "number of people went to market: ", peopleinmarket
    print "number of people went to hospitals: ", peopleH
    #print "After all iterations, number of succeptibility lowered people: ", takencare
    #print "After all iterations, number of vaccinated people: ", vaccinated
    #print "After all iterations, number of removed people: ",removedtemp

    #pl.show()

