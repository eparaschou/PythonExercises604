import matplotlib.pyplot as plt
from matplotlib import style

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

style.use ('ggplot')
#print (style.available)

line1 = plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'Total Number'
                 )
line2 = plt.plot(majors, num_women,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Women'
                 )
line3 = plt.plot(majors, num_men,
                 color = 'black',
                 linestyle = ':',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Men'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()

# multiple charts in one
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()