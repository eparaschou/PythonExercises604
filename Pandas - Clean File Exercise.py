import pandas as pd

df = pd.read_csv('marvel_dirty.csv')
#print (df.info()) #information about the DF
#Info shows us that there are some rows with nulls in them. That is why we see row count as 66 or 65
#note that the nulls are spread out in different rows and not all in the same row

#drop the rows which contain empty cells
#df_1 = df.dropna() #dropna() creates a new dataframe
#print (df_1.info())
#info shows us that the rows with nulls have been removed and now we have 64 rows of data only

#replace the data in the empty cells with some value
df.fillna(130, inplace = True) #this does not create a new DF but replaces information in the same DF
print (df.info())
print (df.tail(5))

#removing dulicates
import pandas as pd
#use the file which you 'dirtied'
df = pd.read_csv('marvel_dirty.csv')
#print(df.duplicated()) #find all rows that are dulicates of some other row

#df.drop_duplicates(inplace = True) #drop the dulicate rows
#print(df.duplicated())