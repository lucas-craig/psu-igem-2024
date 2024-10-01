import numpy as np
import scipy as sp
from scipy.interpolate import CubicSpline
import openpyxl
import pandas as pd
from scipy.interpolate import interp1d


class converter:
    
    __path_to_tblOfVals = "" #private attribute - this would be set to the name of the table containing final calibration dataset
    std = 1 #chosen arbitrarily due to lack of multi-trial data
    #__path_to_tblOfVals = "placeholder_dataset_1.xlsx"

    #def __init__(self):
    #    path_to_tblOfVals = "placeholder_dataset_1.xlsx" #use placeholder dataset if no table of vals provided

    def __init__(self, excel_tblOfVals=None): #default table of vals is placeholder_dataset_1
        #self.wordList = wordList if wordList is not None else []
        if excel_tblOfVals != None and excel_tblOfVals is not isinstance(excel_tblOfVals, str):
            raise TypeError("Path must be a string.")
        else:
            self.__path_to_tblOfVals = excel_tblOfVals if excel_tblOfVals is not None else "placeholder_dataset_1.xlsx"
        
        #self.__path_to_tblOfVals = excel_tblOfVals

    def __get_path_to_tblOfVals(self):
        return self.__path_to_tblOfVals

    #Converts excel file to dataframe, then uses dataframe to produce independent, dependent
    #var arrays and return them in a tuple. Assumes that indep. var is in first col and dep. var is in 2nd
    def __getDataFromTable(self):#, code):
        cols_to_use = ""
        sheet_name = 0
        cols_to_use="A,B"
        """
        if(code == 0):
            cols_to_use="A,D"
        elif(code == 1):
            cols_to_use="B,D"
        else:
            cols_to_use="C,D"
        """
        df = pd.read_excel(self.__get_path_to_tblOfVals(), 
                    usecols=cols_to_use, #use cols A and B of dataset
                    #dtype={"A": np.float64, "B": np.int32}, #set col A datatype to float32, B to int32
                    skiprows=[0]) #skip first row (contains irrelevant notes; col names are in 2nd row)
        iv_arr = df[df.columns[0]].to_numpy()
        dv_arr = df[df.columns[1]].to_numpy()
        return (iv_arr, dv_arr)
    
    def __interpolate(self, iv_arr, dv_arr, input_pt):
        cubicspln_interpln = CubicSpline(iv_arr, dv_arr)
        return cubicspln_interpln(input_pt)

    def __average_RoC(self, arr, mmnt_intrvl):
        #assume arr size of 5
        #4 lines can be drawn between 5 consecutive points
        roc_sum = 0
        for i in range(1, 5):
            roc_sum += (arr[i] - arr[i-1])/mmnt_intrvl
        roc_avg = roc_sum/4
        return roc_avg

    def convertConcentration(self, mmnt_arr, mmnt_intrvl):
        avg_RoC = self.__average_RoC(mmnt_arr, mmnt_intrvl)
        #print(mmnt_arr) #debugging
        #print(avg_RoC) #debugging
        if (avg_RoC < 0):
            return -1
        #cols = self.__getDataFromTable(0)
        cols = self.__getDataFromTable()
        mean = self.__interpolate(cols[0],cols[1], avg_RoC)
        #cols = self.__getDataFromTable(1)
        mean_plus_std = self.__interpolate(cols[0],cols[1], avg_RoC+self.std)
        #cols = self.__getDataFromTable(2)
        mean_minus_std = self.__interpolate(cols[0],cols[1], avg_RoC-self.std)
        return [mean, mean_plus_std, mean_minus_std]
        #return f"mean: {mean} mean+SD: {mean_plus_std}  mean-SD: {mean_minus_std}"
    

mmnt_arr=[20,30,40,50,60]
c = converter()
print(c.convertConcentration(mmnt_arr,10))


"""
#Create dataframe with placeholder for main calculator 
#will be replaced with characterization data
phdata1_df = pd.read_excel("placeholder_dataset_1.xlsx", 
                sheet_name=1, 
                usecols="A:B", 
                dtype={"A": np.float64, "B": np.int32},
                skiprows=[0]) #skip first row (contains irrelevant notes; col names are in 2nd row)
"""

#cnvrtr = converter()
#print(cnvrtr.convertConcentration(40, 40, 20.0))


    #print(phdata1_df)


    #cubicspln_interpln_fn = CubicSpline(iv_arr, dv_arr)

    #def interp(float mesasuremnt1, float measuremnt1):
        

    #print(iv_arr)
    #print(dv_arr)

    #numpy.interp(x, xp, fp, left=None, right=None, period=None)

