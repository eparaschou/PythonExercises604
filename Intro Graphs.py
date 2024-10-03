import matplotlib.pyplot as plt
import numpy as np

# create two lists and draw them
days = ["Mon", "Tue","Wed","Thu","Fri"]
money_earned_thisweek = [2345,654,9076,8765,6794]
money_earned_lastweek = [9788, 8710, 5308, 17630, 21309]
fig, ax = plt.subplots()
ax.set_title("Money Earned This Week vs. Last Week")
ax.plot(days, money_earned_thisweek, "o-g")
ax.plot(days, money_earned_lastweek, "v--m")
ax.legend(["This week", "Last week"])
plt.show()

#data sets
num_students = [38, 25, 32, 7]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

#use the plot function from pyplot module
line1 = plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = ':',
                 marker = 's',
                 linewidth = 5,
                 )
plt.show()


# scatterplot
days = ["Mon", "Tue","Wed","Thu","Fri"]
steps_walked = [8934,2345,5678,9087,5674]

plt.plot(days, steps_walked, "o-")
plt.show()

# line charts advanced
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]
steps_last_week = [9788, 8710, 5308, 17630, 21309, 4002, 5223]
fig, ax = plt.subplots()
ax.plot(days, steps_walked, "o-g")
ax.plot(days, steps_last_week, "v--m")
ax.set_title("Step count | This week and last week")
ax.set_xlabel("Days of the week")
ax.set_ylabel("Steps walked")
ax.grid(True)
ax.legend(["This week", "Last week"])
fig.legend(["Steps this week", "Steps last week"])
plt.show()

# line chart simple
num_students = [38, 25, 32, 7]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']
line1 = plt.plot(majors, num_students)
plt.show()

