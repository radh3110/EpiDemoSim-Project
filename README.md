# EpiDemoSim
EpiDemoSim is a tool  designed to help control and arrive at conclusions when dealing with epidemics in Urban area. Here, Urban area refers to area wherein there live two classes of people, those who live in Slum area where facilities, even basic ones, are lacking  and Upmarket Area where most of the facilities are readily available.  There is movement of people from one Region to another, mainly because of employment. The people living in Slum are not mostly concerned or even educated when it comes to knowing that they have an infection. So if an infection starts spreading in such Urban Scenario, how  will it  progress and how should government tackle this problem with varying strategies  is what this model depicts.


## Prerequisites
Since the Project is Coded in Python 2.7, ypur system should have Python 2.7. We have used PyCharm as the IDE, download PyCharm Community version from <https://www.jetbrains.com/pycharm/>.
After downloading so, please Install the following packages and libraries by command given below:

    $ sudo pip install XlsxWriter
    
    $ sudo pip install numpy

    $ sudo pip install matplotlib
 
    $ sudo pip install xlrd

###### Note:: Windows users can omit ``sudo`` at the start of the command.

## Running 

As can be seen, the project comprises of a number of python files. I shall briefly describe important files from them:
1) ``cost.py``: This file calculates the total cost which is associated with the lowering of susceptibility at each awareness level.

2) ``infecting.py``: Calculates the number infected and exposed agents.

3) ``infectionProbability.py``: Calculates the probability to get infected for a susceptible individual.

4) ``recovery.py``: Calculates the number of recovered and removed agents.

5) ``strategy.py`` : Defines the main procedure for the simulation we are running.

6) ``main.py`` : The main file to run the simulation.

7) ``measures.py`` : This file states the measures that help in reduction of susceptibilities when dealing with epidemics.

8) ``data.xlsx`` : The data that we have considered for running the simulation. This data has some static agent properties so that they remain same across simulations.

The ``input.txt`` file takes the input from user. The ``Explanation for Input File`` describes what should be the input and what it means. Kindly go through the same.
The code can be modified as to meet your requirements.

## Running a Sample Program
With an initial Susceptibility of 0.8 for People in Awareness Level 0, 0.5 for people in Awareness Level one and 0.3 for people in Awareness Level two, we are displaying results of two strategies here: 

| Strategies | 0   | s/3  | 2s/3 | s | 
| -----------|:---:| ----:|----:|----:|
| Strategy0  | 0 | 1, 80 | 0 | 0 |
| Strategy1  | 1, 100 | 0 | 0 | 0 |

The above table reprents two strategies with header row value representing the drop in susceptibility i.e. from  ``s`` it will either drop down to  ``0`` ,  ``s/3`` ,  ``2s/3``  or will remain at  ``s`` . The values 80 and 100  represents delay ie the time after which the government will start taking appropriate measures and only then there will be a drop in susceptibility. The column entries represent the probability values with which the susceptibility will drop down to i.e. for Strategy1 with probability 1 the susceptibility will drop down to  ``0`` from ``s`` after delay of 100 time units. Currently, for this table, the Strategies for people in varying awareness levels is same. It can be different across all three awareness levels. Detailed description is given in code.

The plots representing the difference in the number of infected individuals is given as follows:

![alt text](https://github.com/radh3110/EpiDemoSim-Project/blob/master/plots.png "Plots showing Difference between two Strategies")


The X-axis represents the time in hours and the Y-axis represents the Total Infected Individuals. As can be seen, for``Strategy0``, the total number of Infected Individuals is around ``5730`` while for ``Strategy1`` because Susceptibility drops down to ``0``, the Infected Individuals remains constant to ``1502`` after some time units.

## Authors
* Radhiya A. Arsekar
* Durga Keerthi Mandarapu
* M.V. Panduranga Rao
