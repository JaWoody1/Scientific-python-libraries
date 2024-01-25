import pandas as pd

#sample pandas project

#show max columns
#pd.set_option('display.max_columns', None)


#print
results = pd.read_excel("Lab.xlsx")


###################################
#read the first row
#print (results.head(1))
###################################

###################################
#return the data type of each row
print (results)