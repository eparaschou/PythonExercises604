import pandas as pd
#now that we have learnt about dataframes let us take raw csv data and convert it into a DF and work on it

#use the Pandas read_csv() to read a comma-separated values (csv) file into DataFrame.
df = pd.read_csv('marvel_clean.csv')

#df is a Pandas Dataframe
#by default it is assumed that first row is column titles

print (df.info()) #information about the DF
#print(df.describe())

print (df.index) #row lables
print (df.columns) #column lables

print (df.size) #total number of elements in this DF 8 columns * 64 rows = 512
print (df.values) # the values stored in each row as a python list
print (df.memory_usage()) #memory usage of each column
#first row is assumed to be col titles.
#12th row in our csv file is "Fantastic four"
print(df.loc[12])

#print the 5th, 7th and 9th rows
print(df.loc[[5,7,9]])


