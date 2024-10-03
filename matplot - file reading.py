import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# create empty data lists that will be populated from the csv file data
num_students = []
num_women = []
num_men = []
majors = []

# open the csv file
file_handle = open('intro_to_python.txt', 'r')

#read from the csv
csvdata = csv.reader(file_handle)

# convert the data into a list of lists
csv_list = list(csvdata)
print(csv_list)

# get data from csv lists and put them into our data lists
for elem in csv_list:
    print(elem)
    majors.append(elem[0])
    num_students.append(int(elem[1]))
    num_women.append(int(elem[2]))
    num_men.append(int(elem[3]))
file_handle.close() # always close the file

print(majors)
print(num_students)
print(num_women)
print(num_men)

style.use('ggplot')
print(style.available)
fig1 = plt.figure(1)

# #create a subplot comprising of 3 rows, 1 column and this is the first subplot
plt.subplot(3,1,1)
line1 = plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'Total'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.title ('Majors vs Number of students')

#create a subplot comprising of 3 rows, 1 column and this is the second subplot
plt.subplot(312)
line2 = plt.plot(majors, num_women,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Women'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Female students")
#plt.title ('Majors vs Number of women')
plt.legend()

#create a subplot comprising of 3 rows, 1 column and this is the third subplot
plt.subplot(3,1,3)
line1 = plt.plot(majors, num_men,
                 color = 'yellow',
                 linestyle = '-',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Men'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Male students")

plt.show()


