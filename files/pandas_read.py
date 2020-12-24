import pandas as pd
import xlrd
filename = 'plain.csv'
data = pd.read_csv(filename)
print(data)

data_array = data.values

# import xlrd 
  
# # Give the location of the file 
# loc = ('plain.csv') 
  
# # To open Workbook 
# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
  
# # For row 0 and column 0 
# sheet.cell_value(0, 0) 
