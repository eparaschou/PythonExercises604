import pandas as pd

from pandas import DataFrame as DF

#below is a dictionary of informnation
myDataSet = {
    'movie1':['Howard the Duck', 'Universal Pictures', 'August 1 1986', '$37','$5070136'],
    'movie2':['Blade','New Line Cinema', 'August 21 1998', '$45', "$17073856"],
    'movie3':['X-Men', '20th Century Fox', 'July 14 2000', '$75','$54471475'],
    'movie4':['Spider-Man', 'Sony Pictures', 'May 3 2002', '$139','$114844116']
}
#we convert the above dictionary into a Pandas Dataframe to enable us to use Pandas on this data
#A Pandas data frame is a 2 dimensional data structure like a table with rows and columns
dataFrame = pd.DataFrame(myDataSet)

print(dataFrame)

# Series
import pandas as pd

#below is a standard python list
srs1 = ['Howard the Duck', 'Universal Pictures', 'August 1 1986', 37,5070136]

#converting the python list called srs1 in to a Pandas series
#A Pandas Series is a one-dimensional array of data of any type, like a column in a table.
mySeries = pd.Series(srs1)
print(mySeries)
print (mySeries[3])

import pandas as pd

srs1 = ['Howard the Duck', 'Universal Pictures', 'August 1 1986', 37,5070136]

#we can add column titles by creating another list
col_titles = ['Movie Title', 'Distributor(s)', 'Release date(United States)', 'Budget (millions)', 'Opening weekend(North America)']

#create a series and add col titles
mySeries = pd.Series(srs1, index = col_titles)
print (mySeries)
print (mySeries['Movie Title'])


# Ex1: create a list give it a title and then create a series
import pandas as pd
list1 = ['Blue', 'Red', 'Yellow', 'Green']
col_titles2 = ['Color 1:','Color 2:', 'Color 3:', 'Color 4:']
mySeries2 = pd.Series(list1, index=col_titles2)
print(mySeries2)


import pandas as pd
#create a bunch of python lists
mov1 = ['Howard the Duck', 'Universal Pictures', 'August 1 1986', 37, 5070136]
mov2 = ['Blade','New Line Cinema', 'August 21 1998', 45, 17073856]
mov3 = ['X-Men', '20th Century Fox', 'July 14 2000', 75,54471475]
mov4 = ['Spider-Man', 'Sony Pictures', 'May 3 2002', 139,114844116]


#convert them into Pandas series
srs1 = pd.Series(mov1)
srs2 = pd.Series(mov2)
srs3 = pd.Series(mov3)
srs4 = pd.Series(mov4)


#now group the series together to form a DataFrame
df1 = {'movie1':srs1, 'movie2':srs2, 'movie3':srs3, 'movie4':srs4}
mydf = pd.DataFrame(df1)
print (mydf)

# Ex2 create data frame and add row titles
import pandas
dataframe1 = {'student1' : ['Mike', 'Business', 'Greek', 4.0],
              'student2' : ['Mary','Accounting', 'Spanish', 3.9],
              'student3' : ['Sofia', 'Arts', 'Russian', 3.5],
              'student4' : ['John', 'Biology', 'Canadian', 2.5]
              }

titles = ['Name', 'Major', 'Country', 'GPA']

df = pd.DataFrame(dataframe1, index = titles)
print (df)


# class exercise - add rows titles
import pandas as pd
#create a DataFrame directly without creating the series first

dataframe1 = {
     'movie1': ['Howard the Duck', 'Universal Pictures', 'August 1 1986', 37,5070136],
     'movie2': ['Blade','New Line Cinema', 'August 21 1998', 45, 17073856],
     'movie3': ['X-Men', '20th Century Fox', 'July 14 2000', 75,54471475],
     'movie4': ['Spider-Man', 'Sony Pictures', 'May 3 2002', 139,114844116]
 }
#
myDF = pd.DataFrame(dataframe1)
# print (myDF)
# #
# print (myDF.loc[2])
# print (myDF.loc[[2,3,4]])
#
titles =  ['Title', 'Distrbutr', 'Relse dt', 'Bdgt(mil)', 'Opng wknd']
myDF = pd.DataFrame(dataframe1, index=titles)
print (myDF)
print (myDF.loc['Title'])
print (myDF.loc[['Title', 'Distrbutr']])


# Ex3
import pandas
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)