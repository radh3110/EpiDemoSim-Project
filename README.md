# EpiDemoSim
EpiDemoSim is a tool  designed to help control and arrive at conclusions when dealing with epidemics in Urban area. Here, Urban area refers to area wherein there live two classes of people, those who live in Slum area where facilities, even basic ones, are lacking  and Upmarket Area where most of the facilities are readily available.  There is movement of people from one Region to another, main reason of it being employment. The people living in Slum are not mostly concerned or even educated when it comes to knowing that they have an infection. So if an infection starts spreading in such Urban Scenario, how  will it  progress and how should government tackle this problem with varying strategies  is what this model depicts.


## Prerequisites
Since the Project is Coded in Python 2.7, ypur system should have Python 2.7. We have used PyCharm as the IDE, download PyCharm Community version from <https://www.jetbrains.com/pycharm/>.
After downloading so, please Install the following packages and libraries by command given below:

    $ sudo pip install XlsxWriter
    
    $ sudo pip install numpy

    $ sudo pip install matplotlib
 
    $ sudo pip install xlrd

.. Note::
   Windows users can omit ``sudo`` at the start of the command.

## Installing

As can be seen, the project comprises of a number of python files. I shall briefly describe each of them:
1) cost.py :
This file calculates the total cost whic is associated with the lowering of susceptibility at each awareness levels.

2) gotohospi.py and gotomarket.py:
   These files are associated with agents going to hospital and market when the constraints are satisfied.

3) home_work_coordinates.py and movingpeople.py:
home_work_coordinates assigns home and work coordinates to agents and  movingpeople.py controls their movement to work places and within the specified place as well.

4) infecting.py
Calculates the number infected and exposed agents

5) infectionProbability.py
calculates the probability to get infected for a susceptible individual

6) recovery.py
Calculates the number of recovered and removed agents

7) strategy.py
Defines the main procedure for the simulation we are running.

8) suscep.py
Calculates the number of people who lowered their susceptibilities

9) variables.py and initialise.py
Defines variables and properties for agent and initialises them.

10) plotting.py
Associated with plotting and writing the data to excel spreadsheet

11) main.py
The main file to run the simulation.



