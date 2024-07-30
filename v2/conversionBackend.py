import numpy as np
import scipy as sp
from scipy.interpolate import CubicSpline
import openpyxl
import pandas as pd
from scipy.interpolate import interp1d

#TODO: ADD CSV SUPPORT
#TODO: get constructor working properly. __path_to_tblOfVals never gets initialized

class converter:
    
    __path_to_tblOfVals = "" #private attribute
    #__path_to_tblOfVals = "placeholder_dataset_1.xlsx"

    #def __init__(self):
    #    path_to_tblOfVals = "placeholder_dataset_1.xlsx" #use placeholder dataset if no table of vals provided

    def __init__(self, excel_tblOfVals=None): #default table of vals is placeholder_dataset_1
        #self.wordList = wordList if wordList is not None else []
        self.__path_to_tblOfVals = excel_tblOfVals if excel_tblOfVals is not None else "placeholder_dataset_1.xlsx"
        if excel_tblOfVals != None and excel_tblOfVals is not isinstance(excel_tblOfVals, str):
            raise TypeError("Path must be a string.")
        #self.__path_to_tblOfVals = excel_tblOfVals

    def __get_path_to_tblOfVals(self):
        return self.__path_to_tblOfVals

    #Converts excel file to dataframe, then uses dataframe to produce independent, dependent
    #var arrays and return them in a tuple. Assumes that indep. var is in first col and dep. var is in 2nd
    def __getDataFromTable(self):
        df = pd.read_excel(self.__get_path_to_tblOfVals(), 
                    sheet_name=1, 
                    usecols="A:B", #use cols A and B of dataset
                    #dtype={"A": np.float64, "B": np.int32}, #set col A datatype to float32, B to int32
                    skiprows=[0]) #skip first row (contains irrelevant notes; col names are in 2nd row)
        iv_arr = df[0].to_numpy()
        dv_arr = df[1].to_numpy()
        return (iv_arr, dv_arr)
    
    def __interpolate(self, iv_arr, dv_arr, input_pt):
        cubicspln_interpln = CubicSpline(iv_arr, dv_arr)
        return cubicspln_interpln(input_pt)

    def convertConcentration(self, mmt1, mmt2):
        increase = mmt2 - mmt1
        #TODO: ADD MARGIN OF ERROR IN CASE ACTUAL CONCENTRATION REMAINS CONSTANT BUT SECOND MEASURED CONCENTRATION DECREASES
        if increase < 0:
            raise ValueError("Glucose concentration should not decrease.")
        cols = self.__getDataFromTable()
        return self.__interpolate(cols, increase)
        

    """
    #Create dataframe with placeholder for main calculator 
    #will be replaced with characterization data
    phdata1_df = pd.read_excel("placeholder_dataset_1.xlsx", 
                    sheet_name=1, 
                    usecols="A:B", 
                    dtype={"A": np.float64, "B": np.int32},
                    skiprows=[0]) #skip first row (contains irrelevant notes; col names are in 2nd row)
    """

cnvrtr = converter()
print(cnvrtr.convertConcentration(10,20))


    #print(phdata1_df)


    #cubicspln_interpln_fn = CubicSpline(iv_arr, dv_arr)

    #def interp(float mesasuremnt1, float measuremnt1):
        

    #print(iv_arr)
    #print(dv_arr)

    #numpy.interp(x, xp, fp, left=None, right=None, period=None)

