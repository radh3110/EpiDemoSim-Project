
import xlsxwriter
import matplotlib.pyplot as pl

def doplot(plottype, recoveryresult, infectionresult,totalTime,number):
    if number == 1:   #create excel files depending upon the nuber of strategies. Each excel file will hold results for different strategies
        workbook = xlsxwriter.Workbook('results.xlsx')
    elif number == 2:
        workbook = xlsxwriter.Workbook('results1.xlsx')
    elif number == 3:
        workbook = xlsxwriter.Workbook('results2.xlsx')
    elif number == 4:
        workbook = xlsxwriter.Workbook('results3.xlsx')
    elif number == 5:
        workbook = xlsxwriter.Workbook('results4.xlsx')
    elif number == 6:
        workbook = xlsxwriter.Workbook('results5.xlsx')
    elif number == 7:
        workbook = xlsxwriter.Workbook('results6.xlsx')
    elif number == 8:
        workbook = xlsxwriter.Workbook('results7.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    col = 0
    worksheet.write('A1', 'Time')           #first column time
    worksheet.write('B1', 'Exposed')        #second column number of exposed agents at each time stamp
    worksheet.write('C1', 'Total Exposed')  #third column cumulative exposed agents
    worksheet.write('D1', 'Infected')       #fourth column number of infected agents at each time stamp
    worksheet.write('E1', 'Total Infected') #fifth column cumulative infected agents
    worksheet.write('F1', 'Recovered')      #sixth column number of recovered agents at each time stamp
    worksheet.write('G1', 'Total Recovered')#seventh column cumulative recovered agents
    worksheet.write('H1', 'Removed')        #eighth column number of removed agents at each time stamp
    worksheet.write('I1', 'Total Removed')  #ninth column cumulative removed agents

    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    if plottype == 2:
        for i in range(0,totalTime):
            pl.plot(i ,infectionresult[0][i] , 'yo')    #infectionresult[0][i]  represents exposed agents
            pl.plot(i, infectionresult[1][i], 'ro')     #infectionresult[1][i] represents infected agents
            pl.plot(i,recoveryresult[0][i], 'go')       #recoveryresult[0][i] represents recovered agents
            pl.plot(i, recoveryresult[1][i], 'bo')      #recoveryresult[1][i] represents removed agents
            number1 += infectionresult[0][i]            #adding to calculate the cumulative numbers
            number2 += infectionresult[1][i]
            number3 += recoveryresult[0][i]
            number4 += recoveryresult[1][i]
            worksheet.write(row, col, i)
            worksheet.write(row, col + 1, infectionresult[0][i])
            worksheet.write(row, col + 2, number1)
            worksheet.write(row, col + 3, infectionresult[1][i])
            worksheet.write(row, col + 4, number2)
            worksheet.write(row, col + 5, recoveryresult[0][i])
            worksheet.write(row, col + 6, number3)
            worksheet.write(row, col + 7, recoveryresult[1][i])
            worksheet.write(row, col + 8, number4)
            row += 1
    else:
        for i in range(0, totalTime):         #as stated above
            number1 += infectionresult[0][i]  #exposed
            number2 += infectionresult[1][i]  #infected
            number3 += recoveryresult[0][i]   #recovered
            number4 += recoveryresult[1][i]   #removed
            worksheet.write(row, col, i)
            worksheet.write(row, col + 1, infectionresult[0][i])
            worksheet.write(row, col + 2, number1)
            worksheet.write(row, col + 3, infectionresult[1][i])
            worksheet.write(row, col + 4, number2)
            worksheet.write(row, col + 5, recoveryresult[0][i])
            worksheet.write(row, col + 6, number3)
            worksheet.write(row, col + 7, recoveryresult[1][i])
            worksheet.write(row, col + 8, number4)
            row += 1
            pl.plot(i, number1 , 'yo')    #exposed
            pl.plot(i, number2, 'ro')     #infected
            pl.plot(i, number3, 'go')     #recovered
            pl.plot(i, number4, 'bo')     #removed

    workbook.close()