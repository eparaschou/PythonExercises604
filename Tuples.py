stocks = ('appl', 'amzn', 'wmt','jjj')
# choose what position the word is in and then the position of its letter
print(stocks[1][1])

# unpacking method
john = ('intro to comp',12,'Business','Freshman')
(course, roll_num, major, year) = john
print("course name =", course)
# tuples are immutable; code below will give an error
john[0] = "Elina"

# swapping example
a = 10
b = 5
print(a,b)
# swap values
temp = a
a=b
b = temp
print(a,b)

# swap using tuples
(b,a) = (a,b)
print(a,b)

#swap 4 variables
a = 3
b = 5
c = 7
d = 9
(a,b,c,d) = (d,b,a,c)
print(a,b,c,d)

# length tuple
mytuple = ("apple", "banana","cherry","banana")
print(len(mytuple))
print(mytuple.count('banana'))
print(mytuple.index('apple'))

