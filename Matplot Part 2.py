import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# vertical bar chart
num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))

style.use ('ggplot')
#by default matplotlib.pyplot has a width of 0.8
width = .25
#yerr = (38 25 32 7)
plt.bar(x, num_students, width,  label = 'total' )

for i in x:
    plt.annotate( str(num_students[i]) ,  (x[i],num_students[i]) )


plt.bar(x+.25, num_men, width, label = 'men')
plt.bar(x+.5, num_women, width, label = 'women')

plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.xticks(x+.25, majors)
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()

# bar chart
num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))
print (x)

style.use ('ggplot')

#plt.bar(x, num_students, label = 'total')
#plt.bar(x, num_men, label = 'men')
#plt.bar(x, num_women, label = 'women')

#horizontal bar chart
plt.barh(x, num_students, label = 'total')
plt.barh(x, num_women, label = 'women')


plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.xticks(x, majors)
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()

# subplots
num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

style.use('ggplot')

fig1 = plt.figure('Subplots')

# 1st plot
plt.subplot(3, 2, 1)
plt.plot(majors, num_students, color='green', linestyle='dashed', marker='s', linewidth=3, label='Total')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Number of students")
plt.title('Majors vs Number of students')

# 2nd plot
plt.subplot(3, 2, 2)
plt.plot(majors, num_women, color='red', linestyle='-', marker='o', linewidth=2, label='Women')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Female students")

# 3rd plot
plt.subplot(3, 2, 3)
plt.plot(majors, num_men, color='yellow', linestyle='-', marker='v', linewidth=2, label='Men')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Male students")

# 4th plot
plt.subplot(3, 2, 4)
plt.plot(majors, num_students, color='blue', linestyle='-', marker='x', linewidth=2, label='Total')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Number of students")

# 5th plot
plt.subplot(3, 2, 5)
plt.plot(majors, num_women, color='purple', linestyle='-', marker='*', linewidth=2, label='Women')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Female students")

# 6th plot
plt.subplot(3, 2, 6)
plt.plot(majors, num_men, color='orange', linestyle='-', marker='d', linewidth=2, label='Men')
plt.legend()
plt.xlabel('Majors')
plt.ylabel("Male students")

plt.tight_layout()
plt.show()

# ---------------------------------------- #

# subplots - line chart and bar chart
days = ["Mon", "Tue","Wed","Thu","Fri"]
money_earned_thisweek = [20345,6454,90076,87765,68794]
money_earned_lastweek = [94788, 89710, 55308, 17630, 21309]
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('white')

# line chart - subplot 1
ax[0].plot(days,money_earned_thisweek,"o-g")
ax[0].plot(days,money_earned_lastweek,"v--m")
ax[0].set_title("Money Earned This Week vs. Last Week")
ax[0].set_xlabel("Days of the week")
ax[0].set_ylabel("Money Earned")

ax[0].patch.set_facecolor('white')
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['left'].set_color('black')
ax[0].spines['bottom'].set_color('black')


# bar chart - subplot 2
# Plot bar chart
x_range_current = [-0.2, 0.8, 1.8, 2.8, 3.8]
x_range_previous = [0.2, 1.2, 2.2, 3.2, 4.2]

ax[1].bar(width, money_earned_thisweek, width=0.3, color="g")
ax[1].bar(width, money_earned_lastweek, width=0.3, color="m")
ax[1].bar(x_range_current, money_earned_thisweek)
ax[1].bar(x_range_previous, money_earned_lastweek)
ax[1].set_title("Money Earned This Week vs. Last Week")
ax[1].set_xlabel("Days of the week")
ax[1].set_ylabel("Money Earned")
ax[1].set_xticks(range(5))
ax[1].set_xticklabels(days)


ax[1].patch.set_facecolor('white')
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['left'].set_color('black')
ax[1].spines['bottom'].set_color('black')

plt.show()


