# for loop -> used to iterate over a sequence of items like string, tuple, range
# while loop --> used to repeatedly execute a block of statements while a condition is true
# when the condition is not given they will run into an infinite loop
items = ['pen', 'notebook', 'pencil']
for item in items:
    print(item)

items = ['pen', 'notebook', 'pencil']
index = 0
items_len = len(items)
while index<items_len:
    print(items[index])
    index = index + 1

i = 1
while i < 6:
    print(i)
    i += 1

# A list is a collection which is ordered and changeable. Allows duplicate members
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
my_list.append(6)
print(my_list)

# A dictionary is a collection which is unordered, changeable, and indexed. No duplicate members
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])
my_dict["age"] = 26
print(my_dict)

import math
print(math.sqrt(16))

for i in range(1,11):
    print('Current value:',i)

# patterns --> iterate through rows (i) and through columns (j)
# add a new line after each iteration of the outer loop
# half pyramid
rows = 5
i = 0
# outer loop -> iterates from i to rows with a step of 1
for i in range(i, rows + 1, 1):
    # inner loop iterates from 1 to current value of i with a step of 1
    for j in range(1, i+1):
        print(j, end=' ')
    print("")

# inverted pyramid
rows = 5
# iterates from 5 to 1 with a step of -1
for i in range(rows, 0, -1):
    # iterates from 0 to the current value of i
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

# Ex1: Square of numbers
numbers_square = [1, 2, 3, 4, 5]
for number in numbers_square:
    square = number ** 2
    print(f"The square of {number} is {square}")

# Ex2: Even numbers
numbers_even = [1,2,3,4,5,6,7,8,9,10]
for number in numbers_even:
    if number % 2 == 0:
        print(number)

# Ex3: print if a num is even
numbers_even = [1,2,3,4,5,6,7,8,9,10]
even_count = 0

for number in numbers_even:
    if number % 2 == 0:
        even_count += 1
print(f"The count of even numbers is: {even_count}")

# Ex4: Print sum of squares
list_numbers = [1,2,3,4,5]
sum_sqaures = 0
for number in list_numbers:
    square = number ** 2
    sum_sqaures += square
print(f"The sum of squares of the numbers in the list is: {sum_sqaures}")

# Ex5: print square if num even, cube if it's odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        result = number ** 2
        print(f"The square of {number} is {result}")
    else:
        result = number ** 3
        print(f"The cube of {number} is {result}")

#Ex6 Count number of words of length of 5 in the following paragraph
str1 = "Understand that canyo hard problems are here and it is ok you can go through it. I am a business analyst and I have a background in finance"
list1 = str1.split()
count = 0
for word in list1:
    if len(word) == 5:
        count +=1
print(count)

# while loop example different versions
countdown = 10
while countdown>0:
    print(countdown)
    countdown  -= 1
print("Blastoff")

for i in range(10):
    print(i)
print("Blastoff")

count = 0
while (True):
    print(count)
    count+=1
    if count > 10:
        break
    else:
        continue
    print("count =", count)
print("Blastoff")

# Using a while loop find the sum of all digits from 1 to 100
sum = 0
num = 1
while num <101:
    sum += num
    num += 1
    print(num)
print(sum)

# create a list of all even numbers between 0 and 100 using while loop
even_num = []
num = 0
while num < 101:
    if num % 2 == 0:
        even_num.append(num)
    num += 1
print(even_num)


# Using a while loop find the factorial of number. Use input statement to get the number
# my solution
num = int(input("Enter a number: "))

factorial = 1

while num>=1:
    factorial *= num
    num -=1
print(factorial)

# professor's solution
product = 1 # cause if a product starts with 0 it will forever stay 0
num = 1
factorial = int(input("Enter a number: "))
while num <= factorial:
    product *= num
    num += 1
print(product)

# use the while loop to find the smallest number that is divisible by all integers from 1 to 9
# answer 2520

a = 1
b = 1
count = 3
fib = [a,b]
print("first term =", a)
print("second term=", b)
sum = 0
while count <=100:
    next_term = a+b
    fib.append(next_term)
    a=b
    b=next_term
    count += 1
print(fib)

a = 1
b = 1
count = 3
fib = [a,b]
sum = 0
while True :
    next_term = a+b
    print (count, "th term = ", next_term)
    a,b = b, next_term #this is the swap statement
    count += 1
    fib.append(next_term)
    if (count == 10):
        break
print (fib)


a=1
b=1
count = 2
fib = [a,b]

sum1 = a+b

while count < 5:
    next_term = a+b
    fib.append(next_term)
    a,b = b, next_term
    count += 1
    sum1 = sum1 + next_term

print(fib)
print(sum1)
print(sum(fib))


# find the sum of the first 4 terms of the fibonacci series
a = 1
b = 1
count = 2
sum_fib = a + b
while count <= 5:
    next_term = a + b
    sum_fib += next_term
    a = b
    b = next_term
    count += 1

print(a,b,next_term)
print("sum of the first 4 terms:", sum_fib)

# arithmetic series exercise
a1 = 1
d = 3
n = 1
series = []
while n < 10:
    a_n = a1 + (n-1) * d
    series.append(a_n)
    n += 1
print("First 10 terms of the series:", series)

# triangular numbers exercise
n = 1
trian_numbers = []
while n < 10:
    tn = (n * (n + 1)) // 2
    trian_numbers.append(tn)
    n += 1
print(trian_numbers)

# for loop fibonacci series exercise
a = 1
b = 1
fib = [a, b]
for count in range(3, 101):
    next_term = a + b
    fib.append(next_term)
    a,b = b, next_term
print(fib)

# geometric series for loop
a1 = 2
r = 2
geometric_series = []
for n in range(1, 11):
    an = a1 * (r ** (n - 1))
    geometric_series.append(an)
print(geometric_series)



# geometric series while loop
a1 = 2
r = 2
n = 1
geom_series = []
while n < 10:
    an = a1 * (r ** (n - 1))
    geom_series.append(an)
    n += 1
print(geom_series)

# find the first term in the fibonacci series greater than 10000
a = 1
b = 1
n = 3
while True:
    next_term = a + b
    if next_term > 10000:
        break
    a,b = b,next_term
    n += 1

print("the number greater than 10000 is:", next_term, ", the position in the series",n)

# while loop
target = int(input())
n = int(input())
step = 4
while n >= target:
    print(n * 2)
    n -= step

# while loop
total_product = 1
curr_value = int(input())
while curr_value > 0:
    total_product = total_product * curr_value
    curr_value = int(input())
print(f'Product: {total_product}')

# Write a loop that iterates while input_num is not equal to 35.
# in each iteration print 'Still waiting for 35'.
# in each iteration Read integer input_num from input.

input_num = int(input())

while input_num != 35:
    print( 'Still waiting for 35')
    input_num = int(input())

print('Got 35!')

# reverse numbers
numbers = [3, 8, 6, 4]
for number in reversed(numbers):
    print(number)

# for loop
cities = {
    'Toronto': 982,
    'Chicago': 584,
    'Paris': 438,
}
best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)