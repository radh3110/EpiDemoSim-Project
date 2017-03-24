
from variables import *
from initialise import *
import xlrd
import numpy as np

def varassigning():
    ExcelFileName= 'Data.xlsx'
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("Sheet1") # We need to read the data from the Excel sheet named "Sheet1"

    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data = []
    for curr_row in range(1, num_rows, 1):
        row_data = []
        for curr_col in range(0, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col)# Read the data in the current cell
            if data == int(data):
                row_data.append(int(data))
            else:
                row_data.append(data)

        result_data.append(row_data)

    temp_id=[]    #initialise
    temp_occupation=[]
    temp_edu=[]
    temp_LA=[]
    temp_NS=[]
    temp_Inf=[]
    temp_Age=[]
    temp_gender=[]
    temp_WorkX=[]
    temp_WorkY=[]
    temp_HomeX=[]
    temp_HomeY=[]
    temp_PS=[]
    temp_Susc=[]
    temp_DS= []

    temp_id.append([item[0] for item in result_data]) #separate from sublist to single list
    temp_occupation.append([item[1] for item in result_data])
    temp_edu.append([item[2] for item in result_data])
    temp_LA.append([item[3] for item in result_data])
    temp_NS.append([item[4] for item in result_data])
    temp_Inf.append([item[5] for item in result_data])
    temp_Age.append([item[6] for item in result_data])
    temp_gender.append([item[7] for item in result_data])
    temp_WorkX.append([item[8] for item in result_data])
    temp_WorkY.append([item[9] for item in result_data])
    temp_HomeX.append([item[10] for item in result_data])
    temp_HomeY.append([item[11] for item in result_data])
    temp_PS.append([item[12] for item in result_data])
    temp_Susc.append([item[13] for item in result_data])
    temp_DS.append([item[14] for item in result_data])

    id = np.array(temp_id)   #convert to array
    occ = np.array(temp_occupation)
    edu = np.array(temp_edu)
    LA = np.array(temp_LA)
    NS = np.array(temp_NS)
    Inf = np.array(temp_Inf)
    Age = np.array(temp_Age)
    Gender = np.array(temp_gender)
    WorkX = np.array(temp_WorkX)
    WorkY = np.array(temp_WorkY)
    HomeX = np.array(temp_HomeX)
    HomeY = np.array(temp_HomeY)
    Ps = np.array(temp_PS)
    Susc = np.array(temp_Susc)
    DS = np.array(temp_DS)

    for i in range(0,population):  #assign to the respective agent properties
        people[i][18] = id[0][i]
        people[i][3] = occ[0][i]
        people[i][5] = edu[0][i]
        people[i][6] = LA[0][i]
        people[i][7] = NS[0][i]
        people[i][15] = Inf[0][i]
        people[i][19] = Age[0][i]
        people[i][20] = Gender[0][i]
        people[i][21] = WorkX[0][i]
        people[i][22] = WorkY[0][i]
        people[i][23] = HomeX[0][i]
        people[i][24] = HomeY[0][i]
        people[i][2] = Ps[0][i]
        people[i][14] = Susc[0][i]
        people[i][8] = DS[0][i]

    for i in range(0,population):
        alcount[people[i][6]] +=1
