import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

# initialize lists
dates = []
high_values = []
open_values = []
low_values = []

# open the csv file in read mode
file_handle = open('stockvalues.csv', 'r')

# reads the content of the csv file
csvdata = csv.reader(file_handle)

# converts the CSV data into a list of lists (each sublist represents a row in the CSV file)
csv_list = list(csvdata)
print(csv_list)

# iterates over each row in the csv list and appends the data to the lists
for elem in csv_list:
    print(elem)
    # date value (appended to dates)
    dates.append(elem[0])

    # high value (converted to float and appended to high values)
    high_values.append(float(elem[1]))
    open_values.append(float(elem[2]))
    low_values.append(float(elem[3]))
file_handle.close()

print("Dates:",dates)
print("High:", high_values)
print("Open:", open_values)
print("Low:", low_values)

style.use('ggplot')
print(style.available)

# creates a new figure
fig1 = plt.figure(1)

# first subplot in a grid of 3 rows and 2 columns, selecting the first position
plt.subplot(3,2,1)

line1 = plt.plot(dates, high_values,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'High'
                 )
plt.legend()
#plt.xlabel ('Dates')
plt.ylabel ('High Values')

plt.subplot(3,1,2)
line2 = plt.plot(dates, open_values,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Open Values'
                 )
plt.ylabel ("Open Values")
plt.legend()

plt.subplot(3,1,3)

line3 = plt.plot(dates, low_values,
                 color = 'yellow',
                 linestyle = '-',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Low Values'
                 )
plt.legend()
plt.ylabel ('Low Values')
plt.show()

dates = next(csvdata)
high_values = next(csvdata)
open_values = next(csvdata)
low_values = next(csvdata)

dates = np.array(dates)
high_values = np.array(high_values, dtype=float)
open_values = np.array(open_values, dtype=float)
low_values = np.array(low_values, dtype=float)

fig, axs = plt.subplots(3, 2, figsize=(12, 8))

# 1st plot
axs[0, 0].plot(dates, high_values, label='High', color='r')
axs[0, 0].set_title('High Values')
axs[0, 0].legend()

# 2nd plot
axs[0, 1].plot(dates, open_values, label='Open', color='g')
axs[0, 1].set_title('Open Values')
axs[0, 1].legend()

# 3rd plot
axs[1, 0].plot(dates, low_values, label='Low', color='b')
axs[1, 0].set_title('Low Values')
axs[1, 0].legend()


plt.tight_layout()
plt.show()

