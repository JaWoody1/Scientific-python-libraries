import pandas as pd

#sample pandas project

#show max columns
#pd.set_option('display.max_columns', None)

results = pd.ExcelFile("Lab.xlsx")
constantRun = pd.read_excel(results, 'Table1')
intervalSprint = pd.read_excel(results, 'Table3')


###################################
#read the first row
#print (results.head(1))
###################################

###################################
#return info on the data table
#print (results.info())
###################################

part1time = constantRun["Time"]

part2Time = intervalSprint["Time"]

print(part1time)
print(part2Time)